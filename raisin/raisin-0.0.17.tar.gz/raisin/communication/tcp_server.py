#!/usr/bin/env python3

"""
|========================================|
| C'est la partie qui permet de recevoir |
| des clients et de leur repondre.       |
|========================================|

Ce script permet seulement de faire le lien entre
les clients et le reste du programe. Les reponses
aux requettes ne sont pas faites ici.

Ce fichier est fortement influance par ce lien:
    https://www.neuralnine.com/tcp-chat-in-python/
"""

import multiprocessing
import os
import socket
import sys
import threading
import time
import uuid

from raisin import dumps, loads
from ..tools import Printer, identity, timeout_decorator
from ..application.settings import settings
from ..errors import *
from . import checks, request, routing


class Server:
    """
    |================================================|
    | Serveur raisin qui accepte les clients raisin. |
    |================================================|

    C'est un serveur qui supporte les requettes ipv6 et ipv4.
    Il accepte plusieurs clients a la fois jusqu'a la limite autorisee.

    exemple
    -------
    :Example:
    >>> from raisin.communication import tcp_server
    >>> s = tcp_server.Server()
    >>> s.start() # Methode bloquante.
    """
    def __init__(self):
        """
        Constructeur qui initialise juste les 
        sockets de facon locale.
        """
        with Printer("Initialisation of TCP servers...") as p:
            # partie environement
            self.clients = {}               # c'est tous les clients connectes

            # partie serveur
            self.port = settings["server"]["port"]
            self.listen = settings["server"]["listen"]
            self.ipv4 = identity["ipv4_lan"]
            self.ipv6 = identity["ipv6"]
            if self.ipv4 == None and self.ipv6 == None:
                raise ConnectionError(
                    "Impossible de detecter l'ip, peut etre n'y a-t-il pas internet?")

            addr = ("", self.port)  # Toutes les interfaces, port 'self.port'
            if identity["python_version"] >= "3.8":
                if socket.has_dualstack_ipv6():
                    self.tcp_socket = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True, reuse_port=True)
                else:
                    self.tcp_socket = socket.create_server(addr, reuse_port=True)
            else: # La gestion mixe ipv6 ipv4 n'est disponible que a partir de python3.8 .
                if self.ipv6:
                    self.tcp_socket = socket.socket(
                        socket.AF_INET6,        # socket internet en ipv6
                        socket.SOCK_STREAM)     # creation d'un TCP/IP socket, SOCK_STREAM=>TCP
                    self.tcp_socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)
                    self.tcp_socket.bind(addr)
                else:
                    self.tcp_socket = socket.socket(
                        socket.AF_INET,         # socket internet plutot qu'un socket unix
                        socket.SOCK_STREAM)     # creation d'un TCP/IP socket, SOCK_STREAM=>TCP
                    self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # on tente de reutiliser le port si possible
                    self.tcp_socket.bind(addr)
            # On empeche que la file d'attente soit plus longue
            # que le nombre max de clients acceptable.
            self.tcp_socket.listen(settings["server"]["listen"])

            # Partie information (hmi).
            if self.ipv4 and self.ipv6 and identity["python_version"] >= "3.8":
                message = "aux adresses '%s' et '%s'" % (self.ipv6, self.ipv4)
            else:
                message = "a l'adresse '%s'" % (self.ipv6 if self.ipv6 else self.ipv4)
            p.show("En ecoute sur le port %d %s..." % (self.port, message))

    def is_accepted(self, mac):
        """
        |====================================|
        | S'assure que le client est fiable. |
        |====================================|

        Ne pose aucune question a l'utilisateur, retourne sans attendre.

        entree
        ------
        :param mac: C'est l'adresse mac du client qui passe a la casserole.
        :type mac: str

        sortie
        ------
        :return: True si le client a le droit de se connecter, False sinon.
        :rtype: boolean
        """
        with Printer("Testing if a pecific client is accepted...") as p:
            blacklisted = os.path.join(os.path.expanduser("~"), ".raisin", "blacklisted.txt")
            if os.path.exists(blacklisted):
                with open(blacklisted, "r", encoding="utf-8") as f:
                    if mac in (l.split()[0] for l in f.readlines()):
                        p.show("The client %s is blacklisted." % mac)
                        return False
            whitelisted = os.path.join(os.path.expanduser("~"), ".raisin", "whitelisted.txt")
            if os.path.exists(whitelisted):
                with open(whitelisted, "r", encoding="utf-8") as f:
                    if mac in (l.split()[0] for l in f.readlines()):
                        p.show("The client %s is accepted." % mac)
                        return True
            if settings["server"]["accept_new_client"]:
                p.show("The client %s is automaticaly accepted." % mac)
                return True
            p.show("Maybe, we must ask the question.")
            return None

    def accept(self, client_id):
        """
        |=====================|
        | Memorise le client. |
        |=====================|

        Ajoute le client passe en parametre dans la liste blanche
        ou a la liste noir si l'utilisateur le veut.
        Si il faut attendre l'approbation de l'utilisateur,
        cette fonction est bloquante.
        Si l'utilisateur est trop long a se decider. Le client
        est blacliste et un mail est envoye a l'utilisateur.

        entree
        ------
        :param client_id: Carte d'identite du client.
        :type client_id: dict

        sortie
        ------
        :return: True si le client est en mis en liste blanche, False sinon.
        :rtype: boolean
        """
        @timeout_decorator(3600)
        def graphic_accept():
            """
            Retourne True si c'est ok.
            Retourne False si c'est pas bon.
            Retourne Timeout si c'est indecis.
            """
            import raisin.application.hmi.dialog as dialog
            question =  "'%s' shouaite se connecter.\n" % client_id["username"] \
                        + "Il travail sur l'os '%s'.\n" % client_id["os_version"] \
                        + "Sur le PC '%s'.\n" % client_id["hostname"] \
                        + "Il est localise en '%s' a '%s'.\n" % (client_id["country"], client_id["city"]) \
                        + "Il pretend avoir l'adresse mac '%s'.\n" % client_id["mac"]
            try:
                return dialog.question_binaire(question, default=None, existing_window=None)
            except KeyboardInterrupt:
                raise TimeoutError

        with Printer("Ask to user for accept a new client...") as p:

            # On s'assure que l'utilisateur n'ai pas encore donne son avis.
            is_a = self.is_accepted(client_id["mac"])
            if is_a == True:
                p.show("The client is already accepted.")
                return True
            if is_a == False:
                p.show("This client is already baned.")
                return False
            
            # Si on peut lui demander graphiquement de suite, on le fait.
            import raisin.application.hmi as hmi
            if hmi.tkinter:
                try:
                    rep = graphic_accept() # On lui laisse 1 heure pour repondre.
                except TimeoutError:
                    rep = False
            else:
                rep = None
            
            # On enregistre ensuite le client dans les bases de donnees.
            if rep:
                with open(os.path.join(os.path.expanduser("~"),
                        ".raisin", "whitelisted.txt"), "a") as f:
                    f.write("%s %s\n" % (
                        client_id["mac"],
                        time.strftime("%Y-%m-%dT%H:%M:%S")))
                p.show("The client %s is now accepted." % client_id["mac"])
                return True
            else:
                with open(os.path.join(os.path.expanduser("~"),
                        ".raisin", "blacklisted.txt"), "a") as f:
                    f.write("%s %s %s\n" % (
                        client_id["mac"],
                        time.strftime("%Y-%m-%dT%H:%M:%S"),
                        "wait" if rep == None else "definitive"))
                if rep == False:
                    p.show("The client %s is now definitively baned." \
                        % client_id["mac"])
                    return False

            # Enregistrement de se client dans la liste d'attente.
            with open(os.path.join(os.path.expanduser("~"),
                    ".raisin", "waitlisted.txt"), "a") as f:
                f.write("%s %s\n" % (
                    time.strftime("%Y-%m-%dT%H:%M:%S"),
                    dumps(client_id)))

            # Envoi d'un mail.
            try:
                with open(os.path.join(os.path.expanduser("~"),
                        ".raisin", "last_mail.txt"), "r") as f:
                    last_mail = time.mktime(
                        time.strptime(f.read(), "%Y-%m-%dT%H:%M:%S\n"))
            except FileNotFoundError:
                last_mail = 0
            if time.time() - last_mail > 24*3600: # Si cela fait plus d'un jour qu'on a pas envoye de mail.
                with open(os.path.join(os.path.expanduser("~"),
                        ".raisin", "waitlisted.txt"), "r") as f:
                    waitings = [(
                            time.mktime(time.strptime(t, "%Y-%m-%dT%H:%M:%S")),
                            loads(c))
                        for t, c in [l.split() for l in f.readlines()]] # Les clients en attente.
                clients = [c for t, c in waitings[::-1] if t > last_mail] # Les nouveaux clients.
                message = "Des nouveaux clients attendent que vous les acceptiez.\n" \
                        + "Ce mail est envoye depuis:\n\t%s\n\n" % "\n\t".join(
                            ("%s: %s" % p for p in dict(identity).items())) \
                        + "Pour accepter un client tapez:\n" \
                        + "\t'%s -m raisin client accept client_attribute'\n" % sys.executable \
                        + "Pour refuser un client tapez:\n" \
                        + "\t'%s -m raisin client exile client_attribute'\n" % sys.executable \
                        + "Pour voir tous les clients en attente:\n" \
                        + "\t'%s -m raisin client status'\n" % sys.executable \
                        + "'client_attribute' est n'importe quel champ qui permet d'identifier un client unique.\n" \
                        + "Voici la liste des.du nouveau.x client.s en attente:\n\n" \
                        + "%s" % "\n\n".join(
                            "\n".join("%s: %s" % p for p in c.items())
                            for c in clients)
                import raisin.communication.mail as mail
                mail.send(settings["account"]["email"], "raisin: client waiting", message)
                with open(os.path.join(os.path.expanduser("~"),
                        ".raisin", "last_mail.txt"), "w") as f:
                    f.write(time.strftime("%Y-%m-%dT%H:%M:%S\n"))
                del mail
            return False

    def close(self):
        """
        Permet de fermer proprement les sockets.
        """
        with Printer("Shutdown the server..."):
            for client in self.clients.values():
                client["socket"].shutdown(socket.SHUT_RDWR) # Empeche imediatement les connections.
                client["socket"].close() # Demande au socket de mourir.
            if hasattr(self, "tcp_socket"): # Si le constructeur n'a pas echoue.
                self.tcp_socket.close()

    def handle(self, client_socket, key):
        """
        |====================================|
        | Satisfait les besoins d'un client. |
        |====================================|

        Cette methode doit etre lancee dans un thread.
        Sinon elle bloquerait tout et seul le premier
        client serait servis.
        Cette methode est bloquante.

        entree
        ------
        :param client_socket: Socket tcp du client que l'on ecoute.
        :type client_socket: socket.socket
        :param key: Clef publique du client.
        :type key: str

        sortie
        ------
        :return: True si la discution s'est bien passe. False si il y a un quoic.
        :rtype: boolean
        """
        while True:
            # Traitement des messages.
            with Printer("Waiting for a reponse...") as p:
                try:
                    question = routing.receive(client_socket)
                except NotCompliantError:
                    p.show("Not complient request.")
                    del self.clients[key]
                    return False
                except OSError:
                    p.show("Erreur avec le socket TCP.")
                    try:
                        client_socket.shutdown(socket.SHUT_RDWR)
                        client_socket.close()
                    except OSError:
                        pass
                    del self.clients[key]
                    return False
                else:
                    answer = request.answering(question)
                    if answer["type"] == "error":
                        routing.send_error(client_socket, answer["message"])
                        p.show(answer["message"])
                        del self.clients[key]
                        return False
                    routing.send_object(client_socket, answer)

    def select(self):
        """
        |===============================|
        | Acceuil les nouveaux clients. |
        |===============================|

        Si le client est accepte, il est ajoute dans les clients connectes
        et un nouveau thread est cree rien que pour lui.
        Comme c'est ici que les clients debarquent tout d'abord, on est extremement mefiant
        envers eux pour une question de securitee. Plein de tests dont fait de
        facon a s'assurer qu'ils soit bien en regles.
        """
        while True:
            client_socket, info = self.tcp_socket.accept() # On ne fait pas directement
            ip_client = info[0]                    # client_socket, (ip_client, port_client)
            port_client = info[1]                  # car le deuxieme tuple contient parfois 4 elements.
            with Printer("Un client d'ip %s se connecte via le port %d..." \
                    % (ip_client, port_client)) as p:
                try:
                    # On s'assure qu'il n'y ai pas trop de monde.
                    if len(self.clients) >= settings["server"]["listen"]:
                        routing.send_error(client_socket,
                            "There are already too many connections.")
                        raise ConnectionRefusedError(
                            "Customer expelled because there are already "
                            "too many connections.")
                    
                    with Printer("We make some tests about the customer..."):
                        
                        # Recuperation adresse mac.
                        try:
                            mac = routing.receive(client_socket, timeout=30)
                        except socket.timeout:
                            routing.send_error(client_socket,
                                "You are too slow to send your mac address.")
                            raise TimeoutError("Customer expelled because "
                                "he is too slow to send his mac address.")
                        except NotCompliantError:
                            raise ThreatenError(
                                "Customer expelled because he is threatening.") # Le message d'erreur est deja envoye depuis 'receive'
                        if checks.check_info(mac) or "mac" not in mac:
                            routing.send_error(client_socket, "He did not give his mac address.")
                            raise ThreatenError("Customer expelled because "
                                "he did not give his mac address.")
                        
                        # Recuperation de la clef publique.
                        if 1: # Il faudrait deja regarder si on ne connait pas deja la clef publique a partir de mac.
                            public_key = request.ask_public_key(client_socket)
                            if not public_key:
                                raise ThreatenError("Customer expelled "
                                    "because we don't have his public key.") # Le message d'erreur est deja envoye.

                        # On s'assure qu'il n'usurpe pas l'identitee d'un autre.
                        if settings["server"]["force_authentication"]:
                            if not request.ask_challenge(client_socket, public_key):
                                raise ThreatenError(
                                    "Customer expelled because he's a crook.") # Le message d'erreur est deja envoye.
                        
                        # On s'assure que ce client est le bienvenu.
                        autorization = self.is_accepted(mac["mac"])
                        if autorization == None: # Si il faut demander l'avis de l'utilisateur.
                            client_id = request.ask_identity(client_socket)
                            if not client_id:
                                raise ThreatenError("Customer expelled because "
                                    "we don't have his identity.") # Le message d'erreur est deja envoye.
                            threading.Thread(
                                target=self.accept,
                                args=(client_id,)).start() # On pose la question a l'utilisateur
                            routing.send_error(client_socket,
                                "You have to wait for user approval.")
                            raise ThreatenError("Customer expelled because he "
                                "have to wait for user approval.") # Mais on attend pas qu'il reponde.
                        elif autorization == False: # Si il faut le virer.
                            routing.send_error(client_socket, "You are blacklisted.")
                            raise ThreatenError("Customer expelled because he "
                                "is blacklisted.")
                        
                        # On s'assure que le client n'est pas deja connecte.
                        if public_key in self.clients:
                            routing.send_error(client_socket,
                                "you are already connected.")
                            raise ThreatenError("Customer expelled because he "
                                "is already connected.")

                    # On lui shouaite la bienvenue.
                    request.send_welcome(client_socket)

                    self.clients[public_key] = {
                        "mac": mac["mac"],
                        "port": port_client,
                        "ip": ip_client,
                        "socket": client_socket,
                        "thread": multiprocessing.Process(
                            target=self.handle,
                            args=(client_socket, public_key))}
                    self.clients[public_key]["thread"].start()
                except Exception: # Si il y a un probleme entre temps,
                    continue # on ne fait pas planter le serveur pour ca.

    def start(self):
        """
        |====================|
        | Demare le serveur. |
        |====================|
        """
        return self.select()

    def __del__(self):
        self.close()


def main():
    """
    Lance le serveur.
    """
    s = Server()
    s.start()

if __name__ == "__main__":
    main()

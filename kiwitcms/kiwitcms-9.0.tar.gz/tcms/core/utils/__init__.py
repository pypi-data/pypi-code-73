# -*- coding: utf-8 -*-
#  pylint: disable=too-few-public-methods

import sys


def string_to_list(strs, spliter=","):
    """Convert the string to list"""
    if isinstance(strs, list):
        str_list = (str(item).strip() for item in strs)
    elif isinstance(strs, str) and strs.find(spliter):
        str_list = (str(item).strip() for item in strs.split(spliter))
    else:
        str_list = (strs,)

    lst = []
    for string in str_list:
        if string:
            lst.append(string)
    return lst


def form_errors_to_list(form):
    """
    Convert errors of form to list
    Use for Ajax.Request response
    """
    errors = []
    for key, value in form.errors.items():
        errors.append((key, value[0]))
    return errors


def request_host_link(request, domain_name=None):
    protocol = "https://"
    if "runserver" in sys.argv:
        protocol = "http://"

    if request:
        if not domain_name:
            domain_name = request.get_host()
        # default to https if in production and we don't know
        protocol = "https://"
        if not request.is_secure():
            protocol = "http://"

    return protocol + domain_name

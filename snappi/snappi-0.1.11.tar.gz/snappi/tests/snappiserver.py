from flask import Flask, request, Response
import threading
import json

app = Flask(__name__)
CONFIG = None


@app.route('/config', methods=['POST'])
def set_config():
    global CONFIG
    import snappi
    config = snappi.api.Api().config()
    config.deserialize(request.data.decode('utf-8'))
    test = config.options.port_options.location_preemption
    if test is not None and isinstance(test, bool) is False:
        return Response(status=590,
                        response=json.dumps({'detail': 'invalid data type'}),
                        headers={'Content-Type': 'application/json'})
    else:
        CONFIG = config
        return Response(status=200)


@app.route('/config', methods=['GET'])
def get_config():
    global CONFIG
    return Response(CONFIG.serialize(),
                    mimetype='application/json',
                    status=200)


@app.route('/control/transmit', methods=['POST'])
def set_transmit_state():
    global CONFIG
    return Response(status=200)


@app.route('/results/port', methods=['POST'])
def get_port_metrics():
    import snappi
    api = snappi.api.Api()
    port_metrics_request = api.port_metrics_request()
    port_metrics_request.deserialize(request.data.decode('utf-8'))
    port_metrics = api.port_metrics()
    port_metrics.metric().metric()
    return Response(port_metrics.serialize(),
                    mimetype='application/json',
                    status=200)


@app.route('/results/flow', methods=['POST'])
def get_flow_metrics():
    import snappi
    api = snappi.api.Api()
    flow_metrics_request = api.flow_metrics_request()
    flow_metrics_request.deserialize(request.data.decode('utf-8'))
    flow_metrics = api.flow_metrics()
    flow_metrics.metric().metric()
    return Response(flow_metrics.serialize(),
                    mimetype='application/json',
                    status=200)


@app.after_request
def after_request(resp):
    print(request.method, request.url, ' -> ', resp.status)
    return resp


def web_server():
    app.run(port=80, debug=True, use_reloader=False)


class SnappiServer(object):
    def __init__(self):
        self._CONFIG = None

    def start(self):
        self._web_server_thread = threading.Thread(target=web_server)
        self._web_server_thread.setDaemon(True)
        self._web_server_thread.start()
        return self

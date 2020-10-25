# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()    # debug
import begin
from autobahn.twisted.wamp import Application
from twisted.internet import reactor

"""
    Send a Websocket message to JavaScript page on web server.
:param host:    Hostname or IP adresse. Default=localhost
:param port:    Server port. Default=8080
:param message: Message to send. Default='Hello world!'
:return:        Websocket request to web server.
"""


# Start client on command line if main.
@begin.start
def ws_sender_run(
        host='127.0.0.1',
        channel='argonautes_channel',
        message='Hello world!',
        separator=',',
):
    """
        Send a message to a JavaScript Crossbar client via Websocket.
        Default message is 'Hello World!'
    """
    data = message.split(separator)
    print(f"data: {data}")

    # Wamp Application instance
    app = Application()

    @app.signal('onjoined')
    def called_on_joined():
        json_data = {
            'topic': data,
        }
        # Send to Crossbar/autobahn channel
        app.session.publish(channel, json_data)
        print(f"ws_sender: sending {json_data}")
        app.session.leave()

    @app.signal('onleave')
    def called_on_onleave():
        app.session.disconnect()

    @app.signal('ondisconnect')
    def called_on_ondisconnect():
        reactor.stop()

    # Environment detection: PRODUCTION/DEV
    if host == "open1024.fr":
        app.run(url='wss://{}/ws'.format(host), start_reactor=False)
    else:
        app.run(url='ws://{}:8080/ws'.format(host), start_reactor=True)

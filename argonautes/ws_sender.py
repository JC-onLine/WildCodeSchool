# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()    # debug
import begin
from autobahn.twisted.wamp import Application
from twisted.internet import reactor

"""
    Send a Websocket message to JavaScript page client side.
:param host:        Hostname or IP adresse. Default=localhost
:param channel:     Channel id to JS explatation
:param message:     Message to send. Default='Hello world!'
:param separator:   Can split message to many <div>
:loop:              Use to stop 'reactor' in command line mode.
:log:               Use to display log.  
:return:            Websocket request to web client.
"""


# Start client on command line if main.
@begin.start
def ws_sender_run(
        host='127.0.0.1',
        channel='argonautes_channel',
        message='Hello world!',
        separator='',
        loop=False,
        log=False
):
    """
        Send a message to a JavaScript Crossbar client via Websocket.
    """
    if log:
        print(f"ws_sender: message: {message}")
        print(f"ws_sender: receiv data: {message}")
    if separator != '':
        data = message.split(separator)
    else:
        data = message

    # Wamp Application instance
    app = Application()

    @app.signal('onjoined')
    def called_on_joined():
        if log:
            print(f"ws_sender: onjoined: {data}")
        json_data = {
            'topic': data,
        }
        # Send to Crossbar/autobahn channel
        app.session.publish(channel, json_data)
        if log:
            print(f"ws_sender: sending data: {json_data}")
        if not loop:
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
        app.run(url='ws://{}:8080/ws'.format(host), start_reactor=False)

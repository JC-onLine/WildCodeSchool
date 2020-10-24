# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()    # debug
import os
import django
# Django integration for DB access
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "argonautes.settings")
# django.setup()
from autobahn.twisted.wamp import Application, ApplicationRunner
from twisted.internet.defer import inlineCallbacks
from twisted.internet import reactor


# Environment detection: PRODUCTION/DEV
ENV = os.environ.get('ENV')
if ENV == 'PRODUCTION':
    SERVER = 'open1024.fr'
else:
    SERVER = '127.0.0.1'          # localhost
print('=========================================')
print('ENV:', ENV)
print('SERVER:', SERVER)
print('=========================================')

app = Application()
# app = ApplicationRunner(url='ws://{}:8080/ws'.format(SERVER), realm='realm1')

@app.signal('onjoined')
# @inlineCallbacks
def called_on_joined():
    # ==== Create & Use autobahn 'client_mode' channel
    # ==== to auto refresh web page on the 1st start app
    json_data = {'mode': 'CLEAR'}
    app.session.publish('client_mode', json_data)
    print('called_on_joined: publish', json_data)
    app.session.leave()
    # app.session.disconnect()
    # print("is_connected", app.session.is_connected())
    # print("is_attached", app.session.is_attached())
    print('called_on_joined: END')
    # import pdb; pdb.set_trace()    # debug

@app.signal('onleave')
# @inlineCallbacks
def called_on_onleave():
    app.session.disconnect()
    # print("is_connected", app.session.is_connected())
    # print("is_attached", app.session.is_attached())
    # print('called_on_onleave: END')

@app.signal('ondisconnect')
# @inlineCallbacks
def called_on_ondisconnect():
    # print("is_connected", app.session.is_connected())
    # print("is_attached", app.session.is_attached())
    reactor.stop()
    # print('called_on_ondisconnect: END')


# Start client.
if __name__ == '__main__':
    """Main: Go running app! """
    # Environment detection: PRODUCTION/DEV
    if SERVER == "open1024.fr":
        app.run(url='wss://{}/ws'.format(SERVER), start_reactor=False)
    else:
        app.run(url='ws://{}:8080/ws'.format(SERVER), start_reactor=True)

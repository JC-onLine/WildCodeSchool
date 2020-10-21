# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()    # debug
import os
from autobahn.twisted.wamp import Application
from twisted.internet import reactor

# Environment detection: PRODUCTION/DEV for IP config
ENV = os.environ.get('ENV')
if ENV == 'PRODUCTION':
    SERVER = 'open1024.fr'
else:
    SERVER = '127.0.0.1'          # localhost
app = Application()


@app.signal('onjoined')
# @inlineCallbacks
def called_on_joined():
    # ==== Create & Use autobahn 'client_mode' channel
    # ==== to auto refresh web page when database changed
    json_data = {
        # 'mode': 'CLEAR',
        'team_list': ["Equipier1", "Equipier2", "Equipier3"]
    }
    app.session.publish('argonautes_channel', json_data)
    print('called_on_joined: publish', json_data)
    app.session.leave()


@app.signal('onleave')
def called_on_onleave():
    app.session.disconnect()


@app.signal('ondisconnect')
def called_on_ondisconnect():
    reactor.stop()



# Start client if main.
if __name__ == '__main__':
    """Main: Go running app! """
    # Environment detection: PRODUCTION/DEV
    if SERVER == "open1024.fr":
        app.run(url='wss://{}/ws'.format(SERVER), start_reactor=False)
    else:
        app.run(url='ws://{}:8080/ws'.format(SERVER), start_reactor=True)

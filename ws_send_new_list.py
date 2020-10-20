# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()    # debug
import os
import django
# Django integration for DB access
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_cfg.settings")
django.setup()
from autobahn.twisted.wamp import Application
from twisted.internet import reactor
from argonautes.models import Equipage
from django.forms.models import model_to_dict


# Extract team members from database and convert to json
team_list = Equipage.objects.all()
# team_list_json = model_to_dict(team_list)


# Environment detection: PRODUCTION/DEV for IP config
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

@app.signal('onjoined')
# @inlineCallbacks
def called_on_joined():
    # ==== Create & Use autobahn 'client_mode' channel
    # ==== to auto refresh web page when database changed
    json_data = {
        # 'mode': 'CLEAR',
        'team_list': ["Equipier1", "Equipier2", "Equipier3"]
    }
    app.session.publish('client_mode', json_data)
    print('called_on_joined: publish', json_data)
    app.session.leave()

@app.signal('onleave')
def called_on_onleave():
    app.session.disconnect()

@app.signal('ondisconnect')
def called_on_ondisconnect():
    reactor.stop()


# Start client.
if __name__ == '__main__':
    """Main: Go running app! """
    # Environment detection: PRODUCTION/DEV
    if SERVER == "open1024.fr":
        app.run(url='wss://{}/ws'.format(SERVER), start_reactor=False)
    else:
        app.run(url='ws://{}:8080/ws'.format(SERVER), start_reactor=True)

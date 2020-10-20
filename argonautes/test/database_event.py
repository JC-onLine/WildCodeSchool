# use to update ws client when database change.
import requests


requests.post("http://127.0.0.1:8080/notify",
              json={
                  'topic': 'vatconfig.192.168.1.230',
                  'args': [{'name': 'Equipier1'}]
              })

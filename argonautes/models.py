from django.db import models
# use to update ws client when database change.
import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from .ws_sender import ws_sender_run


class Equipage(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return f"{self.name}"


@receiver(post_save, sender=Equipage, dispatch_uid="server_post_save")
def notify_server_config_changed(sender, instance, **kwargs):
    """ Notifies a communication task that database has been changed.

        This function is executed when we save a Equipage model,
        and it makes a POST request on the WAMP-HTTP bridge (crossbar),
        allowing us to make a WAMP publication from Django.
    """
    # Extract team members from database and convert to json
    print("==== Database Event! ====")

    # team_list = Equipage.objects.all()
    # print(f"team_list: {team_list}")
    # print(f"model_to_dict: {model_to_dict(team_list)}")
    # ws_sender_run(message="Argonaute1, Argonaute2, Argonaute")
    #
    # print("notify_server_config_changed!")
    # requests.post("http://127.0.0.1:8080/notify",
    #               json={
    #                   'topic': 'vatconfig.192.168.1.230',
    #                   'args': [model_to_dict(instance)]
    #               })

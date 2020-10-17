from django.db import models
import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict


class Equipage(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return f"{self.name}"


@receiver(post_save, sender=Equipage, dispatch_uid="server_post_save")
def notify_server_config_changed(sender, instance, **kwargs):
    """ Notifies a client that database has changed.
    """
    requests.post("http://127.0.0.1:8080/notify",
                  json={
                      'topic': 'plcconfig.' + instance.plc_ip,
                      'args': [model_to_dict(instance)]
                  })

from django.db import models
# use to update ws client when database change.
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tools import dispatch_members
from .ws_sender import ws_sender_run


class Equipage(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return f"{self.name}"


# @receiver(post_save, sender=Equipage, dispatch_uid="server_post_save")
def notify_client_database_changed(sender, instance, **kwargs):
    """ Notifies a communication task that database has been changed.

        This function is executed when we save a Equipage model,
        and it makes a POST request on the WAMP-HTTP bridge (crossbar),
        allowing us to make a WAMP publication from Django.
    """
    print("==== Database Event! + ws_sender_run() ====")
    team_queryset = Equipage.objects.values_list('name', flat=True).order_by('pk')
    team_list = list(team_queryset)
    dispatched = dispatch_members(team_list)
    print(f"== Database: {dispatched}")
    ws_sender_run(
        host='bdf25fab89e9.ngrok.io',
        message=dispatched,
        loop=True,
        log=True)


post_save.connect(notify_client_database_changed, sender=Equipage)
from django.db import models
# use to update ws client when database change.
from django.db.models.signals import post_save
from .tools import dispatch_members_3_columns
from .ws_sender import ws_sender_run
from django.conf import settings


class Equipage(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return f"{self.name}"


class AppliSettings(models.Model):
    members_maxi = models.IntegerField(unique=True, default=20)
    columns_number = models.IntegerField(unique=True, default=2)


# @receiver(post_save, sender=Equipage, dispatch_uid="server_post_save")
def notify_client_database_changed(sender, instance, **kwargs):
    """ Notifies a communication task that database has been changed.
        This function is executed when we save a Equipage model,
        and it makes a POST request on the WAMP-HTTP bridge (crossbar),
        allowing us to make a WAMP publication from Django.
    """
    log = False

    if log: print("==== Database Event! + ws_sender_run() ====")
    team_queryset = \
        Equipage.objects.values_list('name', flat=True).order_by('pk')
    team_list = list(team_queryset)
    team_dispatched = dispatch_members_3_columns(team_list)
    if log: print(f"== Database: {team_dispatched}")
    ws_sender_run(
        host=settings.DJANGO_URL,
        message=team_dispatched,
        loop=True,
        log=False
    )


post_save.connect(notify_client_database_changed, sender=Equipage)

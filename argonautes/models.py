from django.db import models
# use to update ws client when database change.
from django.db.models.signals import post_save
from .tools import columns_spliter
from .ws_sender import ws_sender_run
from django.conf import settings


class Equipage(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return f"{self.name}"


class AppliSettings(models.Model):

    profile = models.IntegerField(default=1, unique=True)
    members_maxi = models.IntegerField(default=50, unique=True)
    columns_number = models.IntegerField(default=3, unique=True)


# @receiver(post_save, sender=Equipage, dispatch_uid="server_post_save")
def notify_client_database_changed(sender, instance, **kwargs):
    """ Notifies a communication task that database has been changed.
        This function is executed when we save a Equipage model,
        and it makes a POST request on the WAMP-HTTP bridge (crossbar),
        allowing us to make a WAMP publication from Django.
    """
    # Get/Set applications settings
    # app_settings: get members_maxi & columns_number
    current_app_settings = AppliSettings.objects.filter(profile=1).get()
    app_settings_dict = {
        'members_maxi': current_app_settings.members_maxi,
        'columns_number': current_app_settings.columns_number,
        'log': False,
    }
    log = True
    if log:
        print("==== Database Event! + ws_sender_run() ====")
    members_queryset = \
        Equipage.objects.values_list('name', flat=True).order_by('pk')
    members_list = list(members_queryset)
    team_dispatched = \
        columns_spliter(members_list, app_settings_dict['columns_number'])
    if log:
        print(f"== Database: {team_dispatched}")
    ws_sender_run(
        host=settings.DJANGO_URL,
        message=team_dispatched,
        loop=True,
        log=False
    )


post_save.connect(notify_client_database_changed, sender=Equipage)

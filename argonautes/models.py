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

    members_maxi = models.IntegerField(unique=True)
    columns_number = models.IntegerField(unique=True)


# @receiver(post_save, sender=Equipage, dispatch_uid="server_post_save")
def notify_client_database_changed(sender, instance, **kwargs):
    """ Notifies a communication task that database has been changed.
        This function is executed when we save a Equipage model,
        and it makes a POST request on the WAMP-HTTP bridge (crossbar),
        allowing us to make a WAMP publication from Django.
    """
    # Get/Set applications settings
    # - app_settings: get members_maxi & columns_number
    # - created: True if created else False
    # app_settings, created = AppliSettings.objects.\
    #     get_or_create(members_maxi=40, columns_number=3)
    app_settings_dict = {
        # 'members_maxi': app_settings.members_maxi,
        # 'columns_number': app_settings.columns_number,
        'members_maxi': 40,
        'columns_number': 5,
        'log': False,
    }

    log = False

    if log: print("==== Database Event! + ws_sender_run() ====")
    members_queryset = \
        Equipage.objects.values_list('name', flat=True).order_by('pk')
    members_list = list(members_queryset)
    team_dispatched = \
        columns_spliter(members_list, app_settings_dict['columns_number'])
    if log: print(f"== Database: {team_dispatched}")
    ws_sender_run(
        host=settings.DJANGO_URL,
        message=team_dispatched,
        loop=True,
        log=False
    )


post_save.connect(notify_client_database_changed, sender=Equipage)

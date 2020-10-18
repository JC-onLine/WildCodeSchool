from django.shortcuts import render
from .form import EquipageForm
from .models import Equipage
# use to update ws client when database change.
import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict


def main_page(request):
    """
    Display EquipageForm and save data
    :param request:
    :return:
    """
    form = EquipageForm(request.POST)
    equipage = Equipage.objects.all()
    eq_count = Equipage.objects.count() + 1
    # catch POST form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            context = {
                'equipage': equipage,
                'eq_count': eq_count,
                'form': form
            }
            return render(request, 'argonautes/index.html', context)
    else:
        form = EquipageForm()
    # display form
    context = {
        'equipage': equipage,
        'eq_count': eq_count,
        'form': form
    }
    return render(request, 'argonautes/index.html', context)


@receiver(post_save, sender=Equipage, dispatch_uid="server_post_save")
def notify_server_config_changed(sender, instance, **kwargs):
    """ Notifies a communication task that database has changed.

        This function is executed when we save a Equipage model,
        and it makes a POST request on the WAMP-HTTP bridge (crossbar),
        allowing us to make a WAMP publication from Django.
    """
    requests.post("http://127.0.0.1:8080/notify",
                  json={
                      'topic': 'vatconfig.192.168.1.230',
                      'args': [model_to_dict(instance)]
                  })

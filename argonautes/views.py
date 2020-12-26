from django.shortcuts import render
from .form import EquipageForm
from .models import Equipage
from .tools import dispatch_members_3_columns
from django.conf import settings
# Used for ajasx POST
from django.http import JsonResponse
from django.core import serializers


def main_page(request):
    """
        Display EquipageForm and save data
    :param request: POST request with form
    :return:        Display form for the 1st time
                    Save team memeber name in database
    """
    team_queryset = Equipage.objects.values_list('name', flat=True).order_by('pk')
    team_list = list(team_queryset)
    # dispach members in 3 lists
    team_dispatched = dispatch_members_3_columns(team_list)
    print(f"team_dispatched={team_dispatched}")
    # json compose for JavaScript
    team_list_on_first_open = {
        'topic': team_dispatched,
    }
    # display form
    context = {
        'django_url': settings.DJANGO_URL,
        'team_list_on_first_open': team_list_on_first_open,
        'column1': team_dispatched['column1'],
        'column2': team_dispatched['column2'],
        'column3': team_dispatched['column3'],
    }
    return render(request, 'argonautes/index.html', context)


def add_argonaute(request):
    """
        Add member name from AJAX form in database.
        Called by /wcs/add url
    :param request: POST and AJAX data.
    :return:        Save AJAX data in database.
    """
    # request control: Must be POST and AJAX
    if request.method == "POST" and request.is_ajax :
        # read the form data
        form = EquipageForm(request.POST)
        # check valid data and save
        if form.is_valid():
            current_data = form.save()
            # convert data to json for js
            current_data_json = serializers.serialize('json', [ current_data, ])
            # send data to client.
            return JsonResponse({"instance": current_data_json}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    # some error occured
    return JsonResponse({"error": ""}, status=400)


def reset_argonautes(request):
    """
        Delete members in database.
        Called by /wcs/reset_argonautes url
    :param request: None
    :return:        Delete data in database.
    """
    database_all = Equipage.objects.all()
    database_all.delete()
    return render(request, 'argonautes/index.html', {})
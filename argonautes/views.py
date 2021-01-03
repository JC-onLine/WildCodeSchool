from django.shortcuts import render
from .form import EquipageForm
from .models import Equipage, AppliSettings
from .tools import dispatch_members_3_columns
from django.conf import settings
# Used for ajasx POST
from django.http import JsonResponse
from django.core import serializers


def main_page(request):
    """
        Display EquipageForm and save data
    :param request: POST request with form
    :return:        Display form on page boot
                    Save team memeber name in database
    """
    # Get applications settings
    # - app_settings: get members_maxi & columns_number
    # - created: True if created else False
    app_settings, created = AppliSettings.objects.\
        get_or_create(members_maxi=40, columns_number=3)
    app_settings_dict = {
        'members_maxi': app_settings.members_maxi,
        'columns_number': app_settings.columns_number
    }
    print(f"Get applications settings app_settings: {app_settings.members_maxi} and {app_settings.columns_number}")
    print(f"Get applications settings app_settings_dict: {app_settings_dict}")
    print(f"Get applications settings created: {created}")
    # query setup
    team_queryset = \
        Equipage.objects.values_list('name', flat=True).order_by('pk')
    team_list = list(team_queryset)
    # dispach member list in 3 columns
    page_boot_db = dispatch_members_3_columns(team_list)
    # json compose for JavaScript
    # page_boot_db = {
    #     'topic': team_dispatched,
    # }
    # display form
    context = {
        'DJANGO_URL': settings.DJANGO_URL,
        'page_boot_db': page_boot_db,
        'app_settings': app_settings_dict,
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
    if request.method == "POST" and request.is_ajax:
        # read the form data
        form = EquipageForm(request.POST)
        # check valid data and save
        if form.is_valid():
            current_data = form.save()
            # convert data to json for js
            current_data_json = serializers.serialize('json', [current_data, ])
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

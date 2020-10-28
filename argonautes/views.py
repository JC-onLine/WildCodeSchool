from django.shortcuts import render
from .form import EquipageForm
from .models import Equipage
from .tools import dispatch_members
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
    form = EquipageForm(request.POST)
    form = EquipageForm()
    equipage = Equipage.objects.all().order_by('pk')
    eq_count = Equipage.objects.count() + 1
    # dispach members in 3 lists
    dispatched = dispatch_members(equipage)
    # display form
    context = {
        # 'equipage': equipage,
        'column1': dispatched['column1'],
        'column2': dispatched['column2'],
        'column3': dispatched['column3'],
    }
    return render(request, 'argonautes/index.html', context)
    # return redirect('argonautes/index.html')


def add_argonaute(request):
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
from django.shortcuts import render
from .form import EquipageForm
from .models import Equipage
# Used for ajasx POST
from django.http import JsonResponse
from django.core import serializers


def main_page(request):
    """
    Display EquipageForm and save data
    :param request:
    :return:
    """
    form = EquipageForm(request.POST)
    equipage = Equipage.objects.all().order_by('pk')
    eq_count = Equipage.objects.count() + 1
    # catch POST form
    if request.method == 'POST':
        if form.is_valid():
            # form.save()
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


def add_agonaute(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = EquipageForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
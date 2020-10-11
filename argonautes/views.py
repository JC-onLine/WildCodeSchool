from django.shortcuts import render
from .form import EquipageForm
from .models import Equipage

def main_page(request):
    form = EquipageForm(request.POST)
    equipage = Equipage.objects.all()
    # catch POST form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            context = {
                'equipage': equipage,
                'form': form
            }
            return render(request, 'argonautes/index.html', context)
    # display form
    context = {
        'equipage': equipage,
        'form': form
    }
    return render(request, 'argonautes/index.html', context)

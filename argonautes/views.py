from django.shortcuts import render
from .form import EquipageForm
from .models import Equipage

def main_page(request):
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

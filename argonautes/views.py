from django.shortcuts import render


def main_page(request):
    context = {}
    return render(request, 'argonautes/index.html', context)
from django.shortcuts import render

def home(request):
    """
    Renders the interactive Nikah invitation page (Bride / Pulikkalakath side).
    """
    return render(request, 'index.html')

def dinu(request):
    """
    Renders the interactive Nikah invitation page (Groom / Kollan Thodi side).
    """
    return render(request, 'dinu.html')



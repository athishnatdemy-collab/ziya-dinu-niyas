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

def reception(request):
    """
    Renders the interactive Reception invitation page (Ziya & Dinu) - 4:00 PM to 7:00 PM slot.
    """
    return render(request, 'reception.html')

def reception_7_10(request):
    """
    Renders the interactive Reception invitation page (Ziya & Dinu) - 7:00 PM to 10:00 PM slot.
    """
    return render(request, 'reception_7_10.html')

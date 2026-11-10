from django.shortcuts import render

def home(request):
    """
    Renders the interactive Nikah invitation page.
    """
    return render(request, 'index.html')

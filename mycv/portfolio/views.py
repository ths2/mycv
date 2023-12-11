from django.shortcuts import render

# Create your views here.
    

def wellcome_page(request):
    return render(request, 'index.html')
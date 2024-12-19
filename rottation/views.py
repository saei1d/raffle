from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request,'Card Rotation HTML.html')





def test(request):
    return render(request,'test.html')
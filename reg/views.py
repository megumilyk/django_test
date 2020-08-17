from django.shortcuts import render


# Create your views here.
def reg_view(request):

    if request.method == 'GET':
        return render(request, 'reg.html')

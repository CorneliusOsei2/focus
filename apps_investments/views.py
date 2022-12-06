from django.shortcuts import render

# Create your views here.
def invest(request):
    
    if request.method == 'GET':
        return render(request, 'invest.html')
    elif request.method == 'POST':
        pass
    
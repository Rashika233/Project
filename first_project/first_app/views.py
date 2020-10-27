from django.shortcuts import render, redirect
from . import forms
from .models import Register
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer

# Create your views here.
from django.http import HttpResponse, JsonResponse
def home(request):
    return render(request, 'index.html')

#def about(request):
 #   return HttpResponse('About Page')

def create(request):
    if request.method=="POST":
        form = forms.Registerform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('success')
            except:
                print('Error')
    else:
        form=forms.Registerform()
        return render(request, 'register.html', {'form': form})



def success(request):
    return render(request, 'success.html')


def random(request):
    data={1: {'name':'Rashika', 'email': 'r@gmail.com'}, 2:{'name':'Riyaz', 'email': 'ri@gmail.com'}}
    return JsonResponse(data)

class Registerlist(APIView):
    def get(self, request):
        values=Register.objects.all()
        serializer=RegisterSerializer(values, many=True)
        return Response(serializer.data)
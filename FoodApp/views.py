from django.shortcuts import render

# Create your views here.
def food(request):
    return render(request,'food.html')
    
def fruit(request):
    return render(request,'fruits.html')
    
def calorie(request):
    return render(request,'calorie.html')

def vegetables(request):
    return render(request,'vegetables.html')

def nuts(request):
    return render(request,'nuts.html')

def dairy(request):
    return render(request,'dairy.html')
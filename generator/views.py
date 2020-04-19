from django.shortcuts import render
import random
import string
# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'dfrt44r4f'})

def password(request):

    thepassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 3))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('numbers'):
        characters.extend('1234567890')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

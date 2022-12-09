from django.shortcuts import render,redirect
import random

def index(request):
    return render(request,'index.html')

def test(request):
    request.session['random_number'] = random.randint(1,5)
    request.session['number'] = request.POST['inputNumber']

    if int(request.session['number']) == int(request.session['random_number']):
        return redirect('/win_Number')
    elif int(request.session['number']) > int(request.session['random_number']) :
        request.session['hint'] = "Too Big"
        return render(request,'gameResult.html')
    elif int(request.session['number']) < int(request.session['random_number']):
        request.session['hint'] = "Too small"
        return render(request,'gameResult.html')
    elif int(request.session['number']) > int(request.session['random_number'])+1:
        request.session['hint'] = "You are so closely "
        return render(request,'gameResult.html')
    

def win(request):
    return render(request,'win.html')
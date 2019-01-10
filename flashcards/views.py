from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required(login_url='/accounts/login/')
def index(request):
    cards = Flashcard.objects.all() #retrieves all the saved cards to diplay on the site
    date = dt.date.today()

    return render(request, 'index.html' , {"date":date, "cards":cards})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(username=request.user).first()
    
    return render(request,'profile.html',{'profile':profile})

@login_required(login_url='/accounts/login/')
def update_card(request):
    current_user=request.user
    cards = Flashcards.objects.filter(username=request.user).first()

    #Allows a user to update the flash cards
    if request.method == 'POST':
        form = CardForm(request.POST,instance=card,files=request.FILES)

        #Saves the data from the form into the database
        if form.is_valid():
            card = form.save(commit=False)
            card.username = current_user
            card.save()
        return redirect('index')
    else:
        form = CardForm()
    return render (request, 'update_card.html',{"form":form,"card":card})

def post_card(request):
    current_user=request.user

    # Allows users to post new cards
    if request.method == 'POST':
        form = PostCard(request.POST,instance=card,files=request.FILES)

        if form.is_valid():
            card = form.save(commit=False)
            card.username = current_user
            card.save()
        return redirect('index')
    else:
        form =PostCard()
    return render(request,'post_card.html',{"form":form,"card":card})

def delete_card(request, id):
    try:
        card =Flashcard.objects.get(id=id)
    except:
        raise Htto404()
        

    return render(request,'delete_card.html',{"card":card}) 




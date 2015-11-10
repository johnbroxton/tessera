from users.forms import UserForm, UserProfileForm, PictureForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    #Return the index page
    return render(request, 'index.html')

def about(request):
    #Return the about page
    return render(request, 'about.html')

def register(request):
    # Initial value set to False. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        # Get form information.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        picture_form = PictureForm(data=request.POST)

        # If the forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Hash the password with the set_password method.
            user.set_password(user.password)
            user.save()

            # Sort out the UserProfile instance.
            profile = profile_form.save(commit=False)
            image = picture_form.save(commit=False)
            profile.user_extended = user
            image.user = user

            # User provides a photo
            if 'file' in request.FILES:
                image.file = request.FILES['file']

            # Save the UserProfile model instance.
            profile.save()
            image.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            return HttpResponseRedirect('/login/')

        # Print problems to the terminal, show to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Blank forms, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        picture_form = PictureForm()

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered,
             'picture_form': picture_form} )


def user_login(request):

    if request.method == 'POST':
        # Get username and password provided by the user from the login.

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username/password is valid

        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        if user:
            # Check if the account is active
            if user.is_active:
                # If the account is active, log the user in.
                login(request, user)
                usr_id = request.user.id
                profile = UserProfile.objects.get(user_extended = usr_id)

                return HttpResponseRedirect('/mosaic/'+str(profile.id))
            else:
                # Account is inactive
                return HttpResponse("Your Tessera account is disabled.")
        else:
            # Cannot log in the user
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'login.html', {})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def profile(request, pk):
    #show the photos the user has uploaded
    userp = UserProfile.objects.get(pk=pk)
    user_id = userp.user_extended.id
    images = Picture.objects.filter(user_id = user_id)
    print(images)
    return render(request, 'mosaic.html', {'image_set':images})


def upload(request):
    form = Picture()
    if request.method == "POST":
        form = Picture()
        form.file = request.FILES['new_image']
        form.user = request.user
        form.save()
    usr_id = request.user.id
    profile = UserProfile.objects.get(user_extended = usr_id)

    return HttpResponseRedirect('/mosaic/'+str(profile.id))


def show_image(request):
    image_set = UserProfile.objects.all()
    return render(request, 'mosaic.html', {'image_set':image_set})

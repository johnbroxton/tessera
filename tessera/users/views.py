from users.forms import UserForm, UserProfileForm, PictureForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from PIL import Image
from PIL import ImageOps
from .models import *

def index(request):
     return render(request, 'index.html')

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        picture_form = PictureForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            image = picture_form.save(commit=False)
            profile.user_extended = user
            image.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'file' in request.FILES:
                image.file = request.FILES['file']

            # Now we save the UserProfile model instance.
            profile.save()
            image.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            return HttpResponseRedirect('/login/')

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
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

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                usr_id = request.user.id
                profile = UserProfile.objects.get(user_extended = usr_id)

                return HttpResponseRedirect('/mosaic/'+str(profile.id))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Tessera account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

def profile(request, pk):
    userp = UserProfile.objects.get(pk=pk)
    images = Picture.objects.filter(user = pk)
    print("images")
    return render(request, 'mosaic.html', {'image_set':images})


def upload(request):
    form = Picture()
    if request.method == "POST":
        form = Picture()
        form.file = request.FILES['new_image']
        form.save()

    return render(request, 'mosaic.html', {'form':form})

# def mosaic(request):
#     return render(request, 'mosaic.html')

def show_image(request):
    image_set = UserProfile.objects.all()
    return render(request, 'mosaic.html', {'image_set':image_set})

# def bw_image(request):
#     bw_set = Picture.objects.all()
#     return render(request, 'mosaic.html', {'bw_set':bw_set})


# def show_image(request):
#     image = "IMG_2066.jpg"
#     image = Image.open(image)
#     image_set = ImageOps.grayscale(image)
#     return render(request, 'mosaic.html', {'image_set':image_set})
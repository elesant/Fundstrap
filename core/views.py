from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse("Success")
        else:
            return HttpResponse("Inactive")
    else:
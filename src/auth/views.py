from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()


def login_view(request):

    # print(request.POST or None)

    if request.method == 'POST':
        username = request.POST.get('username') or None
        password = request.POST.get('password') or None

        if all([username, password]):
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')

    return render(request, 'auth/login.html', {})


def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username') or None
        password = request.POST.get('password') or None
        email = request.POST.get('email') or None

        user_exists = User.objects.filter(username__iexact=username).exists()

        return render(request, 'auth/login.html', {})

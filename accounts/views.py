from django.shortcuts import render, redirect
from .forms import UserRegistrationFrom
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from predictor.models import Xray
from django.http import HttpResponse


# User registration view
def register_request(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserRegistrationFrom(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("/accounts/login")
            else:
                messages.error(request, "Unsuccessful registration. Invalid information.")
        else:
            form = UserRegistrationFrom()
        return render(request, template_name="accounts/register.html", context={"register_form": form})
    return redirect("/predictor")

# User login view
def login_request(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("/predictor")
            messages.error(request, "Invalid username or password.")
        else:
            form = AuthenticationForm()
        return render(request, template_name="accounts/login.html", context={"login_form": form})
    return redirect("/predictor")

# User logout view
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/accounts/login")

# Analysis page view
def analysis_view(request):
    xrays = Xray.objects.all()
    positive_count = xrays.filter(result='Positive').count()
    negative_count = xrays.filter(result='Negative').count()

    return render(request, 'accounts/analysis.html', {
        'positive_count': positive_count,
        'negative_count': negative_count,
    })


def personal_view(request):
    return render(request, 'accounts/personal.html')
def case_view(request):
    return render(request, 'accounts/case.html')
def precautions_view(request):
    return render(request, 'accounts/precautions.html')
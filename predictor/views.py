from django.shortcuts import render, redirect
from .forms import XrayForm
from django.http import HttpResponse
from .predictor_service import is_covid_positive
from .models import Xray

def render_upload_page(request):
   if request.user.is_authenticated:
      if request.method == 'POST':
         form = XrayForm(request.POST, request.FILES)

         if form.is_valid():
            xray = form.save()
            xray.user = request.user
            result = is_covid_positive(form.instance.image.path)
            xray.result = "POSITIVE" if result else "NEGATIVE"
            xray.save()
            return render(request, 'predictor/upload.html', {'form': form, 'xray': xray})
      else:
         form = XrayForm()
      return render(request, 'predictor/upload.html', {'form': form, 'xray': None})
   return redirect("/accounts/login")

def show_history(request):
   if request.user.is_authenticated:
      xrays = Xray.objects.filter(user=request.user).values()
      img = request.GET.get('img')
      return render(request, 'predictor/history.html', {'xrays': xrays, 'image': img})
   return redirect("/accounts/login")


def analysis_page():
   def analysis_page(request):
      # Your view logic for the analysis page goes here
      return render(request, 'analysis.html')
      # Replace 'analysis.html' with the actual template name

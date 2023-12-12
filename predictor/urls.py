from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from your current app (not 'predictor.views')

urlpatterns = [
    path('', views.render_upload_page, name='upload'),
    path('history/', views.show_history, name='history'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

from django.contrib import admin
from django.urls import path, include

# Import views directly from the app
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('analysis/', views.analysis_view, name='analysis'),
    path('personal/', views.personal_view, name='personal'),
    path('case/', views.case_view, name='case'),
    path('precautions/', views.precautions_view, name='precautions'),

    # Use analysis_view
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
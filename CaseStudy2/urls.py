from django.contrib import admin
from django.urls import include, path
from Feedback import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Add this line
    path('feedback/', include('Feedback.urls')),
]

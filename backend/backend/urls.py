from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/user/register/', CreateUserView.as_view(), name='register'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # add this 

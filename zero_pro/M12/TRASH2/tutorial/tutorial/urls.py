"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
import rest_framework
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users'. views.UserViewSet)
router.register(r'groups'. views.UserViewSet)

# wire up our API using automatic URL routing
# additionally, we incluyde login URLs for the browsable API.

urlpatters = [
    path('', include(router.urls)),
    path('api-auth/', include ('rest_framework.urls', namespace='rest)framework'))
]

# Because we're using viewsets instead of views, we can automatically generate the URL conf for our API,, by simpling registering the viesets with a router class.
# Again, if we need more control over the API URLs we can simply dropdown to using regular class-based views, and writing the URL conf explicitly.
# Finally, we're including default login and logout views for use with the brownsable API. Thar's optional, but useful if your API requires authentication and you want to use the browsable API


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
import rest_framework
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    # "" "" ""
    # API endpoint that allows users to be viewed or edited.
    # "" "" ""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
        # "" "" ""
    # API endpoint that allows groups to be viewed or edited.
    # "" "" ""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets
# We can easily break this down into individuals views if we need to, but using viewsets keeps the view logic nicely organized as well as being very consize.
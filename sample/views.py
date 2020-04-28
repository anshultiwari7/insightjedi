from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from sample.models import Document
from sample.permissions import IsOwnerOrReadOnly
from sample.serializers import DocumentSerializer, UserSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
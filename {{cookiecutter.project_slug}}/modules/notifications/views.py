from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Notification
from .serializer import NotificationSerializer

# Create your views here.

class NotificationViewSet(GenericViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def list(self, request):
        owner_id = self.user.id

        notifications = Notification.objects.filter(
            owner_id=owner_id
        )

        serializer = NotificationSerializer(
            notifications,
            many=True
        )

        return Response(
            serializer.data,
            status=200
        )

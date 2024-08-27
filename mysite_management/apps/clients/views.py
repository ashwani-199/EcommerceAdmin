from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ClientProfile, ClientAddress, ClientOrder
from .serializers import ClientProfileSerializer, ClientAddressSerializer, ClientOrderSerializer
from rest_framework.permissions import AllowAny


class ClientProfileViewSet(viewsets.ModelViewSet):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [AllowAny] ##Need to create access_token so that we user IsAuthenticated as a parameter

    # def get_querrset(self):
    #     status = self.request.querry_params.get('status', None)
    #     querryset = ClientProfile.objects.all()
    #     if status is not None:
    #         querryset = querryset.filter(status=status)
    #     return querryset

class ClientAddressViewSet(viewsets.ModelViewSet):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    permission_classes = [AllowAny] ##same as above IsAuthenticated



class ClientOrderViewSet(viewsets.ModelViewSet):
    queryset = ClientOrder.objects.all()
    serializer_class = ClientOrderSerializer

    def get_queryset(self):
        status = self.request.query_params.get('status', None)
        queryset = ClientOrder.objects.all()
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset
from rest_framework import serializers
from .models import ClientAddress, ClientOrder, ClientProfile
from rest_framework import viewsets

class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = ['id', 'user', 'phone_number', 'address', 'created_at', 'updated_at']

class ClientAddressSerializer(serializers.ModelSerializer):
    client_profile = ClientProfileSerializer(source ='client')
    class Meta:
        model = ClientAddress
        fields = ['id', 'client_profile', 'address', 'city', 'state', 'zipcode']

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        client_profile = ClientProfile.objects.create(**client_data)
        client_address = ClientAddress.objects.create(client = client_profile, **validated_data)
        return client_address
    
    def update(self, instance, validated_data):
        client_data = validated_data.pop('client')
        client_profile = instance.client
        client_profile.phone_number = client_data.get('phone_number', client_profile.phone_number)
        client_profile.address = client_data.get('address', client_profile.address)
        client_profile.save()

        instance.address = validated_data.get('address', instance.address)
        instance.city =validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.save()
        
        return instance

class ClientOrderSerializer(serializers.ModelSerializer):
    client_profile = ClientProfileSerializer(source = 'client')
    class Meta:
        model = ClientOrder
        fields = ['id', 'client_profile', 'total_amount', 'status']
    
    def create(self, validated_data):
        client_data = validated_data.pop('client')
        client_profile = ClientProfile.objects.create(**client_data)
        client_order = ClientOrder.objects.create(client = client_profile, **validated_data)
        return client_order
    
    
    def update(self, instance, validated_data):
        client_data = validated_data.pop('client')
        client_profile_serializer = ClientProfileSerializer(instance.client, data=client_data, partial=True)
        if client_profile_serializer.is_valid():
            client_profile_serializer.save()

        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance




    
    # def update(self, instance, validated_data):
        
    #     client_data = validated_data.pop('client')
    #     client_profile = instance.client
    #     client_profile.phone_number = client_data.get('phone_number', client_profile.phone_number)
    #     client_profile.address = client_data.get('address', client_profile.address)
    #     client_profile.save()

    #     instance.total_amount = validated_data.get('total_amount', instance.total_amount)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance
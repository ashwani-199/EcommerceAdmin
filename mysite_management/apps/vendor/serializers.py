from rest_framework import serializers
from apps.vendor.models import Vendor, VendorProfile
from apps.users.serializers import UserSerializer
from apps.users.models import User

class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'store_name', 'store_description', 'address', 'logo', 'created_at']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        vendor = Vendor.objects.create(user=user, **validated_data)
        return vendor
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(instance.user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
        instance.store_name = validated_data.get('store_name', instance.store_name)
        instance.store_description = validated_data.get('store_description', instance.store_description)
        instance.address = validated_data.get('address', instance.address)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.save()
        return instance
    

class VendorProfileSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    class Meta:
        model = VendorProfile
        fields = ['id', 'vendor', 'company_name', 'contact_person', 'email', 'phone', 'address', 'created_at', 'updated_at']

    def create(self, validated_data):
        vendor_data = validated_data.pop('vendor')
        vendor = Vendor.objects.create(**vendor_data)
        vendors = VendorProfile.objects.create(vendor=vendor, **validated_data)
        return vendors
    
    def update(self, instance, validated_data):
        vendor_data = validated_data.pop('vendor')
        vendor_serializer = VendorSerializer(instance.vendor, data=vendor_data, partial = True)
        if vendor_serializer.is_valid():
            vendor_serializer.save()
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.contact_person = validated_data.get('contact_person', instance.contact_person)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
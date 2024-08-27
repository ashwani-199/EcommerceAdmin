from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','is_superuser','is_staff','is_active']
       
# class AuthTokenSerializer(serializers.ModelSerializer):

#     user = UserSerializer(source = 'user')
#     class Meta:
#         model = AuthToken
#         fields = ['id', 'user', 'token', 'created_at', 'updated_at']


# class PasswordResetTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PasswordResetToken
#         fields = '__all__'


# class UserActivitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserActivity
#         fields = '__all__'


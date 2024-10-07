from apps.users.models import User
from django.contrib.sites.shortcuts import get_current_site
import hashlib
import datetime
import time


PROTOCOL = 'http://'
RESET_PASSWORD_URL = '/reset-password/'



class MainService:
    def __init__(self, request):
        self.request = request
        self.currentSite = get_current_site(self.request)
        self.user = None

    def passwordForgotLink(self, user):
        self.user = user
        email = self.user.email
        timeStamp = time.mktime(datetime.datetime.today().timetuple())
        keyString = str(email) + str(timeStamp)
        res = hashlib.md5(keyString.encode())
        tokenString = res.hexdigest()
        user = self.saveForgotPasswordData(tokenString, None)
        return user

    def saveForgotPasswordData(self, tokenString, OTP):
        userObj = User.objects.get(id=self.user.id)
        if OTP is None:
            userObj.forgot_password_string = tokenString
            userObj.save()
        else:
            userObj.forgot_password_string = tokenString
            userObj.forgot_password_otp = OTP
            userObj.save()
        return userObj

    def createUrlString(self, tokenString):
        forgotPasswordUrl = str(self.currentSite) + RESET_PASSWORD_URL + tokenString + '/'
        return forgotPasswordUrl

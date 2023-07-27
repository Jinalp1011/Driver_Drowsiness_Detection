from django.db import models
# from django.contrib.auth.models import AbstractUser

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(null=True,max_length=15)
    email = models.EmailField(null=True,max_length=15)
    password = models.CharField(max_length=500)
    license_id = models.CharField(max_length=100, unique=True)


    def register(self):
        self.save()
        
        
    @staticmethod
    def get_user_by_license_id(license_id):
        try:
            return User.objects.get(license_id = license_id)
        # Customer.objects.get(email = email)
        except:
            return False
        
    def isExist(self):
        if User.objects.filter(license_id = self.license_id):
            return True
        
        return False
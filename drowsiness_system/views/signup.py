from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from drowsiness_system.models.user import User


class Signup(View): 
    def get(self,request):
        return render(request , 'signup.html')
    
    
    def post(self,request):
        ##collect all the data from here 
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        license_id = request.POST['license_id']
        password = request.POST['password']
        
        #validation
        value = {
                'first_name' : first_name,
                'last_name' : last_name,
                'phone' : phone,
                'email' : email,
                'license_id' : license_id
            }
            
        error_message = None
         
        #create customer user   
        user = User(first_name = first_name,
                                last_name = last_name,
                                phone = phone,
                                email = email,
                                license_id = license_id,
                                password = password)
            
        error_message = self.validateCustomer(user)  #it will validate customer if there is an error then it will return the error.
    
        #saving
        #if not error then register the deatils
        if not error_message:
            print(first_name,last_name,phone,email,license_id,password)
            user.password = make_password(user.password)
            user.register()
            # return redirect('index.html') #it will redirect to the pass you link.
            return render(request,'index.html')  #if the signup go3es succes it will go to the index.html pagee you pass in next argument.
            
        else:  #if there is an error then return signup page
            data = {
                'error' : error_message,
                'values': value
            }
            return render(request,'signup.html',data)
        
        
    def validateCustomer(self,user):
        error_message = None
        
        if not user.first_name:
            error_message = "First Name required!!"
        elif len(user.first_name) < 4:
            error_message = "First name must be 4 char long or more."
        elif not user.last_name:
            error_message = "Last name required!!" 
        elif len(user.last_name) < 4:   
            error_message = "Last name must be 4 char long or more."
        elif not user.phone:
            error_message = "Last name required!!" 
        elif len(user.phone) < 10:   
            error_message = "phone number must be 10 char."
        elif not user.password:
            error_message = "password required!!" 
        elif len(user.password) < 6:   
            error_message = "Password must be 6 char long and more."
        elif not user.email:
            error_message = "Email required!!"
        elif len(user.email) < 5:
            error_message = "Email must be 5 char long and more."
        elif not user.license_id:
            error_message = "License_ID required!!"
        elif user.isExist(): 
            error_message = 'License_ID already Registered.'
            
        return error_message
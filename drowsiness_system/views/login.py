from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from drowsiness_system.models.user import User

class Login(View):
    def get(self, request):
        return render(request,'login.html')
    
    
    def post(self,request):
        license_id = request.POST['license_id']
        password = request.POST['password']
        user = User.get_user_by_license_id(license_id)

        # print(customer)
        error_message = None
        if user:
            flag = check_password(password,user.password)
            if flag:
                request.session['user'] = user.id
               
                return render(request,'index.html')
            else:
                error_message = "License_ID or Password invalid!"
        else:
            error_message = "License_ID or Password invalid!"
        print(license_id,password)
        return render(request,'login.html',{'error':error_message})
    
    
def logout(request):
    request.session.clear()
    # return redirect('login')
    return render(request,'index.html')
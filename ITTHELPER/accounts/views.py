from django.shortcuts import render
from rest_framework.decorators import APIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate,login, logout
from Server.views import HomeView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request,format=None):
        if request.method == "POST":
            data = request.data
            myuser = UserSerializer(data=data) 
            if myuser.is_valid():
                save_user = UserSerializer.save(myuser)
                if save_user : 
                    json = myuser.data
                    return Response(json)
        return Response(myuser.errors)
    

    
def sign_up_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        password= request.POST.get("password")
        # date_of_birth = request.POST("date_of_birth")
        phone_number = request.POST.get("phone_number")
        try :
           user = CustomUser.objects.create(
                username=username,
                email=email,
                phone_number=phone_number,
                first_name = first_name,
                last_name=last_name
                # date_of_birth=date_of_birth
            )
           user.set_password(password)
           user.save()
           if user :
               return redirect(login_user)
        except: 
            return render(request ,'signup.html')
    # else :
    #     return render(request, 'not_authed.html')
    return render(request,'signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password= request.POST.get("password")
        # print(username,password)
        try :
            user = authenticate(
                u_e_p=username,
                password = password
            )
            if user is not None :
                login(request,user)
                print(user)
                return redirect(HomeView)
        except:
            print("user in not vaild")    

    return render(request, 'login.html') 

@login_required
def logout_user(request):
    if request.method == "POST":
        logout(request)
    return redirect(HomeView)
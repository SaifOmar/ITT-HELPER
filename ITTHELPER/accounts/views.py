from django.shortcuts import render
from rest_framework.decorators import APIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate,login, logout
from Server.views import HomeView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.http import JsonResponse 
from rest_framework_simplejwt.tokens  import RefreshToken


#mvvm

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request,format=None):
            data = request.data
            myuser = UserSerializer(data=data) 
            if myuser.is_valid():
                save_user = UserSerializer.save(myuser)
                if save_user : 
                    json = myuser.data
                    return Response(json)
            return Response(myuser.errors)
    
class LoginView(APIView):
    permission_classes= [AllowAny]
    def post(self, request, format = None):
        u_e_p = request.data.get('username')
        password = request.data.get('password')
        try :
            user = authenticate(u_e_p=u_e_p, password=password)
            if user :
                login(request,user)
                #pass user to the token endpoint to make the refresh token and return a response with the tokens and (..) ??
                token = RefreshToken.for_user(user)
                response  = {"refresh" : str(token),
                            "access" : str(token.access_token)}
                return Response(response)
            else :
                return Response({"error": "An error happend while trying to log you in, Please try again!"})
        except : 
                response = {"error" : "We couldn't find a user with the given username or password"}
                return Response(response)
            
    
            
class LogoutView(APIView):
    def get(self,request, format = None):
            logout(request)
            return Response({"response" : "You logged out successfully"})





##






#mvc
    
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
        u_e_p = request.POST.get("username")
        password= request.POST.get("password")
        # print(username,password)
        try :
            user = authenticate(
                u_e_p=u_e_p,
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

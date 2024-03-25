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
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from rest_framework_simplejwt.tokens  import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.authentication import JWTAuthentication



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
    
class LogoutView(APIView):
    def post(self,request, format = None):
            try :
                refresh = request.data["refresh"]
                token = RefreshToken(refresh)
                token.blacklist() 
                
                return Response({"response":"You logged out successfully"})
            except :
                return Response({"response":"you are already logged out"})
           
# class LoginView(APIView):
#     permission_classes= [AllowAny]
#     def post(self, request, format = None):
#         u_e_p = request.data.get('username')
#         password = request.data.get('password')
#         try :
#             user = authenticate(u_e_p=u_e_p, password=password)
#             if user is not None:
#                 login(request,user)
#                 token = RefreshToken.for_user(user)
#                 response  = {"refresh" : str(token),
#                             "access" : str(token.access_token)}
#                 #pass user to the token endpoint to make the refresh token and return a response with the tokens and (..) ??
#                 return Response(response)
#             else :
#                 return Response({"error": "An error happend while trying to log you in, Please try again!"})
#         except : 
#                 response = {"error" : "We couldn't find a user with the given username or password"}
#                 return Response(response)
            





##






#mvc
    
def sign_up_user(request):
    if request.method == 'POST':
        if not request.user.is_authenticated :
            username = request.POST.get("username")
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name= request.POST.get("last_name")
            password= request.POST.get("password")
            phone_number = request.POST.get("phone_number")
            # date_of_birth = request.POST.get("date_of_birth")
            try :
                    user = CustomUser.objects.create(
                    username=username,
                    email=email,
                    phone_number=phone_number,
                    first_name = first_name,
                    last_name=last_name)
                    # date_of_birth=date_of_birth
                    user.set_password(password)
                    user.save()
                    if user :
                        return redirect(login_user)
            except: 
                    return render(request ,'signup.html')
        else :
                return redirect(HomeView)
    return render(request,'signup.html')

def login_user(request):
    if not request.user.is_authenticated :
        if request.method == "POST":
            u_e_p = request.POST.get("username")
            password= request.POST.get("password")
            try :
                user = authenticate(
                    u_e_p=u_e_p,
                    password = password
                )
                if user is not None :
                    login(request,user)
                    print(user)
                    return redirect(HomeView)
                else : 
                        return render(request, "not_authed.html")
            except:
                #return htmx here 
                print("user in not vaild")
    else :
            return redirect(HomeView)

    return render(request, 'login.html')


def logout_user(request):
    #will be changed to post method later
    if request.method == "GET":
        if request.user.is_authenticated :
            logout(request)
            return HttpResponseRedirect(login_user)
        else :
            return redirect(login_user)
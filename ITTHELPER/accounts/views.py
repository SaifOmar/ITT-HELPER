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
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.conf import settings 
import requests

# Create your views here.

# These are tthe mobile app views

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request,format=None):
            data = request.data
            myuser = UserSerializer(data=data) 
            if myuser.is_valid():
                save_user = UserSerializer.save(myuser)
                if save_user : 
                    # json = myuser.data
                    return Response({"response":"You signed up successfully"})
                    # return Response(json)
            else :
                return Response(myuser.errors,{"response":"You should enter your creds correctly"})
                     
    
class LogoutView(APIView):
   # permission_classes = IsAuthenticated
    def post(self,request, format = None): 
            try :
                refresh = request.data["refresh"]
                token = RefreshToken(refresh)
                token.blacklist() 
                
                return Response({"response":"You logged out successfully"})
            except :
                return Response({"response":"you are already logged out"})

jwt_authenticate_access = JWTAuthentication()
class ChangePasswordView(APIView):
    # permission_classes = IsAuthenticated
    def post(self,request):
        response ={"response":"An error happened while trying to change your password, Please try again later"} 
        try :
            auth = jwt_authenticate_access.authenticate(request)
            if auth :
                user, token = auth
                old_password = request.data['old_password']
                password1 = request.data["password1"]
                password2 = request.data["password2"]
                if not check_password(old_password,user.password):
                    return Response({"response":"The password you entered was incorrect"})
                if password1 == password2 :
                    user.set_password(password1)
                    user.save
                    return Response({"response":"Password changed successfully!"})
            else :
                return Response(response)
        except :
                return Response(response)

class VerifyEmailMobile(APIView):
    def post(self,request):
        if request.user.email_is_verified != True:
            user = request.user
            site = get_current_site(request)
            subject = "Verify Email"
            message = render_to_string(
                 'MobileVerificationMessage.html', {
                      'request' : request,
                      'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                      'domain': site.domain,
                      'user': user,
                      'token': account_activation_token.make_token(user),
                }
            )
        email = EmailMessage(
                subject,message,to =[user.email]
           )
        email.content_subtype = 'html'
        email.send()
        response = {"responese": "Please check your email for to verify your account!"}
        return Response(response)
    
class VerifyEmailCheck(APIView):
        def get(self,uidb64,token):
                try :
                    uid = force_str(urlsafe_base64_decode(uidb64))
                    user = CustomUser.objects.get(pk=uid)
                except :
                    (TypeError,ValueError,OverflowError,CustomUser.DoesNotExist)
                    user = None
                if user is not None and account_activation_token.check_token(user,token) is not False:
                    user.email_is_verified = True
                    user.save()
                    response = "Your email verification was successful" 
                    return Response(response)
                else : 
                    response = "Something went wrong while trying to verify your email"
                    return Response(response)






#These are the website views    
def sign_up_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
            username = request.POST.get("username")
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name= request.POST.get("last_name")
            password1= request.POST.get("password1")
            password2= request.POST.get("password2")
            phone_number = request.POST.get("phone")
            is_company = request.POST.get('is_company')
            # date_of_birth = request.POST.get("date_of_birth")
            if password2 != password1 :
                messages.warning(request,"Passwords didn't match")
                return redirect('signup')
            try :
                    password = password2
                    user = CustomUser.objects.create(
                    username=username,
                    email=email,
                    phone_number=phone_number,
                    first_name = first_name,
                    last_name=last_name,
                    is_company=is_company
                    )
                    user.set_password(password)
                    user.save()
                    if user :
                        user = authenticate(
                            u_e_p = username,
                            password=password)
                        login(request,user)
                        return redirect('verify_email')
                    else :
                        messages.error(request,"we couldn't sign you up 1")
                        return redirect('signup')
            except: 
                    messages.error(request,"we couldn't sign you up 2")
                    return redirect('signup')
    return render(request,'signup.html')



def login_user(request):
    if request.user.is_authenticated :
        return redirect('home') 
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
                return redirect(HomeView)
            else : 
                    messages.error(request,"we couldn't find a user with these creds ")
                    return redirect('login')
        except:
            return redirect(login_user)

    return render(request, 'login.html')




def logout_user(request):
    if not request.user.is_authenticated :
        return redirect('login')
    # change to post method later
    if request.method == "POST":
            logout(request)
            messages.success(request,"You logged out successfully")
            return redirect('login')
        

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "profile.html")

def change_info(request):
    if not request.user.is_authenticated :
        return redirect('login')
    if request.method == "POST":
        try:
            user = request.user
            fname = request.POST.get("first_name")
            lname= request.POST.get("last_name")
            username= request.POST.get("username")
            email= request.POST.get("email")
            phone = request.POST.get("phone")
            user.first_name = fname
            user.last_name = lname
            user.username = username
            user.phone_number = phone 
            user.email = email
            user.save()
        except:
            messages.error(request, "Something went wrong.")
            return redirect('profile')
        messages.success(request,"Your info was updated!")
        return redirect('profile')

def change_pic(request):
    if not request.user.is_authenticated :
        return redirect('login')
    if request.method == "POST":
        try :
            user= request.user
            img = request.FILES['image']
            user.img=img
            user.save()
        except :
            messages.error(request, "Something went wrong.")
            return redirect('profile')
        messages.success(request,"Your pictue was Changed!")
        return redirect('profile')
             

def change_password(request):
    if not request.user.is_authenticated :
        return redirect('login')
    if request.method == "POST":
        user = request.user
        old_password = request.POST.get('old_password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if check_password(old_password,user.password):
            if password1 == password2:
                user.set_password(password1)
                user.save()
                user = authenticate(u_e_p=user.email,password= password1)
                login(request,user)
                messages.success(request,"Password changed successfully")
                return redirect('profile')
            else : 
                messages.error(request,"Password changed successfully")
                return redirect('profile')
        else :
                messages.warning(request,"Please enter the correct old password")
                return redirect('profile')
                  


def forgot_password(request):
    if request.user.is_authenticated:
        user = request.user
        email = request.user.email
    else :
        email = request.POST.get("email")
        user = CustomUser.objects.get(email=email)
        if not user:
            messages.error(request,"we couldn't find any accnounts with this email")
            return redirect('login')
    if user:
        try :
            site = get_current_site(request)
            subject = "Forgot Password"
            message = render_to_string(
                'forgot_pw_msg.html', {
                    'request':request,
                    'user': user,
                    'domain': site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                    }
                )
            E = EmailMessage(
                subject,message,to = [email]
            )
            E.content_subtype = 'html'
            E.send()
            messages.success(request,"We sent you an email, Please check your inbox!")
            return redirect("profile")
        except :
            messages.error(request,"something went wrong")
            return redirect('profile')
    else :
        messages.error(request,"we couldn't find any accounts with this email")
        return redirect('profile')


def forgot_password_callback(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if not request.user.is_authenticated :
            user = authenticate(e_u_p = user.email,password = user.password)
            login(request,user)
        return render(request,'change_pw_forgot.html')   
    else:
        messages.warning(request, 'The link is invalid.')
        return redirect('profile')
    
    
def change_forgot_password(request):
    if request.method == "POST":
        user = request.user
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2 :
            user.set_password(p1)
            user.save()
            return redirect('profile')
        else :
            messages.warning(request,"Passwords don't match")
            return redirect('profile')
            


@login_required
def verify_email(request):
    if not request.user.email_is_verified :
        user = request.user
        site = get_current_site(request) 
        email = request.user.email
        subject = "Verify Email"
        message = render_to_string(
            'verify_email_message.html', {
                'request':request,
                'user': user,
                'domain': site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                }
            )
        E = EmailMessage(
            subject,message,to = [email]
        )
        E.content_subtype = 'html'
        E.send()
        return redirect(verify_email_pending)
    return render(request,'verify_email.html')

@login_required
def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect(verify_email_complete)   
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'verify_email_confirm.html')


@login_required
def verify_email_pending(request):
    return render(request, 'verify_email_pending.html')

@login_required
def verify_email_complete(request):
        return render(request, 'user/verify_email_complete.html')


def oauth_redirect(request):
    google_redirect_url = (
    "https://accounts.google.com/o/oauth2/auth"
    "?response_type=code"
    "&client_id={client_id}"
    "&redirect_uri={redirect_uri}"
    "&scope=openid%20email%20profile"
    ).format(client_id = settings.GOOGLE_CLIENT_ID,
    redirect_uri =settings.GOOGLE_REDIRECT_URI)
    return redirect(google_redirect_url)

def callback(request):
        code = request.GET.get("code")
        token_url = "https://oauth2.googleapis.com/token"
        token_date = {
            "code": code,
            "clinet_id": settings.GOOGLE_CLIENT_ID,
            "clinet_secret":settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type":"authorization_code",
        }
        token_r = requests.post(token_url, data = token_date)
        token_json = token_r.json()
        access_token = token_json.get("access_token")

        user_info_url= "https://www.googleapis.com/oauth2/v1/userinfo"
        user_info_parametars = {"access_token":access_token}
        user_info_r = requests.get(user_info_url,params=user_info_parametars)
        user_info  = user_info_r.json()
        print(user_info)

        user = CustomUser.objects.get(user_info["email"])

        if user :
            email = user_info["email"]
            password = user.password
            user = authenticate(u_e_p = email, password= password)
            login(request,user)
            messages.error(request,"smth went wrong")
            return redirect('login')
        
        elif not user :
            try :
                CustomUser.objects.create(
                email= user_info["email"],
                # would fail bcs phone and username are needed i think
                # make username from email (before@) or random username using the email and make phone number not necesaary to sign up
                first_name = user_info["given_name"],
                last_name = user_info["family_name"],
                username = user_info["given_name"] + user_info["family_name"]
                                      )
                user.set_password(email)
                user.save()
                user = authenticate(u_e_p = email , password=password)
                login(request,user)
                return redirect('home')
            except :
                (ValueError,TypeError,OverflowError)
                messages.error(request,"we failed to log you in")
                return redirect()
        else :
            return render(request,"something_blew_up.html")     

# display for errors
def something_blew_up(request):
     return render(request, "something_blew_up.html")
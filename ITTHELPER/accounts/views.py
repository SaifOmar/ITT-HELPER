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
            password= request.POST.get("password")
            phone_number = request.POST.get("phone")
            # date_of_birth = request.POST.get("date_of_birth")
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
                        return redirect('verify_email')
                    else :
                        return redirect('singup')
            except: 
                    messages.error(request,"we couldn't sign you up")
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
    if request.method == "GET":
            logout(request)
            messages.success(request,"You logged out successfully")
            return redirect('login')
        




@login_required
def change_password(request):
    if request.method == "POST":
         if request.user.is_authenticated :
            if request.user.email_is_verified != True:
              return redirect(verify_email)
            else :
                user = request.user
                old_password = request.POST.get("old_password")
                password1 = request.POST.get("password1")
                password2 = request.POST.get("password2")
                if not check_password(old_password,user.password):
                    messages.error(request, "The password you entered was incorrect")
                    return redirect(change_password)
                if password1 == password2 :
                    user.set_password(password1)
                    user.save()
                    messages.success(request,"Password changed successfully")
                    return redirect(change_password)
                # need to handle what happens to user
                else:
                    messages.error(request, "Passwords don't match")
                    return redirect(change_password)
    return(request, "changepw.html")
            

#pw change email verification needs to be thought about and implemented later
# refactor but you have base now
def forgot_password(request):
    if request.user.is_authenticated:
        user = request.user
        email = request.user.email
    else :
        email = request.POST.get("email")
        user = CustomUser.objects.get(email=email)
    if user:
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
        return render(request, "forgot_password")
    else :
        messages.error(request,"we couldn't find any accnounts with this email")
        return redirect(forgot_password)

def forgot_password_callback(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # should either log in and redirect to the change password page, or do pw change template in it, change all redirects
        messages.success(request, 'Your email has been verified.')
        return redirect(verify_email_complete)   
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'verify_email_confirm.html')


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
    ).format(client_id = settings.GOOGLE_CILENT_ID,
    redirect_uri =settings.GOOGLE_REDIRECT_URI)
    return redirect(google_redirect_url)

def callback(request):
        code = request.GET.get("code")
        token_url = "https://oauth2.googleapis.com/token"
        token_date = {
            "code": code,
            "clinet_id": settings.GOOGLE._CLIENT_ID,
            "clinet_secret":settings.GOOGLE_CLINET_ID,
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

        user = CustomUser.objects.get(user_info["id"])

        if user :
            login(request,user)
            return redirect()
        
        elif not user :
            try :
                CustomUser.objects.create(
                email= user_info["email"],
                #would fail bcs phone and username are needed i think
                # make username from email (before@) or random username using the email and make phone number not necesaary to sign up
                first_name = user_info["given_name"],
                last_name = user_info["family_name"],
                                      )
                login(request,user)
                return redirect()
            except :
                (ValueError,TypeError,OverflowError)
                messages.error(request,"we failed to log you in")
                return redirect()
        else :
            return render(request,"something_blew_up.html")     

# display for errors
def something_blew_up(request):
     return render(request, "something_blew_up.html")
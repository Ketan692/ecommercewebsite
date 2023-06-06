from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from accounts.models import Address
from django.contrib.auth import logout as django_logout

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        User.objects.filter(email=email).delete()
        
        usernames = User.objects.filter(username = username)
        users_email = User.objects.filter(email = email)
        
        if usernames:
            messages.error(request, "Username already in use.")
            return render(request, "templates/accounts/register.html")
        
        if users_email:
            messages.error(request, "Email already in use.")
            return render(request, "templates/accounts/register.html")
        
        if password1 != password2 :
            messages.error(request, "Passwords didn't match.")
            return render(request, "templates/accounts/register.html")
        
        if not len(password1) >= 8 :
            messages.error(request, "Password must be at least 8 characters long.")
            return render(request, "templates/accounts/register.html")
        
        new_user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password1, is_active = False)
        new_user.save()
        activateEmail(request, new_user, email)
        return redirect("login")

    else:
        return render(request, "templates/accounts/register.html")
    

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('templates/accounts/template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('home')


def user_address(request, user):
    data = None
    full = 2
    the_user = list(Address.objects.filter(user_id = user))
    if len(the_user)<2:
        full = None
    
    if the_user:
        data = {
            "address": the_user,
            "full": full,
        }
    
    return render(request, 'templates/accounts/user_address.html', data)


def add_user_address(request, user):

    the_user = list(User.objects.filter(id = user))[0]
    
    data = {
        "user":the_user,
        "full_name":the_user.first_name.capitalize()+" "+the_user.last_name.capitalize(),
        "states":["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
    }
    return render(request, 'templates/accounts/add_user_address.html', data)


def edit_address(request, address):
    the_address = Address.objects.get(id = int(address))
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile_no')
        postal_code = request.POST.get('postal_code')

        the_address.name = name
        the_address.address = address
        the_address.state = state
        the_address.city = city
        the_address.mobile = mobile
        the_address.postal_code = postal_code
        the_address.save()

        return redirect("user_address", user = the_address.user_id)



    the_address = Address.objects.filter(id = int(address))
    data = {
        "address": the_address,
        "states":["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
    }
    print(the_address)
    return render(request, "templates/accounts/edit_address.html", data)


def delete_address(request, address):
    Address.objects.filter(id=address).delete()
    return redirect("user_address", user=request.user.id)


def submit_address(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile_no')
        postal_code = request.POST.get('postal_code')

        new_address = Address(user_id=request.user.id, name=name, address=address, state=state, city=city, mobile=mobile, postal_code=postal_code)
        new_address.save()
        return redirect('user_address', user=request.user.id)
    
    return redirect('user_address', user=request.user.id)
    

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        
        if not user:
            messages.error(request, "Enter correct username.")
            return redirect("login")
        
        if user[0].is_active == False:
            messages.error(request, f"Hey {user[0].first_name}, Acivate your account with email sent on <b>{user[0].email}</b>")
            return redirect("login")
        
        if user:
            user_auth = authenticate(username=username, password=password)
            if user_auth == None:
                messages.error(request, f"Check your Password.")
                return redirect('login')
            elif user_auth:
                login(request, user[0])
                return redirect('home')
        
    return render(request, "templates/accounts/login.html")


def logout(request):
    django_logout(request)
    return redirect('home')

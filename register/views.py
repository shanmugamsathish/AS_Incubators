
from django.shortcuts import redirect, render
from register.models import user1
from django.contrib import messages
from django.db import connection
from django.contrib.auth.models import User, auth

from register.models import user1

# Create your views here.
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, password=password, email=email, mobile=mobile)
        user.save();
        print('User Created')
        return redirect('/')
    

    else:
        return render(request,'register/register.html')

def registeruser(request):
    result=user1.objects.all();
    userlist = {'allusers':result}
    return render(request, 'register/userlist.html',userlist)


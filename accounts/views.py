from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from .forms import UserCreationForm,LoginForm
from .models import Profile
# Create your views here.

def signup(request):
    context=dict()
    
    if request.method=="POST":
        #회원가입 프로세스
        save_form = UserCreationForm(request.POST)
   
        
        if save_form.is_valid():
            save_form.save()
        
            
            ##회원가입후에 자동 로그인이 되는 프로세스
            user = authenticate(username=save_form.cleaned_data['username'], 
                                password =save_form.cleaned_data['password1'])
            
            login(request,user)
            
            #이쯤되면 signal때문에 profile생성
            
            print("%"*50)
            return redirect('index')
        else:
            print("8"*50)

            context['user_form'] = save_form
            return render(request,'registration/signup.html', context)
    else:
        user_form = UserCreationForm()
        context['user_form'] = user_form
        
        #프로필 입력 폼을 profile_form이름으로 signup에 넘김
        context['profile_form'] =LoginForm()
        
        return render(request,'registration/signup.html', context)



from django.contrib.auth.models import User  

def profile(request,pk):
    context=dict()
    pro_info = User.objects.get(id = pk)
    
    context['pro_info'] = pro_info
    print(pro_info.profile.location)
    return render(request,'profile.html',context)
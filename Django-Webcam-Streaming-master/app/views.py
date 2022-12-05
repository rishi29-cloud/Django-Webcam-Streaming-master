from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect, Http404
# Create your views here.






@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            loginuser = form.get_user()
            if loginuser is not None:
                if loginuser.is_active:
                    auth_login(request, loginuser)
                    if request.GET.get('next'):
                        return HttpResponseRedirect('/home')
                else:
                    errors='activate account through mail'
            return HttpResponseRedirect('/home')
            #return HttpResponseRedirect('/home/')
    else:
        form = AuthenticationForm()
    return render(request,"index.html", locals())

def logout_page(request):
    return render(request,"index.html", locals())

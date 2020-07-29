from django.shortcuts import render,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account
# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    # return HttpResponse(user.account.role)
    user = get_object_or_404(Account,user=request.user)
    return render(request,'account/center.html',{'user':user})

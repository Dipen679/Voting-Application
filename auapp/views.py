from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Question
from .forms import QuesForm


def ucreate(request):
	if request.user.is_authenticated:
		if request.method=="POST":		
			data=QuesForm(request.POST)
			if data.is_valid():
				data.save()
				return redirect("uhome1")
				fm = QuesForm()
				return render(request,"ucreate.html",{"fm":fm,"msg":msg})
			else:	
				msg="Check Errors"
				return render(request,"ucreate.html",{"fm":data,"msg":msg})
		else:
			fm=QuesForm()
			return render(request,"ucreate.html",{"fm":fm})
	else:
		return redirect("uhome")

	
def uresult(request,poll_id):
	if request.user.is_authenticated:
		data=Question.objects.get(pk=poll_id)
		return render(request,"uresult.html",{"data":data})
	else:
		return redirect("uhome")

def uvote(request,poll_id):
	if request.user.is_authenticated:
		data=Question.objects.get(pk=poll_id)
		if request.method=="POST":
			selected_option=request.POST["poll"]
			if selected_option == "op1":
				data.option_one_count += 1 
			elif selected_option == "op2":
				data.option_two_count += 1 
			else:
				data.option_three_count += 1
			data.save()
			return redirect("uhome1")
	else:
		return redirect("uhome")
		
	
	return render(request,"uvote.html",{"data":data})

def uhome(request):
	if request.user.is_authenticated:
		return redirect("uhome1")
	else:
		if request.method=="POST":
			un=request.POST.get("un")
			pw=request.POST.get("pw")
			usr=authenticate(username=un,password=pw)
			if usr is None:
				return render(request,"uhome.html",{"msg":"Invalid username/Password"})
			else:	
				login(request,usr)
			return redirect("uhome1")
		else:
			return render(request,"uhome.html")

def usignup(request):
	if request.user.is_authenticated:
		return redirect("uhome1")
	else:
		if request.method=="POST":
			un=request.POST.get("un")
			pw1=request.POST.get("pw1")
			pw2=request.POST.get("pw2")
			if pw1==pw2:
				try:
					usr=User.objects.get(username=un)
					return render(request,"usignup.html",{"msg":"User Already 	Exists"})
				except User.DoesNotExist:
					usr=User.objects.create_user(username=un,password=pw1)
					usr.save()
					return redirect("uhome")
			else:
				return render(request,"usignup.html",{"msg":"Password Didnt Match"})
		else:
			return render(request,"usignup.html")

def uhome1(request):
	data=Question.objects.all()
	return render(request,"uhome1.html",{"data":data})

def ulogout(request):
	logout(request)
	return redirect("uhome")

def ucp(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			pw1=request.POST.get("pw1")
			pw2=request.POST.get("pw2")
			if pw1==pw2:
				try:
					usr=User.objects.get(username=request.user.username)
					usr.set_password(pw1)
					usr.save()	
					return redirect("uhome")
				except User.DoesNotExist:
					return render(request,"ucp.html",{"msg":"user does not exists"})
					
			else:
				return render(request,"ucp.html",{"msg":"Password Didnt Match"})
		else:
			return render(request,"ucp.html")
	else:
		return redirect("uhome1")

def remques(request,poll_id):
	de=Question.objects.get(pk=poll_id)
	de.delete()
	return redirect("uhome1")



	


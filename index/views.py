from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from people.models import People,MyClass
from django.core.urlresolvers import reverse
class CheckLogForm(forms.Form):
	name = forms.CharField(label='姓名',max_length=10)
	phone = forms.CharField(label='手机号',max_length=11)

class RegistForm(forms.Form):
	name = forms.CharField(label='姓名',max_length=10)
	phone = forms.CharField(label='手机号',max_length=11)
	home_addr = forms.CharField(label='家庭住址',max_length=40)
	work_addr = forms.CharField(label='工作地址',max_length=40)
	profession= forms.CharField(label='从事行业',max_length=15)
	company =   forms.CharField(label='公司/职位',max_length=16)
	is_married =forms.NullBooleanField(label='婚否')
	photo = forms.ImageField(label='近期照片')
class ClassPasswdForm(forms.Form):
	passwd = forms.CharField(label='班级暗号',max_length=30)

def index(request):
	if request.method == 'POST':
		if request.POST.get('login',False):
			loginform = CheckLogForm(request.POST)
			if loginform.is_valid():
				username = loginform.cleaned_data['name']
				userphone = loginform.cleaned_data['phone']
				try:
					user = People.objects.get(phone=userphone,name=username)
				except:
					return render(request,'loginerror.html')  
				else:
					request.session['phone']=userphone
					request.session['is_login']=True
					return HttpResponseRedirect(reverse('profile',args={userphone}))
			else:
				return render(request,'inputblank.html')
		elif request.POST.get('checkpasswd',False):
			passwdform = ClassPasswdForm(request.POST)
			if passwdform.is_valid():
				passwd=passwdform.cleaned_data['passwd']
				try:
					myclass = MyClass.objects.get(password=passwd)
				except:
					return render(request,'passwderror.html')  
				else:
					request.session['myclass']=myclass.name
					return HttpResponseRedirect(reverse('regist'))
			else:
				return render(request,'inputblank.html')
	else:
		loginform = CheckLogForm()
		checkpasswdform=ClassPasswdForm()
		return render(request,'index.html',{'loginform':loginform,'checkpasswdform':checkpasswdform})




def profile(request,userphone):
	if request.session.get('is_login',False):
		try:
			user = People.objects.get(phone=userphone)
		except:
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request,'profile.html',{'user':user})
	else:
		return HttpResponseRedirect(reverse('index'))



def logout(request):
	del request.session['is_login']
	return HttpResponseRedirect(reverse('index')) 


def regist(request):
	classname = request.session.get('myclass',False)
	if classname:
		if request.method == 'POST':
			registform = RegistForm(request.POST,request.FILES)
			if registform.is_valid():
				try:
					People.objects.get(phone=registform.cleaned_data['phone'])
				except:
					student = People()
					student.name=registform.cleaned_data['name']
					student.phone=registform.cleaned_data['phone']
					student.home_addr=registform.cleaned_data['home_addr']
					student.work_addr=registform.cleaned_data['work_addr']
					student.company=registform.cleaned_data['company']
					student.profession=registform.cleaned_data['profession']
					student.is_married=registform.cleaned_data['is_married']
					student.photo=registform.cleaned_data['photo']
					student.myclass=MyClass.objects.get(name=classname)
					student.is_monitor=False
					student.save()
					del request.session['myclass']
					request.session['is_login']=True
					request.session['phone']=student.phone
					return render(request,'registsucess.html')
				else:
					del request.session['myclass']
					return render(request,'alreadyexist.html')
			else:
				return render(request,'registerror.html')
		else:
			registform=RegistForm()
			return render(request,'regist.html',{'registform':registform})
	else:
		return HttpResponseRedirect(reverse('index'))
	


def classprofile(request):
	if request.session.get('is_login',False):    
		userphone = request.session['phone']
		user=People.objects.get(phone=userphone)
		currentclass=user.myclass
		classprofile=currentclass.students.all()
		return render(request,'classprofile.html',{'classprofile':classprofile})
	else:
		return HttpResponseRedirect(reverse('index')) 
def createclass(request):
	return render(request,'createclass.html')
def about(request):
	return render(request,'about.html')

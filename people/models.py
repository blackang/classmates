#coding:utf8
from django.contrib import admin
from django.db import models
class MyClass(models.Model):
	name = models.CharField("班级名",max_length=10)
	password = models.CharField("暗号",max_length=30,blank='False')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "班级"
		verbose_name_plural = "班级"
class People(models.Model):
	is_monitor = models.BooleanField("班长",default=0)
	myclass=models.ForeignKey(MyClass,verbose_name="所属班级",on_delete=models.CASCADE,null=True,related_name='students')
	name = models.CharField("姓名",max_length=10,blank='False')
	phone = models.IntegerField("手机号",blank='False')
	home_addr = models.CharField("家庭住址",max_length=40,blank='False')
	work_addr = models.CharField("工作地址",max_length=40,blank='False')
	profession = models.CharField("从事行业",max_length=15,blank='False')
	company = models.CharField("公司/职位",max_length=16,blank='False')
	is_married = models.NullBooleanField("婚否 ")
	photo = models.ImageField("近期照片",upload_to='photo')
	create_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "同学"
		verbose_name_plural = "同学"
admin.site.register(People)
admin.site.register(MyClass)


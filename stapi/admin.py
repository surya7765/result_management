from django.contrib import admin
from stapi.models import Student,Subject, SubMarks

# Register your models here.

# create inline class

class SubMarksInline(admin.TabularInline):
  model = SubMarks
  extra = 0


class UserAdmin(admin.ModelAdmin):
  search_fields = ['user__username']

# # create superclass CategoryAdmin
class StudentAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Student Information',{'fields':['user','registration_number','class_name','father_name','mother_name','address','phone','email']}),
  ]
  inlines = [SubMarksInline]
  autocomplete_fields = ['user']
  list_display = ('user_name','registration_number','class_name','phone')
  list_filter = ['class_name']
  search_fields = ['registration_number','class_name','father_name','mother_name','address','phone','email']

  
  def user_name(self,obj):
    return obj.user.username

admin.site.register(Subject)
admin.site.register(Student,StudentAdmin)
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Cat
from .models import Dog
from .models import JangsaUser 

admin.site.site_header = 'Jangsa Animal Adoption'
admin.site.site_title  =  'Jangsa Animal Adoption admin site'
admin.site.index_title  =  'Jangsa Animal Adoption Admim'

class catAdmin(admin.ModelAdmin): 
    list_display = ('name', 'age', 'description', 'created') 

class dogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description', 'created') 
    
admin.site.register(Cat, catAdmin)  
admin.site.register(Dog, dogAdmin)
admin.site.register(JangsaUser)


# Register your models here. 

from django.contrib import admin

# Register your models here.


from shop.models import category,product




class Categoryadmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category, Categoryadmin)

class Productadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,Productadmin)




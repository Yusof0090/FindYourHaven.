from django.contrib import admin
from .models import Member
from .models import contact_model

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("full_name", "email",)
admin.site.register(Member, MemberAdmin,)
class contactAdmin(admin.ModelAdmin):
  list_display = ("fullname", "email",)
admin.site.register(contact_model, MemberAdmin,)
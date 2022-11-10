from django.contrib import admin
from .models import User
from django import forms

class UserForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = User
        fields = '__all__'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
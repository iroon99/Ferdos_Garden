from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterUserForm(forms.ModelForm):
    # Buttoms and fields settings and widgets
    first_name = forms.CharField(
        label = 'نام',
        error_messages = {'required':'این فیلد نمی تواند خالی باشد'},
        widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'نام خود را وارد کنید'})
    )

    last_name = forms.CharField(
        label = 'نام خانوادگی',
        error_messages = {'required':'این فیلد نمی تواند خالی باشد'},
        widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد کنید'})
    )

    username = forms.CharField(
        label = 'نام کاربری',
        error_messages = {'required':'این فیلد نمی تواند خالی باشد'},
        widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'نام کاربری مورد نظر خود را وارد کنید'})
    )

    password1 = forms.CharField(
        label = 'رمز عبور',
        error_messages = {'required':'این فیلد نمی تواند خالی باشد'},
        widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'پسورد خود را وارد کنید'})
    )

    password2 = forms.CharField(
        label = 'تکرار رمز عبور',
        error_messages = {'required':'این فیلد نمی تواند خالی باشد'},
        widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'پسورد خود را تکرار کنید'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    # Validation Methods
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 == password2:
            return password2
        else:
            raise ValidationError("خطای رمز عبور خالی یا غیر یکسان")
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise ValidationError("نام کربری نمی تواند کوچکتر از 4 کارکتر باشد")
        return username
    
class LoginUserForm(forms.Form):
    username = forms.CharField(
        label = 'نام کاربری',
        error_messages = {'required':'این فیلد نمی تواند خالی باشد'},
        widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'نام کاربری مورد نظر خود را وارد کنید'})
    )

    password = forms.CharField(
        label = 'رمز عبور',
        error_messages = {'required':'این فیلد نمی تواند خالی باشد'},
        widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'پسورد خود را وارد کنید'})
    )
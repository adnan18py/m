from django import forms

class LoginForm(forms.Form):
    
    username=forms.CharField(label='نام کاربری',widget=forms.TextInput(attrs={'class':'input100','placeholder':'نام کاربری'}))
    password=forms.CharField(label='رمز عبور',widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'رمز عبور'}))
    

class RegisteritonForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input100','placeholder':'نام کاربری'}))
    frist_name=forms.CharField(widget=forms.TextInput(attrs={'class':'input100','placeholder':'نام'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'input100','placeholder':'نام خوانوادگی'}))
    
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'input100','placeholder':'ایمیل'}))

    password=forms.CharField(label='رمز عبور',widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'رمز عبور'}))

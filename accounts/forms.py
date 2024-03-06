from django import forms

class LoginForm(forms.Form):
    
    username=forms.CharField(label='نام کاربری',widget=forms.TextInput(attrs={'class':'input100'}))
    password=forms.CharField(label='رمز عبور',required=False,widget=forms.PasswordInput(attrs={'class':'input100'}))
    

    
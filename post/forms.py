from django import forms



class CommentForm(forms.Form):
    data='comment'

    attrs={'class':'comment_input',"placeholder":'نظر خود را بنویسید'}
    attrs2={'class':'username_input',"placeholder":'نام و نام خوانوادگی'}
    name=forms.CharField(label='',widget=forms.TextInput(attrs=attrs2))
    text=forms.CharField(label='',widget=forms.Textarea(attrs=attrs))
    


class ReplyForm(forms.Form):
    attrs={'class':'reply_input'}
    text=forms.CharField(label=None,widget=forms.TextInput(attrs=attrs))





    
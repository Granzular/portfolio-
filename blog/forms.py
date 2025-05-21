from django import forms

class NameForm(forms.Form):
    website_url = forms.CharField(max_length=100)
    result = forms.CharField(widget=forms.Textarea)

class MessageForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


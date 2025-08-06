from django import forms

class NameForm(forms.Form):
    website_url = forms.CharField(max_length=100)
    result = forms.CharField(widget=forms.Textarea)

class MessageForm(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {
        "class" : "form-control text-input",
        "placeholder" : "Email",
        }
                                                       ) )
    message = forms.CharField(widget = forms.Textarea(attrs = {
        "class" : "form-control",
        "placeholder" : "Type a message"
        }
        ))


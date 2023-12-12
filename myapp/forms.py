from django import forms


class ContactForms (forms.Form):
    name = forms.CharField(
        label="Full name",
        widget=forms.TextInput(
            attrs={
                "id": "name",
                "class": "form-control valid",
                "placeholder": "Enter your name"
            }
        )
    )
    email = forms.EmailField(
        label="Your email",
        widget=forms.TextInput(
            attrs={
                "id": "email",
                "class": "form-control valid",
                "placeholder": "Enter your email"
            }
        )
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(
            attrs={
                "id": "subject",
                "class": "form-control",
                "placeholder": "Enter subject"
            }
        )
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={
                "id": "message",
                "class": "form-control w-100",
                "placeholder": "Your message",
                "cols": "30",
                "rows": "9",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Enter message'",
            }
        )
    )

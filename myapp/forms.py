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
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea())

from django import forms

class ChatbotForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
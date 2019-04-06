from django.contrib.auth.forms import UserCreationForm
from django import forms
from coders.models import UserProfile, Faqs

# class SignUpForm(ModelForm):
#     class Meta():
#         model = UserProfile
#         fields = ('name', 'username', 'password1', 'password2')
#         # fields = ('name', 'username')
#
#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)
#         self.fields['name'].label = 'Name'
#         self.fields['username'].label = 'Handle'
#         # self.fields['password1'].label = 'Password'
#         # self.fields['password2'].label = 'Confirm Password'

class UserProfileCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ('name', 'username', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(UserProfileCreationForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Name'
        self.fields['username'].label = 'Handle'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

class FAQForm(forms.ModelForm):
    class Meta:
        model = Faqs
        fields = ['question', 'answer']
        widgets = {
            'question':forms.Textarea(attrs={'class':'editable'}),
            'answer':forms.Textarea(attrs={'class':'editable'})
        }

    def __init__(self, *args, **kwargs):
        super(FAQForm, self).__init__(*args, **kwargs)

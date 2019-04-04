from django.contrib.auth.forms import UserCreationForm
from coders.models import UserProfile

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

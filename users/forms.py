from allauth.account.forms import SignupForm
from django import forms

class SignupForm(SignupForm):
    nickname = forms.CharField(
                label="닉네임",
                required=True,
                widget=forms.TextInput(attrs={'placeholder': '닉네임'})
                ) 

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.profile.nickname = self.cleaned_data["nickname"]
        user.save()
        return user

  
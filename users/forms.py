from allauth.account.forms import SignupForm
from django import forms
from .models import Profile

class SignupForm(SignupForm):
    nickname = forms.CharField(
                label="닉네임",
                required=True,
                widget=forms.TextInput(attrs={'placeholder': '닉네임'})
                ) 
    
    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('이미 존재하는 닉네임입니다.')
        return nickname

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.profile.nickname = self.cleaned_data["nickname"]
        user.save()
        return user

  
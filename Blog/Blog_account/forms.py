from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

Account = get_user_model()


class UserCreateForms(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True, max_length=30)
    surname = forms.CharField(required=True, max_length=30)

    class Meta:
        model = Account
        fields = ('username', 'email', 'name', 'surname', 'birth_date', 'city', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']
        user.birth_date = self.cleaned_data['birth_date']
        user.city = self.cleaned_data['city']
        if commit:
            user.save()
        return user


class UserReviewForm:
    review = forms.Textarea()

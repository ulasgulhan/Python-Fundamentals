
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# region Registration Form

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # email alanının boş geçilmesini engelledik
        self.fields['email'].required = True

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # register olmaya çalışan kullanıcının girdiği mail biricik olmalıdır. aşağıda onu temin ettik. Veri tabanında böyle bir mail var mı diye baktık. Bu mantığın aynısını username gibi biricik olmasını istediğiniz her alan için kullanabilirsiniz.
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is invalid')

        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long')

        return email

# endregion

# region Login Form

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)

# endregion

# region Update Profile Form

class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required = True

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # register olmaya çalışan kullanıcının girdiği mail biricik olmalıdır. aşağıda onu temin ettik. Veri tabanında böyle bir mail var mı diye baktık. Bu mantığın aynısını username gibi biricik olmasını istediğiniz her alan için kullanabilirsiniz.
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email is invalid')

        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long')

        return email

# endregion

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class MixinStyle:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(MixinStyle, UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'country', 'avatar', 'email')


class UserRegisterForm(MixinStyle, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

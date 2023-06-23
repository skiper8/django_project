from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views import generic

from users.forms import UserForm, UserRegisterForm
from users.models import User
from utils import send_activate_email


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:products_list')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(generic.CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:confirm_email')
    template_name = 'users/user_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        new_user = form.save()

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            send_activate_email(new_user)
            return redirect('users:confirm_email')
        context_data = {
            'form': form
        }
        return render(request, self.template_name, context_data)


class EmailActivate(generic.UpdateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:products_list')

    def verify(self, request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                code = form.cleaned_data.get("code")
                user = User.objects.get(code=code)
                user.is_active = True
                user.save()
                object = super().get_object()
                object.is_active = True
                object.save()
        else:
            form = UserRegisterForm()
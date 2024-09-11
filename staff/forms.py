from django import forms
from django.contrib.auth.forms import UserCreationForm

from staff.models import Staff
from django.contrib.auth.models import User, Group




class StaffForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "group"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()

        Staff.objects.create(user=user, group=self.cleaned_data["group"])
        return user

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'usable_password':
                continue
            self.fields[field].widget.attrs.update({"class": "form-control"})
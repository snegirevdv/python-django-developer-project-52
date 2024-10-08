from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from task_manager.core import consts
from task_manager.core.mixins import (
    LoginIsRequiredMixin,
    ProtectedDeletionMixin,
)
from task_manager.users import forms, models
from task_manager.users.mixins import OnlySelfUserCanEdit


class UserCreateView(SuccessMessageMixin, generic.CreateView):
    """User registration view."""

    form_class = forms.UserForm
    template_name: str = consts.Template.USER_CREATE_UPDATE.value
    success_url: str = reverse_lazy("login")
    success_message: str = consts.Message.SUCCESS_USER_CREATION.value


class UserUpdateView(
    LoginIsRequiredMixin,
    OnlySelfUserCanEdit,
    SuccessMessageMixin,
    generic.UpdateView,
):
    """User editing view."""

    model = models.User
    form_class = forms.UserForm
    template_name: str = consts.Template.USER_CREATE_UPDATE.value
    success_url: str = reverse_lazy("index")
    success_message: str = consts.Message.SUCCESS_USER_UPDATE.value


class UserDeleteView(
    LoginIsRequiredMixin,
    OnlySelfUserCanEdit,
    ProtectedDeletionMixin,
    SuccessMessageMixin,
    generic.DeleteView,
):
    """User deletion view."""

    model = models.User
    template_name: str = consts.Template.USER_DELETE.value
    success_url: str = reverse_lazy("index")
    success_message: str = consts.Message.SUCCESS_USER_DELETION.value
    deletion_error_message: str = consts.Message.FAILURE_USER_DELETE.value

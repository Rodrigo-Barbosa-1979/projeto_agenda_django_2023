from collections.abc import Mapping
from typing import Any
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Escreva aqui",
            }
        ),
        label="Primeiro nome",
        help_text="Texto de ajuda para seu usuário",
    )

    # def __init__(self, *args, **Kwargs):
    #     super().__init__(*args, **Kwargs)

    # self.fields["first_name"].widget.attrs.update({
    #     "class": "classe-a classe-b",
    #     "placeholder": "Escreva aqui",
    # })

    class Meta:
        model = Contact
        fields = "first_name", "last_name", "phone", "email", "description", "category",

        # widgets = {
        #     "first_name": forms.TextInput(
        #         attrs={
        #             "class": "classe-a classe-b",
        #             "placeholder": "Escreva aqui",
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        if first_name == last_name:
            msg = "Primeiro nome não pode ser igual ao segundo nome."

            self.add_error("first_name", msg)
            self.add_error("last_name", msg)

        # self.add_error(
        #     "first_name",
        #     ValidationError(
        #         "Mensagem de erro",
        #         code="invalid",
        #     )
        # )

        # self.add_error(
        #     "first_name",
        #     ValidationError(
        #         "Mensagem de erro 2",
        #         code="invalid",
        #     )
        # )

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        # raise ValidationError(
        #     "Mensagem do raise.",
        #     code="invalid",
        # )

        if first_name == "ABC":
            raise ValidationError(
                "ABC não é válido neste campo."
            )

        return first_name

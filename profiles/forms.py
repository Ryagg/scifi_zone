from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """Receive users default address"""

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """Add placeholders, remove labels"""
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_city": "City",
            "default_postcode": "Postcode",
            "default_state": "State",
            "default_country": "Country",
        }

        self.fields["default_street_address1"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False

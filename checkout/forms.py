from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "street_address1",
            "street_address2",
            "city",
            "postcode",
            "state",
            "country",
        )

    def __init__(self, *args, **kwargs):
        """Add placeholders, remove labels"""
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "city": "City",
            "postcode": "Postcode",
            "state": "State",
            "country": "Country",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False

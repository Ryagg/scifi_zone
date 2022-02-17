"""This module contains the form for the Actor class"""

from django import forms
from tickets.models import Actor

class ActorForm(forms.ModelForm):
    """Form needed to add or edit guests"""
    class Meta:
        """Inherits all fields from the actor model"""
        model = Actor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Name",
            "star_autograph_category": "Star Autograph Category",
            "star_photoshoot_category": "Star Photoshoot Category",
            "star_image_url": "Star Image URL",
            "star_image": "Star Image",
            "star_info_1": "Short SciFi related summary",
            "star_info_2": "Info without SciFi reference",
            "star_imdb": "Link to IMDb entry for guest",
            "star_wiki": "Link to Wikipedia entry for guest",
            "star_official": "Link to official homepage for guest",
        }

        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = 'custom-form input'
            self.fields[field].label = False
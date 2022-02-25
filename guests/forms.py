"""This module contains the form for the Actor class"""

from django import forms
from tickets.models import Actor


class ActorForm(forms.ModelForm):
    """Form needed to add or edit guests"""
    class Meta:
        """Inherits all fields from the actor model"""
        model = Actor
        fields = (
            'name',
            'star_autograph_category',
            'star_photoshoot_category',
            'star_image',
            'star_info_1',
            'star_info_2',
            'star_imdb',
            'star_wiki',
            'star_official')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Name",
            "star_autograph_category": "Star Autograph Category \
                (A-C case-sensitve)",
            "star_photoshoot_category": "Star Photoshoot Category \
                (A-C case-sensitve)",
            "star_image": "Image",
            "star_info_1": "SciFi related info",
            "star_info_2": "Info without SciFi reference",
            "star_imdb": "Link to IMDb entry for guest",
            "star_wiki": "Link to Wikipedia entry for guest",
            "star_official": "Link to official homepage for guest",
        }

        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = 'custom-form input'
            self.fields[field].label = False
            if self.fields[field] != "star_image":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                    self.fields[field].widget.attrs[
                        "placeholder"] = placeholder

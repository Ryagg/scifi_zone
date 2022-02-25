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
        # not very DRY, but the only way to prevent error for placeholder
        # on file input field and have placeholders on all other fields
        self.fields["name"].widget.attrs.update(
            {"placeholder": "Name"},
        )
        self.fields["star_autograph_category"].widget.attrs.update(
            {"placeholder": "Star Autograph Category (A-C, case-sensitve)"}
        )
        self.fields["star_photoshoot_category"].widget.attrs.update(
            {"placeholder": "Star Photoshoot Category (A-C, case-sensitve)"}
        )
        self.fields["star_info_1"].widget.attrs.update(
            {"placeholder": "SciFi related info"}
        )
        self.fields["star_info_2"].widget.attrs.update(
            {"placeholder": "Info without SciFi reference"}
        )
        self.fields["star_imdb"].widget.attrs.update(
            {"placeholder": "Link to IMDb entry for guest"}
        )
        self.fields["star_wiki"].widget.attrs.update(
            {"placeholder": "Link to Wikipedia entry for gues"}
        )
        self.fields["star_official"].widget.attrs.update(
            {"placeholder": "Link to official homepage for guest"}
        )

        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = 'custom-form input'
            self.fields[field].label = False

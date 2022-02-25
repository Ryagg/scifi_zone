# pylint: disable=locally-disabled, no-member, redefined-outer-name
"""This module contains all form tests for the guests app."""
import pytest

from guests.forms import ActorForm


@pytest.mark.django_db
# marking test as expecting to fail
@pytest.mark.xfail(reason='actor will not be created without required data')
def test_actor_form_is_not_valid_without_required_data():
    """Verify that the form is not valid without required data"""
    data = {
        'name': "somebody"
    }
    form = ActorForm(data=data)
    form.save()
    assert True is form.is_valid()


@pytest.mark.django_db
def test_actor_form_is_valid_with_data(create_guest):
    """Verify that the form with data is valid"""
    data = {
        'name': create_guest.name,
        'star_autograph_category': create_guest.star_autograph_category,
        'star_photoshoot_category': create_guest.star_photoshoot_category,
        'star_image': create_guest.star_image,
        'star_info_1': create_guest.star_info_1,
        'star_info_2': create_guest.star_info_2,
        'star_imdb': create_guest.star_imdb,
        'star_wiki': create_guest.star_wiki,
        'star_official': create_guest.star_official
    }

    form = ActorForm(data=data)
    form.save()

    assert True is not None
    assert True is form.is_valid()

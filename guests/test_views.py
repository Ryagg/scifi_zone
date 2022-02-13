# pylint: disable=locally-disabled, no-member, redefined-outer-name
"""This module contains all tests for views from the guests app."""
import pytest

from django.shortcuts import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains

@pytest.mark.new
@pytest.mark.django_db
def test_page_url_works(client, actor_data):
    """Verify that the page renders as expected"""
    url = reverse('guests')
    for actor in actor_data:
        response = client.get(url)
        assert response.status_code == 200
        assertContains(response, actor.id)


@pytest.mark.new
@pytest.mark.django_db
def test_page_url_with_parameter_works(client, actor_data):
    """Verify that the pages render as expected"""
    for actor in actor_data:
        response = client.get('guests/actor.id')
        assert response.status_code == 200
        assertContains(response, actor.name)

@pytest.mark.new
@pytest.mark.django_db
def test_uses_correct_template_to_render_a_view(client):
    """Test the view uses the correct template"""
    url = reverse('guests')
    response = client.get(url)
    assertTemplateUsed(response, 'guests/guests.html')

@pytest.mark.new
@pytest.mark.django_db
def test_page_with_parameters_uses_correct_template(client, actor_data):
    """Test the view uses the correct template"""
    for actor in actor_data:
        response = client.get('guests/actor.id')
        assertTemplateUsed(response, 'guests/guest_detail.html')
        assertContains(response, actor.star_image_url)

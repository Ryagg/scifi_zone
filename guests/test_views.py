# pylint: disable=locally-disabled, no-member, redefined-outer-name
"""This module contains all tests for views from the guests app."""
import pytest
from django.shortcuts import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains


@pytest.mark.new
@pytest.mark.django_db
def test_page_url_works(client, actor_data):
    """Verify that the page renders as expected"""
    url = reverse("guests")
    for actor in actor_data:
        response = client.get(url)
        assert response.status_code == 200
        assertContains(response, actor.id)


@pytest.mark.new
@pytest.mark.django_db
def test_page_url_with_parameter_works(client, actor_data):
    """Verify that the pages render as expected"""
    for actor in actor_data:
        response = client.get("guests/actor.id")
        assert response.status_code == 200
        assertContains(response, actor.name)


@pytest.mark.new
@pytest.mark.django_db
def test_uses_correct_template_to_render_a_view(client):
    """Test the view uses the correct template"""
    url = reverse("guests")
    response = client.get(url)
    assertTemplateUsed(response, "guests/guests.html.jinja")


@pytest.mark.new
@pytest.mark.django_db
def test_page_with_parameters_uses_correct_template(client, actor_data):
    """Test the view uses the correct template"""
    for actor in actor_data:
        response = client.get("guests/actor.id")
        assertTemplateUsed(response, "guests/guest_detail.html.jinja")
        assertContains(response, actor.star_image_url)


@pytest.mark.new
@pytest.mark.django_db
def test_add_guest_page_not_accessible_for_unauthenticated_users(
    client, user_data
):
    """Verify that the page returns an error message for
    unauthenticated users"""
    url = reverse("add_guest")
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.new
@pytest.mark.django_db
def test_add_guest_page_not_accessible_for_non_superusers(
    client, authenticated_user
):
    """Verify that the page returns an error message for
    authenticated users who are not superusers"""
    url = reverse("add_guest")
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.new
# django_db() mark not needed for admin_client fixture
def test_add_guest_page_accessible_for_superusers(admin_client):
    """Verify that the page renders as expected for superusers"""
    url = reverse("add_guest")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_add_guest_works(admin_client):
    """Verify that added guests appear on the home and guests pages"""
    data = {
        "name": "John Doe",
        "star_autograph_category": "C",
        "star_photoshoot_category": "C",
        "star_image_url": "",
        "star_image": "",
        "star_info_1": "Info",
        "star_info_2": "More info",
        "star_imdb": "",
        "star_wiki": "",
        "star_offical": "",
    }
    url = reverse("add_guest")
    admin_client.post(url, data)
    guests = reverse("guests")
    update = admin_client.get(guests)
    home = admin_client.get("/")
    assertContains(update, "John Doe")
    assertContains(home, "John Doe")

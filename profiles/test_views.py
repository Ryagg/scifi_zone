# pylint: disable=locally-disabled, no-member, redefined-outer-name
"""This module contains all tests for views from the profiles app."""

import pytest

from django.shortcuts import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains

@pytest.mark.new
@pytest.mark.django_db
def test_profile_page_not_accessible_for_unauthenticated_users(
    client, user_data):
    # user_data passed to show that the user needs to be logged in
    """Verify that the page returns an error message for
    unauthenticated users"""
    url = reverse('profile')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.new
@pytest.mark.django_db
def test_profile_page_accessible_for_authenticated_users(
    client, authenticated_user):
    """Verify that authenticated users can view the page"""
    url = reverse('profile')
    response = client.get(url)
    assert response.status_code == 200
    assertContains(response, "Order History")

@pytest.mark.new
@pytest.mark.django_db
def test_profile_pages_uses_correct_template(client, authenticated_user):
    url = reverse('profile')
    response = client.get(url)
    assertTemplateUsed(response, 'profiles/profile.html')

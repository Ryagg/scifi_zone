# pylint: disable=locally-disabled, no-member, redefined-outer-name
"""This module contains all tests for views from the find app."""
import pytest

from django.shortcuts import reverse


@pytest.mark.django_db
def test_page_url_works(client):
    """Verify that the find page renders as expected"""
    user_query = "lancie"
    url = reverse('search_results')
    query = url + '?q=' + user_query
    response = client.get(query)
    assert response.status_code == 200

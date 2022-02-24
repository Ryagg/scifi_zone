# pylint: disable=locally-disabled, no-member, redefined-outer-name
"""This module contains all tests for views from the checkout app."""
import pytest

from django.shortcuts import reverse


@pytest.mark.parametrize('templates', [
    ('checkout')
])
@pytest.mark.new
@pytest.mark.django_db
def test_checkout_with_empty_bag(client, templates):
    """
    Verify that the page cannot be accessed when the bag is empty
    """
    url = reverse(templates)
    response = client.get(url)
    assert response.status_code == 302

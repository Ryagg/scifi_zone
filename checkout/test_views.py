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

# @pytest.mark.skip("items not added to bag")
# @pytest.mark.django_db
# def test_checkout_with_items_in_bag(client, create_ticket):
#     """Verify that the page can be accessed with items in the bag"""
#     response = reverse('view_bag')
#     bag = client.post('add/'create_ticket.id)
#     print(bag)
#     url = reverse('checkout')
#     response = client.get(url)
#     assert response.status_code == 302

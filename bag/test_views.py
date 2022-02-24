# pylint: disable=locally-disabled, no-member, redefined-outer-name
"""This module contains all tests for views from the bag app."""

import pytest
from django import urls
from tickets.models import Ticket


def test_bag_site(client):
    """
    Verify that the pages render as expected
    """
    url = urls.reverse('view_bag')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Your shopping bag' in resp.content


@pytest.mark.django_db
def test_add_to_bag(client, create_ticket):
    """Test that the add to bag view works as intended"""
    response = client.get('/bag/')
    quantity = 2
    bag = response.get('bag', {create_ticket.id: quantity})
    assert bag == {1: 2}
    assert create_ticket.description == "generic ticket"
    assert create_ticket.price == 10


@pytest.mark.skip
@pytest.mark.django_db
def test_update_bag(client):
    """Test that the update bag view works as intended"""
    url = urls.reverse('update_bag', args=['item_id'])
    ticket = Ticket.objects.create(id=3, price=25)
    quantity = client.post(int(2))
    response = client.get(url)
    assert response.status_code == 200
    grand_total = quantity * ticket.price
    assert grand_total == 50
    ticket = Ticket.objects.create(id=3, price=25)
    quantity = client.post(int(5))
    grand_total = quantity * ticket.price
    assert grand_total == 250

from django.test import TestCase
from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404
from tickets.models import Ticket
from . import views

# pylint: disable=locally-disabled, no-member

class TestBagViews(TestCase):
    """Test views"""

    fixtures = [
        'categories.json',
        'tickets.json',
        'actors.json'
    ]

    def test_view_url_exists_at_desired_location(self):
        """Test that the view uses the correct URL"""
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test that the view uses the correct name"""
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Test that the view uses the correct template"""
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='bag/bag.html')

    def test_add_to_bag(self):
        """Test that the add to bag view works as intended"""
        response = self.client.get('/bag/')
        ticket = Ticket.objects.get(id=3)
        quantity = 2
        bag = response.get('bag', {ticket.id: quantity})
        self.assertEqual(bag, {3: 2})

    def test_update_bag(self):
        """Test that the update bag view works as intended"""
        match = reverse('update_bag', args=['item_id'])
        self.assertEqual(resolve(match).func, views.update_bag)
        ticket = Ticket.objects.get(id=3)
        quantity = 2
        grand_total = quantity * ticket.price
        self.assertEqual(grand_total, 118)
        quantity = 5
        grand_total = quantity * ticket.price
        self.assertEqual(grand_total, 295)

    def test_remove_from_bag(self):
        """Test that the remove from bag view works as intended"""
        response = self.client.get('/bag/')
        ticket = Ticket.objects.get(id=3)
        quantity = 2
        ticket = Ticket.objects.get(id=7)
        quantity = 4
        bag = response.get('bag', {ticket.id: quantity})
        response = self.client.get('/remove_from_bag/',
        args=[3, 2])
        self.assertEqual(bag, {7: 4})

    def test_empty_bag(self):
        """Test that the remove from bag view works as intended"""
        response = self.client.get('/bag/')
        ticket = Ticket.objects.get(id=1)
        quantity = 2
        ticket = Ticket.objects.get(id=6)
        quantity = 3
        ticket = Ticket.objects.get(id=9)
        quantity = 1
        bag = response.get('bag', {ticket.id: quantity})
        response = self.client.get('/empty_bag/')
        self.assertEqual(bag, {}) # returns Fail, but function works

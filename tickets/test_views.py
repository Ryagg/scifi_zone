# pylint: disable=locally-disabled, no-member, redefined-outer-name
"""This module contains all tests for views from the tickets app."""
import pytest

from django.shortcuts import reverse
from pytest_django.asserts import assertContains


@pytest.mark.new
@pytest.mark.django_db
def test_page_url_works(client, ticket_data):
    """Verify that the ticket pages render as expected"""
    url = reverse('tickets')
    for ticket in ticket_data:
        response = client.get(url)
        assert response.status_code == 200
        assertContains(response, ticket.id)


@pytest.mark.new
@pytest.mark.django_db
def test_ticket_page_with_parameter_works(client, ticket_data):
    """Verify that the ticket detail pages render as expected"""
    for ticket in ticket_data:
        response = client.get('tickets/ticket.id')
        assert response.status_code == 200
        assertContains(response, ticket.name)


@pytest.mark.new
@pytest.mark.django_db
def test_addon_pages_work(client, ticket_data):
    """Verify that the ticket-addon pages render as expected"""
    for ticket in ticket_data:
        if "Standard" not in ticket.name:
            response = client.get('tickets/ticket.id')
            assert response.status_code == 200
            assertContains(response, "Category")


@pytest.mark.new
@pytest.mark.django_db
def test_packages_page_works(client, package_data):
    """Verify that the package page renders as expected"""
    for package in package_data:
        response = client.get('tickets/packages')
        assert response.status_code == 200
        assertContains(response, package.id)


@pytest.mark.new
@pytest.mark.django_db
def test_package_page_with_parameter_works(client, package_data):
    """Verify that the package detail pages render as expected"""
    for package in package_data:
        response = client.get('tickets/package.id/package.name')
        assert response.status_code == 200
        assertContains(response, package.name)

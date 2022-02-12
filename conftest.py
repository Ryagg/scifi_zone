# pylint: disable=W, C, R, no-member
import imp
import pytest

from django.contrib.auth.models import User
from checkout.models import Order
from tickets.models import Ticket

@pytest.fixture
def user_data():
	return {
    'email': 'user_email',
    'username': 'user_name',
    'password': 'user_password12345'
    }

@pytest.fixture
def create_test_user(user_data):
	test_user = User.objects.create_user(**user_data)
	test_user.set_password(user_data.get('password'))
	return test_user

@pytest.fixture
def authenticated_user(client, user_data):
	test_user = User.objects.create_user(**user_data)
	test_user.set_password(user_data.get('password'))
	test_user.save()
	client.login(**user_data)
	return test_user

@pytest.fixture
def ticket_data():
    ticket = Ticket.objects.create(
        id=1,
        name="Test ticket",
        description="generic ticket",
        price=10
    )
    return ticket

@pytest.fixture
def order_data():
    order = Order.objects.create(
        order_number="123",
        email="userone@test.com",
        sub_total=25,
        grand_total=199
    )
    return order

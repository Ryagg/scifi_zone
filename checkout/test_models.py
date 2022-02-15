# pylint: disable=W, C, R, no-member
import pytest

from django.contrib.auth.models import User

from .models import Order


@pytest.mark.django_db
@pytest.fixture()
def order_data():
    # Set up order used by all test methods
    order = Order.objects.create(
        order_number="123",
        email="userone@test.com",
        sub_total=25,
        grand_total=199
    )
    return order

@pytest.mark.django_db
@pytest.mark.custom_model
def test_model_labels(order_data):
    assert order_data.order_number == "123"
    assert order_data.email == "userone@test.com"
    assert order_data.sub_total == 25
    assert order_data.grand_total == 199

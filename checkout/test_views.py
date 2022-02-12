import pytest

from django import urls
from django.contrib.auth.models import User

@pytest.mark.parametrize('templates', [
    ('checkout')

])

@pytest.mark.new
@pytest.mark.django_db
@pytest.mark.xfail
def test_views(client, templates):
    """
    Verify that the pages render as expected
    """
    url = urls.reverse(templates)
    resp = client.get(url)
    # checkout not accessible with an empty bag
    assert resp.status_code == 200

import pytest

from django.shortcuts import reverse

from pytest_django.asserts import assertTemplateUsed

@pytest.mark.parametrize('templates', [
    ('home')
])

@pytest.mark.django_db
def test_home_page_url_works(client, templates):
    """Verify that the pages render as expected"""
    url = reverse(templates)
    response = client.get(url)
    assert response.status_code == 200

# separate test for home page due to different names for view and name

@pytest.mark.django_db
def test_home_page_uses_correct_template(client):
    """Test the view uses the correct template"""
    response = client.get('/')
    assertTemplateUsed(response, 'home/index.html')

# test for all pages except 'home'
# @pytest.mark.parametrize('templates', [
#     ('home') # remove later and replace with remaining templates from view
# ])

# @pytest.mark.parametrize('names', [
#     ('home') # see above
# ])

# @pytest.mark.new
# @pytest.mark.django_db
# def test_uses_correct_template_to_render_a_view(client, templates, names):
#     """Test the view uses the correct template"""
#     url = reverse(templates)
#     response = client.get(url)
#     assertTemplateUsed(response, f'{templates}/{names}.html')

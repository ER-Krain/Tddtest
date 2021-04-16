from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):
    
    def test_root_url_resolve_to_home_page_view(self):
        #found = resolve('/')
        response = self.client.get('/')
        #self.assertEqual(found.func, home_page)
        self.assertTemplateUsed(response, 'home.html')

    #def test_home_page_returns_correct_html(self):
        ##request = HttpRequest()
        #response = self.client.get('/') #1
        ##response = home_page(request) 
        #html = response.content.decode('utf8') #2
        #self.assertTrue(html.startswith('<html>')) 
        #self.assertIn('<title>To-Do lists</title>', html) 
        #self.assertTrue(html.strip().endswith('</html>'))
        #self.assertTemplateUsed(response,'home.html') #3

# Create your tests here.

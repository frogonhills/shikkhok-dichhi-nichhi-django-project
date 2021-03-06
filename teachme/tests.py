# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import teachers , StudentPost
from . import views


class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/teachme/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/teachme/')
        self.assertContains(response, '<h1>শিক্ষক দিচ্ছি-নিচ্ছি!</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/teachme/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
            
            
     
   



class PostTests(TestCase):

       
            
    def setUp(self):
        StudentPost.objects.create(Spost='tase case')            
    
    
    
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
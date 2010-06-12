"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from django.test import Client, TestCase
from django.contrib.auth.models import User
from grid.models import *

class ApiTest(TestCase):

    def setUp(self):
        u = User.objects.create_user('test', 'test@test.com', 'test')
        d = Design.objects.create(slug='tshirt', name= 'T Shirt')

    def test_post(self):
        e_h  = rand_bool_seq()
        e_v  = rand_bool_seq()
        d_sw = rand_bool_seq()
        d_se = rand_bool_seq()
        post_data = {
                'edge_h'  : e_h,
                'edge_v'  : e_v,
                'diag_sw' : d_sw,
                'diag_se' : d_se,
                }
        login = self.client.login(username='test', password='test')
        self.failUnless(login, 'Could not login')
        response = self.client.post('/grid/api/tshirt/', post_data)
        self.assertEqual(response.status_code, 200)
        d = Design.objects.last()
        delta = d.deltas.last()
        self.assertEqual(delta.e_h, e_h)
        self.assertEqual(delta.user, User.objects.get(username='test'))
        

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

def rand_bool_seq(length=256):
    import random
    l = ''
    for i in range(length):
        if random.random() > .5: l + '1'
        else: l + '0'
    return l

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}


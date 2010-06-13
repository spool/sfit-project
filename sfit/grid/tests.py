"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from django.test import Client, TestCase
from django.contrib.auth.models import User
from grid.models import *
import random

class ApiTest(TestCase):

    def setUp(self):
        self.u = User.objects.create_user('test', 'test@test.com', 'test')
        self.d = Design.objects.create(slug='tshirt', name= 'T Shirt')
        self.e_h  = rand_bool_seq(4096)
        self.e_v  = rand_bool_seq(4096)
        self.d_sw = rand_bool_seq(4096)
        self.d_se = rand_bool_seq(4096)
        self.cell = random.randint(0,63)
        self.post_data = {
                'edges_h': self.e_h,
                'edges_v': self.e_v,
                'diag_sw': self.d_sw,
                'diag_se': self.d_se,
                'cell'   : self.cell,
                }

    def testShortPost(self):
        login = self.client.login(username='test', password='test')
        self.failUnless(login, 'Could not login')
        post_data = self.post_data
        post_data['edges_h'] = rand_bool_seq()
        response = self.client.post('/grid/api/tshirt/', self.post_data)
        self.assertEqual(response.status_code, 400)

    def testPost(self):
        login = self.client.login(username='test', password='test')
        self.failUnless(login, 'Could not login')
        response = self.client.post('/grid/api/tshirt/', self.post_data)
        self.assertEqual(response.status_code, 200)
        d = Design.objects.get(slug='tshirt')
        delta = d.deltas.last()
        self.assertEqual(delta.edges_h, self.e_h)
        self.assertEqual(delta.user, User.objects.get(username='test'))

    def testRepeatEdit(self):
        login = self.client.login(username='test', password='test')
        self.failUnless(login, 'Could not login')
        response = self.client.post('/grid/api/tshirt/', self.post_data)
        self.assertEqual(response.status_code, 200)
        

        


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

def rand_bool_seq(length=256):
    l = ''
    for i in range(length):
        if random.random() > .5: l += '1'
        else: l += '0'
    return l

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}


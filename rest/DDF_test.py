from django.test import TestCase
from companies.models import Company
from django_dynamic_fixture import G, P

class TestDrf(TestCase):

    '''DJANGO DYNAMIC FEATURES - DDF'''
    def test_new_feature_g(self):
        instance = G(Company, name="Tangent Tech", project_root="C:", source_root="D:", render_root="E:", 
                        created = '2019-06-17T19:52:12.233747Z', modified = '2019-06-17T19:52:12.233747Z')
        print("instance name: ", instance.name)
        self.assertEqual(instance.project_root, "C:")
    
    def test_new_feature_f(self):
        P(G(Company))

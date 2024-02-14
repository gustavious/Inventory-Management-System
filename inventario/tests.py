from django.test import TestCase
from django.urls import reverse
from .models import Equipo
from django.contrib.auth.models import User

class EquipoModelTest(TestCase):
    def setUp(self):
        self.equipo = Equipo.objects.create(
            referencia='123ABC',
            marca='Apple Super Beauty',
            procesador='Intel i7',
            memoria='8GB',
            disco='256GB SSD',
            tipo='Laptop'
        )

    def test_equipo_model(self):
        self.assertEqual(self.equipo.referencia, '123ABC')
        self.assertEqual(self.equipo.marca, 'Apple Super Beauty')
        self.assertEqual(self.equipo.procesador, 'Intel i7')
        self.assertEqual(self.equipo.memoria, '8GB')
        self.assertEqual(self.equipo.disco, '256GB SSD')
        self.assertEqual(self.equipo.tipo, 'Laptop')


class EquipoListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.equipo = Equipo.objects.create(
            referencia='123ABC',
            marca='Apple Super Beauty',
            procesador='Intel i7',
            memoria='8GB',
            disco='256GB SSD',
            tipo='Laptop'
        )

    def test_equipo_list_view(self):
        response = self.client.get(reverse('equipo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123ABC')
        self.assertContains(response, 'Apple Super Beauty')
        self.assertContains(response, 'Laptop')

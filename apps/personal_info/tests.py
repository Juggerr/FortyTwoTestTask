from datetime import date

from django.test import TestCase
from django.test import Client

from .models import PersonalInfo


class TestMainPage(TestCase):

    def setUp(self):
        self.test_name = "Igor"
        self.test_email = "lyakhigor@gmail.com"

        PersonalInfo.objects.create(
            name=self.test_name,
            last_name="Lyakh",
            birth_date=date(1992, 03, 31),
            bio="""Liseum 22 1998-2007
            Chernihiv Radio-machanical collage 2007-2011
            Chernihiv State Technological University 2011-2016""",
            contacts="""Ukraine, Chernihiv, Rokossovsky str. 37a, 42.
            phone: +380936536892""",
            email=self.test_email,
            jabber="lyakhigor@42cc.co",
            skype="Juggerr",
            other="Some other contacts"
        )

        self.client = Client()

    def test_correct_content(self):
        """Test is site main page contains correct content"""
        response = self.client.get('/')
        self.assertContains(response, "42 Coffee Cups Test Assignment")
        self.assertContains(response, self.test_name)
        self.assertContains(response, self.test_email)

    def test_base_query(self):
        """Test base query"""
        personal_info = PersonalInfo.objects.last()
        self.assertEqual(personal_info.name, self.test_name)

    def test_two_records(self):
        """Test when table contains more than one record"""

        test_second_name = "Second name"

        PersonalInfo.objects.create(
            name=test_second_name,
            last_name="Lyakh",
            birth_date=date(1992, 03, 31),
            bio="""Liseum 22 1998-2007
            Chernihiv Radio-machanical collage 2007-2011
            Chernihiv State Technological University 2011-2016""",
            contacts="""Ukraine, Chernihiv, Rokossovsky str. 37a, 42.
            phone: +380936536892""",
            email=self.test_email,
            jabber="lyakhigor@42cc.co",
            skype="Juggerr",
            other="Some other contacts"
        )

        personal_info = PersonalInfo.objects.last()
        self.assertEqual(personal_info.name, test_second_name)

    def test_no_records(self):
        """Test when there is no records"""

        PersonalInfo.objects.all().delete()

        response = self.client.get('/')
        self.assertContains(response, "There is no data yet")

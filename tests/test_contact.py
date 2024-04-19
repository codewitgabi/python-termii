"""
Contacts API allows you manage (i.e. edit, update, & delete) contacts in your phonebook.
"""

# imports

import os
from src.termii.termii import Termii
from unittest import TestCase


class TestContacts(TestCase):
    def setUp(self) -> None:
        self.termii = Termii(api_key=os.environ.get("TERMII_API_KEY"))
        self.sender_id = os.environ.get("TERMII_SENDER_ID")

    def test_get_contacts(self):
        res = self.termii.get_contact("11f390d2-8bd6-48dd-9f9f-65a3e2b2267b")

        self.assertIn("data", res)

    def test_add_contact(self):
        res = self.termii.add_contact(
            "11f390d2-8bd6-48dd-9f9f-65a3e2b2267b", "7026983249", country_code="234")

        self.assertIn("data", res)

    def test_delete_contact(self):
        res = self.termii.delete_contact(
            42142587)

        self.assertDictEqual(res, {"message": "Contact deleted successfully"})

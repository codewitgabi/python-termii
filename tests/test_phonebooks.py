"""
Create, view & manage phonebooks using these APIs. Each phonebook can be identified by a unique ID, which makes it easier to edit or delete a phonebook.
"""

# imports

import os
from unittest import TestCase
import unittest
from termii import Termii


class TestPhonebook(TestCase):
    def setUp(self) -> None:
        self.termii = Termii(api_key=os.environ.get("TERMII_API_KEY"))
        self.sender_id = os.environ.get("TERMII_SENDER_ID")

    @unittest.expectedFailure
    def test_create_phonebook_with_description(self):
        res = self.termii.create_phonebook(
            "Phone", "My test phonebook")

        self.assertDictEqual(res, {
            "message": "Phonebook added successfully"
        })

    @unittest.expectedFailure
    def test_create_phonebook_without_description(self):
        res = self.termii.create_phonebook("Phone2")

        self.assertDictEqual(res, {
            "message": "Phonebook added successfully"
        })

    def test_create_phonebook_already_exists(self):
        res = self.termii.create_phonebook("Phone")
        res2 = self.termii.create_phonebook("Phone2")

        self.assertDictEqual(res, {'message': 'Phonebook name already exist'})
        self.assertDictEqual(res2, {'message': 'Phonebook name already exist'})

    def test_get_phonebooks(self):
        res = self.termii.get_phonebooks()

        self.assertIn("data", res)

    def test_update_phonebook(self):
        res = self.termii.delete_phonebook(
            "c180920c-8bd0-40c8-8ad2-47a77379ab54")

        self.assertDictEqual(
            res, {'message': 'Phone Book Has been Updated Successfully'})

    @unittest.expectedFailure
    def test_delete_phonebook(self):
        res = self.termii.delete_phonebook(
            "c180920c-8bd0-40c8-8ad2-47a77379ab54")

        self.assertDictEqual(
            res, {'message': 'Phone Book Has been Deleted Successfully'})

    def test_delete_phonebook_does_not_exist(self):
        res = self.termii.delete_phonebook(
            "c180920c-8bd0-40c8-8ad2-47a77379ab54")

        self.assertDictEqual(
            res, {'message': 'Phonebook does not exist'})

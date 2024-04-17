"""
This API allows businesses send messages to customers using Termii's auto-generated messaging numbers that adapt to customers location.
"""

# imports

import os
from unittest import TestCase
from termii import Termii


class TestNumberAPI(TestCase):
    def setUp(self) -> None:
        self.sender_id = os.environ.get("TERMII_SENDER_ID")
        self.termii = Termii(api_key=os.environ.get(
            "TERMII_API_KEY"), sender_id=self.sender_id)

    def test_send_message(self):
        res = self.termii.send_auto_message(
            ["2349020617734", "2347026983249"], "This is an auto message test.")

        self.assertIn("code", res)
        self.assertIn("message_id", res)
        self.assertIn("message", res)
        self.assertIn("balance", res)
        self.assertIn("user", res)

    def test_country_inactive_error(self):
        """This error occurs when a country is inactive"""

        res = self.termii.send_auto_message(
            ["2349020617734", "2347026983249"], "This is an auto message test.")

        self.assertDictEqual(
            res, {'message': 'Country Inactive. Contact Administrator to activate country.'})

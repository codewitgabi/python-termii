"""
The Balance API returns your total balance and balance information from your wallet, such as currency.
"""

# imports

import os
from unittest import TestCase
from src.termii.termii import Termii


class TestInsights(TestCase):
    def setUp(self) -> None:
        self.sender_id = os.environ.get("TERMII_SENDER_ID")
        self.termii = Termii(api_key=os.environ.get(
            "TERMII_API_KEY"), sender_id=self.sender_id)

    def test_get_balance(self):
        res = self.termii.get_balance()

        self.assertIn("user", res)
        self.assertIn("balance", res)
        self.assertIn("currency", res)

    def test_verify_phone_number(self):
        res = self.termii.verify_phone_number("2349020617734")

        self.assertEqual(res.get("number"), "2349020617734")
        self.assertIn("status", res)
        self.assertIn("network", res)
        self.assertIn("network_code", res)

        res2 = self.termii.verify_phone_number("2347026983249")

        self.assertEqual(res2.get("number"), "2347026983249")
        self.assertIn("status", res2)
        self.assertIn("network", res2)
        self.assertIn("network_code", res2)

    def test_history(self):
        res = self.termii.history()

        self.assertIsInstance(res, dict)
        self.assertIn("data", res)
        self.assertIsInstance(res.get("data"), list)

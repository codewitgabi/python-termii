import os
from unittest import TestCase
from src.termii.termii import Termii


class TestSenderID(TestCase):
    def setUp(self) -> None:
        self.termii = Termii(api_key=os.environ.get("TERMII_API_KEY"))

    def test_get_senderId(self):
        res = self.termii.get_senderId()

        self.assertIn("data", res)

    def test_request_senderId(self):
        res = self.termii.request_senderId(
            "Test", "I want to use this api for sending otp messages", "No company")

        self.assertDictEqual(
            {"code": "ok", "message": "Sender Id requested. You will be contacted by your account manager."}, res)

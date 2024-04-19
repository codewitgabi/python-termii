"""
The send token API allows businesses trigger one-time-passwords (OTP) across any available messaging channel on Termii. One-time-passwords created are generated randomly and there's an option to set an expiry time.
"""

# imports

import os
from unittest import TestCase
from src.termii.termii import Termii


class TestToken(TestCase):
    def setUp(self) -> None:
        self.termii = Termii(api_key=os.environ.get("TERMII_API_KEY"))
        self.sender_id = os.environ.get("TERMII_SENDER_ID")
        self.email_configuration_id = os.environ.get(
            "TERMII_EMAIL_CONFIGURATION_ID")

    def test_send_token(self):
        res = self.termii.send_token(
            "NUMERIC", "2347026983249", self.sender_id, "generic", "Please verify your email")

        self.assertIn("pinId", res)
        self.assertIn("to", res)
        self.assertEqual(res.get("smsStatus"), "Message Sent")
        self.assertEqual(res.get("status"), 200)

    def test_voice_token(self):
        res = self.termii.voice_token("2347026983249", 4, 15, 6)

        self.assertEqual(res.get("code"), "ok")
        self.assertIn("pin_id", res)
        self.assertEqual(res.get("message"), "Successfully Sent")
        self.assertIn("balance", res)

    def test_voice_call(self):
        res = self.termii.voice_call("2347026983249", "449521")

        self.assertEqual(res.get("code"), "ok")
        self.assertEqual(res.get("message"), "Successfully Sent")

    def test_email_token(self):
        res = self.termii.email_token(
            "test@example.com", "458832", self.email_configuration_id)

        self.assertEqual(res.get("code"), "ok")
        self.assertEqual(res.get("message"), "Successfully Sent")

    def test_verify_token(self):
        res = self.termii.verify_token(
            "c8dcd048-5e7f-4347-8c89-4470c3af0b", "133945")

        self.assertEqual(res.get("verified"), "True")
        self.assertIn("msisdn", res)

    def test_generate_token(self):
        res = self.termii.generate_token("NUMERIC", "2347026983249", 4, 15, 6)

        self.assertEqual(res.get("status"), "success")
        self.assertIn("data", res)

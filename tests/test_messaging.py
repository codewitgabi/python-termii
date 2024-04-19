"""This API allows businesses send text messages to their customers across different messaging channels. The API accepts JSON request payload and returns JSON encoded responses, and uses standard HTTP response codes.
"""

# imports

import os
import unittest
from unittest import TestCase
from src.termii.termii import Termii


class TestMessaging(TestCase):
    def setUp(self) -> None:
        self.termii = Termii(api_key=os.environ.get("TERMII_API_KEY"))
        self.sender_id = os.environ.get("TERMII_SENDER_ID")

    def test_send_message(self):
        res = self.termii.send_message(self.sender_id, [
                                       "+2349020617734"], "plain", "generic", "Test SMS sent from termii-python-pkg")

        self.assertIn("message_id", res)
        self.assertIn("user", res)
        self.assertIn("balance", res)

    @unittest.expectedFailure    
    def test_send_whatsapp_message(self):
        res = self.termii.send_message(self.sender_id, [
                                       "+2349020617734"], "plain", "whatsapp", "Test SMS sent from termii-python-pkg to whatsapp", {"caption": "Caption from whatsapp media."})

        self.assertIn("message_id", res)
        self.assertIn("user", res)
        self.assertIn("balance", res)

    def test_whatsapp_device_404_error(self):
        res = self.termii.send_message(self.sender_id, [
                                       "+2349020617734"], "plain", "whatsapp", "Test SMS sent from termii-python-pkg to whatsapp", {"caption": "Caption from whatsapp media."})

        self.assertDictEqual(
            res, {'message': 'Device not found. Contact your account manager'})

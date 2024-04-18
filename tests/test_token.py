"""
The send token API allows businesses trigger one-time-passwords (OTP) across any available messaging channel on Termii. One-time-passwords created are generated randomly and there's an option to set an expiry time.
"""

# imports

import os
from unittest import TestCase
from termii import Termii


class TestToken(TestCase):
    def setUp(self) -> None:
        self.termii = Termii(api_key=os.environ.get("TERMII_API_KEY"))
        self.sender_id = os.environ.get("TERMII_SENDER_ID")

    def test_send_token(self):
        pass

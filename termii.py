# imports

from typing import Union
import requests


class Termii:
    def __init__(self, api_key: str, sender_id: Union[str, None] = None) -> None:
        self.api_key = api_key
        self.sender_id = sender_id
        self.__base_url = "https://api.ng.termii.com/api"

    def get_senderId(self):
        """Get a list of all sender IDs for the specified api key.
        """

        response = requests.get(
            f"{self.__base_url}/sender-id?api_key={self.api_key}")

        return response.json()

    def request_senderId(self, sender_id: str, use_case: str, company: str):
        """Request a new sender ID for your account.

        Arguments:
        
        sender_id (str): Represents the ID of the sender which can be alphanumeric or numeric. Alphanumeric sender ID length should be between 3 and 11 characters (Example:CompanyName)

        use_case (str): A sample of the type of message sent.. Should be >= 20 characters.

        company (str): Represents the name of the company with the sender ID.
        """
        payload = {
            "api_key": self.api_key,
            "sender_id": sender_id,
            "usecase": use_case,
            "company": company
        }

        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(
            f"{self.__base_url}/sender-id/request/", headers=headers, json=payload)

        return response.json()

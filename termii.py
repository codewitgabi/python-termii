# imports

from typing import Union, Literal, Optional, Mapping
import requests
from requests import Response


class Termii:
    def __init__(self, api_key: str, sender_id: Union[str, None] = None) -> None:
        self.api_key = api_key
        self.sender_id = sender_id
        self.__base_url = "https://api.ng.termii.com/api"

    def get_senderId(self) -> Response:
        """Get a list of all sender IDs for the specified api key.
        """

        response = requests.get(
            f"{self.__base_url}/sender-id?api_key={self.api_key}")

        return response.json()

    def request_senderId(self, sender_id: str, use_case: str, company: str) -> Response:
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

    def send_message(self, _from: Union[str, None], to: Union[str, list], type: str, channel: Literal["whatsapp", "dnd", "generic"], sms: Union[str, None] = None,  media: Union[Optional[Mapping[Literal["url", "caption"], str]], None] = None) -> Response:
        """
        Arguments:

        _from (str): Represents the ID of the sender which can be alphanumeric or numeric. Alphanumeric sender ID length should be between 3 and 11 characters (Example:CompanyName)

        to (str): Represents the destination phone number. Phone number must be in the international format (Example: 23490126727). You can also send to multiple numbers. To do so put numbers in an array (Example: ["23490555546", "23423490126999"]) Please note: the array takes only 100 phone numbers at a time

        sms (str): Text of a message that would be sent to the destination phone number

        type (str): The kind of message that is sent, which is a plain message.

        channel (Literal["whatsapp", "dnd", "generic"]): This is the route through which the message is sent. It is either dnd, whatsapp, or generic

        media (Optional[Mapping[Literal["url", "caption"], str]]): This is a media object, it is only available for the High Volume WhatsApp. When using the media parameter, ensure you are not using the sms parameter
        """

        payload = {
            "from": _from,
            "to": to,
            "sms": sms,
            "type": type,
            "channel": channel,
            "api_key": self.api_key,
        }
        headers = {
            'Content-Type': 'application/json',
        }

        if channel == "whatsapp":
            payload["media"] = media
            del payload["sms"]

        response = requests.post(f"{self.__base_url}/sms/send/", json=payload, headers=headers)

        return response.json()

    def send_bulk_message(self, _from: Union[str, None], to: Union[str, list], sms: Optional[str], type: str, channel: Literal["whatsapp", "dnd", "generic"]) -> Response:
        """
        Arguments:

        _from (str): Represents the ID of the sender which can be alphanumeric or numeric. Alphanumeric sender ID length should be between 3 and 11 characters (Example:CompanyName)

        to (str): Represents the destination phone number. Phone number must be in the international format (Example: 23490126727). You can also send to multiple numbers. To do so put numbers in an array (Example: ["23490555546", "23423490126999"]) Please note: the array takes only 100 phone numbers at a time

        sms (str): Text of a message that would be sent to the destination phone number

        type (str): The kind of message that is sent, which is a plain message.

        channel (Literal["whatsapp", "dnd", "generic"]): This is the route through which the message is sent. It is either dnd, whatsapp, or generic
        """

        payload = {
            "from": _from,
            "to": to,
            "sms": sms,
            "type": type,
            "channel": channel,
            "api_key": self.api_key,
        }
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(f"{self.__base_url}/sms/send/bulk", json=payload, headers=headers)

        return response.json()

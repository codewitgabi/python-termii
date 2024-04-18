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

        response = requests.post(
            f"{self.__base_url}/sms/send/", json=payload, headers=headers)

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

        response = requests.post(
            f"{self.__base_url}/sms/send/bulk", json=payload, headers=headers)

        return response.json()

    def send_auto_message(self, to: str, sms: str) -> Response:
        """
        This API allows businesses send messages to customers using Termii's auto-generated messaging numbers that adapt to customers location.

        Arguments:

        to (str): Represents the destination phone number. Phone number must be in the international format (Example: 2349012672711)

        sms (str): Text of a message that would be sent to the destination phone number
        """

        payload = {
            "to": to,
            "sms": sms,
            "api_key": self.api_key
        }

        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(
            f"{self.__base_url}/sms/number/send", headers=headers, json=payload)

        return response.json()

    def get_phonebooks(self) -> Response:
        """
        Get phonebooks using these APIs. Each phonebook can be identified by a unique ID, which makes it easier to edit or delete a phonebook.
        """

        response = requests.get(
            f"{self.__base_url}/phonebooks?api_key={self.api_key}")

        print(response.json())
        return response.json()

    def create_phonebook(self, phonebook_name: str, description: Optional[str] = None) -> Response:
        """
        Create a phonebook

        Arguments:

        phonebook_name (str): Name of the phonebook

        description (str): Description of the phonebook, not required
        """

        payload = {
            "api_key": self.api_key,
            "phonebook_name": phonebook_name,
        }

        if description:
            payload["description"] = description

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(
            f"{self.__base_url}/phonebooks", headers=headers, json=payload)

        return response.json()

    def update_phonebook(self, phonebook_id: str, phonebook_name: str, description: Optional[str] = None) -> Response:
        """
        Update phonebook with the given phonebook_id

        Arguments:

        phonebook_id (str): ID of the phonebook

        phonebook_name (str): Name of the phonebook

        description (str): Description of the phonebook, not required
        """

        payload = {
            "api_key": self.api_key,
            "phonebook_name": phonebook_name,
        }

        if description:
            payload["description"] = description

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.patch(
            f"{self.__base_url}/phonebooks/{phonebook_id}", headers=headers, json=payload)

        return response.json()

    def delete_phonebook(self, phonebook_id: str) -> Response:
        """Delete a phonebook

        Argument:

        phonebook_id (str): ID of the phonebook to be deleted
        """

        response = requests.delete(
            f"{self.__base_url}/phonebooks/{phonebook_id}?api_key={self.api_key}")

        return response.json()

    def get_contact(self, phonebook_id: str):
        """
        Get all available contacts
        """

        response = requests.get(
            f"{self.__base_url}/phonebooks/{phonebook_id}/contacts?api_key={self.api_key}")

        print(response.json())
        return response.json()

    def add_contact(self, phonebook_id: str, phone_number: str, country_code: Optional[int] = None, email_address: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, company: Optional[str] = None) -> Response:
        """
        Adds a single contact to a phonebook

        Arguments:

        phonebook_id (str): The id of the phonebook to add contact

        phone_number (str): Phone number of the contact

        country_code (Optional[str]): Represents short numeric geographical codes developed to represent countries (Example: 234 ).

        email_address (Optional[str]): email address of the contact

        first_name (Optional[str]): first name of the contact

        last_name (Optional[str]): last name of the contact

        company (Optional[str]): name of the company of the contact
        """

        payload = {
            "api_key": self.api_key,
            "phone_number": phone_number,
            "email_address": email_address,
            "first_name": first_name,
            "last_name": last_name,
            "company": company,
            "country_code": country_code
        }

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(
            f"{self.__base_url}/phonebooks/{phonebook_id}/contacts", headers=headers, json=payload)

        return response.json()

    def add_contacts(self, phonebook_id: str, contact_file: str, file_type: str, country_code: str) -> Response:
        """
        Add bulk contacts to a phonebook

        Arguments:

        phonebook_id (str): The id of the phonebook to add contacts

        contact_file (str): File containing the list of contacts you want to add to your phonebook. Supported files include : 'txt', 'xlsx', and 'csv'.

        file_type (str): The type of file that contains your contacts. Example: 'text/csv'.

        country_code (str): Represents short numeric geographical codes developed to represent countries (Example: 234 ).
        """

        payload = {'country_code': country_code}

        files = [
            ('contact_file', (contact_file, 'rb'), file_type)
        ]

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(f"{self.__base_url}/phonebooks/{
                                 phonebook_id}/contacts", headers=headers, data=payload, files=files)

        return response.json()

    def delete_contact(self, contact_id: str) -> Response:
        """Delete a contact

        Argument:

        contact_id (str): Id of contact to be deleted.
        """

        response = requests.delete(
            f"{self.__base_url}/phonebook/contact/{contact_id}?api_key={self.api_key}")

        return response.json()

    def send_token(self, message_type: Literal["NUMERIC", "ALPHANUMERIC"], to: str, _from: str, channel: Literal["generic", "dnd", "whatsapp"], message_text: str, pin_time_to_live: int = 60, pin_attempts: int = 3, pin_length: int = 4, pin_placeholder: str = "< 1234 >") -> Response:
        """
        The send token API allows businesses trigger one-time-passwords (OTP) across any available messaging channel on Termii. One-time-passwords created are generated randomly and there's an option to set an expiry time.

        Arguments:

        message_type (str): Enum: "NUMERIC" "ALPHANUMERIC" Type of message that will be generated and sent as part of the OTP message. You can set message type to numeric or alphanumeric

        to (str): Represents the email address if the channel is set to email (Example: testshola@termii.com). It represents the destination phone number if other channels are selected. Phone number must be in the international format (Example: 23490126727)

        from (str): Represents the configuration ID if the channel is set to email (Example: 0a53c416-uocj-95af-ab3c306aellc). It can be found on your Termii dashboard. If other channels are selected, it represents a sender ID which can be alphanumeric or numeric. Alphanumeric sender ID length should be between 3 and 11 characters (Example:CompanyName)

        channel (Literal[generic, dnd, whatsapp]): This is the route through which the message is sent. It is either dnd, WhatsApp, or generic or email

        pin_attempts (int): Example: 3
        Represents the number of times the PIN can be attempted before expiration. It has a minimum of one attempt

        pin_time_to_live (int): Example: 1
        Represents how long the PIN is valid before expiration. The time is in minutes. The minimum time value is 0 and the maximum time value is 60

        pin_length (int): Example: 4
        The length of the PIN code.It has a minimum of 4 and maximum of 8.

        pin_placeholder (str): Example: "< 1234 >"
        PIN placeholder. Right before sending the message, PIN code placeholder will be replaced with generate PIN code.

        message_text (str): Text of a message that would be sent to the destination phone number
        """

        payload = {
            "api_key": self.api_key,
            "message_type": message_type,
            "to": to,
            "from": _from,
            "channel": channel,
            "pin_attempts": pin_attempts,
            "pin_time_to_live":  pin_time_to_live,
            "pin_length": pin_length,
            "pin_placeholder": pin_placeholder,
            "message_text": message_text,
            "pin_type": message_type
        }

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(
            f"{self.__base_url}/sms/otp/send", headers=headers, json=payload)

        return response.json()

    def voice_token(self, phone_number: str, pin_attempts: int, pin_time_to_live: int, pin_length: int) -> Response:
        """
        The voice token API enables you to generate and trigger one-time passwords (OTP) through the voice channel to a phone number. OTPs are generated and sent to the phone number and can only be verified using our Verify Token API .

        Arguments:

        phone_number (str): The destination phone number. Phone number must be in the international format (Example: 23490126727)

        pin_attempts (int): Represents the number of times the PIN can be attempted before expiration. It has a minimum of one attempt

        pin_time_to_live (int): Represents how long the PIN is valid before expiration. The time is in minutes. The minimum time value is 0 and the maximum time value is 60

        pin_length (int): The length of the PIN code.It has a minimum of 4 and maximum of 8.
        """

        payload = {
            "api_key": self.api_key,
            "phone_number": phone_number,
            "pin_attempts": pin_attempts,
            "pin_time_to_live":  pin_time_to_live,
            "pin_length": pin_length,
        }

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(
            f"{self.__base_url}/sms/otp/send/voice", headers=headers, json=payload)

        return response.json()

    def voice_call(self, phone_number: str, code: str) -> Response:
        """
        The voice call API enables you to send messages from your application through our voice channel to a phone number. Only one-time-passwords (OTP) are allowed for now and these OTPs can not be verified using our Verify Token API.

        Arguments:

        phone_number (str): The destination phone number. Phone number must be in the international format (Example: 23490126727)

        code (str): Example: 3344
        The code you want your users to receive. It has to be numeric and length must be between 4 and 8 digits.
        """

        payload = {
            "api_key": self.api_key,
            "phone_number": phone_number,
            "code": code
        }

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(
            f"{self.__base_url}/sms/otp/send/voice", headers=headers, json=payload)

        return response.json()

    def email_token(self, email_address: str, code: str, email_configuration_id: str) -> Response:
        """
        The email token API enables you to send one-time-passwords from your application through our email channel to an email address. Only one-time-passwords (OTP) are allowed for now and these OTPs can not be verified using our Verify Token API.

        Arguments:

        email_address (str): Represents the email address you are sending to (Example: test@termii.com).

        code (str): Represents the OTP sent to the email address

        email_configuration_id (str): This is represents the email configuration you have added on your Termii dashboard. It can be found on your Termii dashboard.
        """

        payload = {
            "api_key": self.api_key,
            "email_address": email_address,
            "code": code,
            "email_configuration_id": email_configuration_id
        }

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(
            f"{self.__base_url}/email/otp/send", headers=headers, json=payload)

        return response.json()

    def verify_token(self, pin_id: str, pin: str) -> Response:
        """
        Verify token API, checks tokens sent to customers and returns a response confirming the status of the token. A token can either be confirmed as verified or expired based on the timer set for the token.

        Arguments:

        pin_id (str): ID of the PIN sent (Example: "c8dcd048-5e7f-4347-8c89-4470c3af0b")

        pin (str): The PIN code (Example: "195558")
        """

        payload = {
            "api_key": self.api_key,
            "pin_id": pin_id,
            "pin": pin
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(
            f"{self.__base_url}/sms/otp/verify", headers=headers, json=payload)

        return response.json()

    def generate_token(self, pin_type: Literal["NUMERIC", "ALPHANUMERIC"], phone_number: str, pin_attempts: int, pin_time_to_live: int, pin_length: int) -> Response:
        """
        This API returns OTP codes in JSON format which can be used within any web or mobile app. Tokens are numeric or alpha-numeric codes generated to authenticate login requests and verify customer transactions.

        Arguments:

        pin_type (Literal["NUMERIC], "ALPHANUMERIC]): Enum: "NUMERIC" "ALPHANUMERIC"
        Type of PIN code that will be generated and sent as part of the OTP message. You can set PIN type to numeric or alphanumeric

        phone_number (str): The destination phone number. Phone number must be in the international format (Example: 23490126727)

        pin_attempts (int): Represents the number of times the PIN can be attempted before expiration. It has a minimum of one attempt

        pin_time_to_live (int): Represents how long the PIN is valid before expiration. The time is in minutes. The minimum time value is 0 and the maximum time value is 60

        pin_length (int): The length of the PIN code. It has a minimum of 4 and maximum of 8.
        """

        payload = {
            "api_key": self.api_key,
            "pin_type": pin_type,
            "phone_number": phone_number,
            "pin_attempts": pin_attempts,
            "pin_time_to_live": pin_time_to_live,
            "pin_length": pin_length
        }

        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(
            f"{self.__base_url}/sms/otp/generate", headers=headers, json=payload)

        return response.json()

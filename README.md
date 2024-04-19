<h1 align="center">Termii Python Client <img alt="Static Badge" src="https://img.shields.io/badge/termii-python-client?style=for-the-badge&logo=github&logoColor=%23000">
</h1>
<br><br>

<div align="center">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/codewitgabi/python-termii">
    <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/codewitgabi/python-termii">
    <img alt="GitHub Issues or Pull Requests" src="https://img.shields.io/github/issues/codewitgabi/python-termii">
    <img alt="GitHub Issues or Pull Requests" src="https://img.shields.io/github/issues-pr/codewitgabi/python-termii">
    <img alt="GitHub License" src="https://img.shields.io/github/license/codewitgabi/python-termii">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/codewitgabi/python-termii">
    <img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/codewitgabi/python-termii">
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/termii-python-client">
</div>

<hr/>

### What is Termii

Termii is an API that provide endpoint which can be used to send sms messages, it also perform other functions which will be discussed below.
click [here](https://developer.termii.com/) for more about Termii

### Key Features

- Messaging: Allows you to send message to any country in the world across sms and whatsapp channels

- Tokens: Allows business to generate,send and verify one time password (OTP)

- Insight: Retrieve real-time delivery report of messages sent to customers as well as the status of their contact.

### Usage

Install the python package from pip by running

```shell
pip install termii-python-client
```

Before delving into the usage, you need the following:

- A Termii account : This can be created [here](www.termii.com)

- Get your api key which will be used for further api calls

#### Implementing python termii functionalities

- **Initillize the Termii class**

```python
import os
from termii.termii import Termii

# get your api-key
api_key = os.environ.get("TERMII_API_KEY")
sender_id = os.environ.get("TERMII_SENDER_ID")

termii = Termii(api_key, sender_id)
```

#### Available methods

```python
import os
from typing import Union, Literal
from termii.termii import Termii

termii = Termii(os.environ.get("TERMII_API_KEY"), os.environ.get("TERMII_SENDER_ID"))

termii.add_contact(phonebook_id: str, phone_number: str, country_code: Optional[int] = None, email_address: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, company: Optional[str] = None)
termii.add_contacts(phonebook_id: str, contact_file: str, file_type: str, country_code: str)
termii.create_phonebook(phonebook_name: str, description: Optional[str] = None)
termii.delete_contact(contact_id: str)
termii.delete_phonebook(phonebook_id: str)
termii.email_token(email_address: str, code: str, email_configuration_id: str)
termii.generate_token(pin_type: Literal["NUMERIC", "ALPHANUMERIC"], phone_number: str, pin_attempts: int, pin_time_to_live: int, pin_length: int)
termii.get_balance()
termii.get_contact(phonebook_id: str)
termii.get_phonebooks()
termii.get_senderId()
termii.history()
termii.request_senderId(sender_id: str, use_case: str, company: str)
termii.send_auto_message(to: str, sms: str)
termii.send_bulk_message(_from: Union[str, None], to: Union[str, list], sms: Optional[str], type: str, channel: Literal["whatsapp", "dnd", "generic"])
termii.send_message(_from: str, to: str | None, type: str, channel: Literal["whatsapp", "dnd", "generic"], sms: Union[str, None] = None, media: Union[Optional[Mapping[Literal["url", "caption"], str]], None] = None)
termii.send_token(message_type: Literal["NUMERIC", "ALPHANUMERIC"], to: str, _from: str, channel: Literal["generic", "dnd", "whatsapp"], message_text: str, pin_time_to_live: int = 60, pin_attempts: int = 3, pin_length: int = 4, pin_placeholder: str = "< 1234 >")
termii.update_phonebook(phonebook_id: str, phonebook_name: str, description: Optional[str] = None)
termii.verify_phone_number(phone_number: str)
termii.verify_token(pin_id: str, pin: str)
termii.voice_call(phone_number: str, code: str)
termii.voice_token(phone_number: str, pin_attempts: int, pin_time_to_live: int, pin_length: int)
```

To get more detail about a particular method, use the python help() function

### Contributors

- Gabriel Michael Ojomakpene [codewitgabi]
- Joseph Joshua

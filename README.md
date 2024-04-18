# TERMII PYTHON

### WHAT IS TERMII

Termii is an API that provide endpoint which can be used to send sms messages, it also perform other functions which will be discussed below.
click [here](https://developer.termii.com/) for more about Termii

# PROJECT DESCRIPTION

### KEY FEATURES

- Messaging: Allows you to send message to any country in the world across sms and whatsapp channels

- Tokens: Allows business to generate,send and verify one time password (OTP)

- Insight: Retrieve real-time delivery report of messages sent to customers as well as the status of their contact.

### INSTALLATION
Install the python package from pip by running
```
pip install termii-python-client==1.0.0
```

### USAGE
Before delving into the usage, you need the follow
ing:
* A Termii account : This can be created [here](www.termii.com)

* Get your api key which will be used for further calls

#### Implementing python termii functionalities

- **Initillize the Termii class**
    ```
    import Termii

    # get your api-key 
    api_key = "1236erhrbdjd"

    termii = Termii(api_key,sender_id)

    ```

- **Getting senderId**: this project also provide a method to get senders id 

    ``` termii.get_senderId() ```

- **requesting new sender id**: 
To request a new sender id, you need to pass the following parameters
    * sender_id(str) : which is your previous sender id
    * use_case(str) : A sample of the type of message sent.. Should be >= 20 characters.
    * Company(str): Represents the name of the company with the sender id.

    With the above parameters you can request a new sender id by calling the function below

    ``` termii.request_senderId(sender_id,use_case,company) ```

- **Send Message**: This method allows you to send message
    
    ``` termii.send_message(from,to,type,sms,channel,media)```
    * from (str): Represents the ID of the sender which can be alphanumeric or numeric. Alphanumeric sender ID length should be between 3 and 11 characters (Example:CompanyName)

    * to (str): Represents the destination phone number. Phone number must be in the international format (Example: 23490126727). You can also send to multiple numbers. To do so put numbers in an array (Example: ["23490555546", "23423490126999"]) Please note: the array takes only 100 phone numbers at a time

    * sms (str): Text of a message that would be sent to the destination phone number

    * type (str): The kind of message that is sent, which is a plain message.

    * channel (Literal["whatsapp", "dnd", "generic"]): This is the route through which the message is sent. It is either dnd, whatsapp, or generic

    * media (Optional[Mapping[Literal["url", "caption"], str]]): This is a media object, it is only available for the High Volume WhatsApp. When using the media parameter, ensure you are not using the sms parameter
        





# WhatsApp Message Scheduler using Twilio

This project enables you to schedule WhatsApp messages to be sent at a specific time using Python and Twilio's API. The script allows users to input recipient details, message content, and scheduling information, and it will automatically send the message at the scheduled time.

## Features

- **Send WhatsApp messages automatically**: Schedule a message to be sent at a future date and time.
- **Input recipient and message details**: Enter recipient’s name, WhatsApp number, and the message you want to send.
- **Uses Twilio API**: Sends messages through WhatsApp using Twilio’s messaging service.
- **Time validation**: Ensures that messages are sent at the specified time, only in the future.

## Requirements

- Python 3.x
- `twilio` library
- `datetime` module (part of Python’s standard library)

### Installation

To use this project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/whatsapp-message-scheduler-twilio.git
    cd whatsapp-message-scheduler-twilio
    ```

2. Install the required dependencies:

    ```bash
    pip install twilio
    ```

3. You need to create a Twilio account to obtain your **Account SID** and **Auth Token**.
   - Sign up at [Twilio](https://www.twilio.com/).
   - Get your Twilio account SID and auth token from the Twilio console.
   - Replace `account_sid` and `auth_token` in the code with your own credentials.

4. Make sure you have a Twilio number configured to send WhatsApp messages (you can get one from the Twilio console).

## Usage

1. Run the script:

    ```bash
    python schedule_whatsapp_message.py
    ```

2. Follow the prompts to enter the following information:

    - **Recipient's Name**: The name of the person you want to message.
    - **Recipient's WhatsApp Number**: The recipient's phone number, including the country code (e.g., +919123456789).
    - **Message Body**: The content of the message you want to send.
    - **Date**: The date (YYYY-MM-DD) you want the message to be sent.
    - **Time**: The time (HH:MM in 24-hour format) at which you want the message to be sent.

3. The script will calculate the time difference between the current time and the scheduled time, and it will send the message to the recipient at the specified time.

4. You’ll receive a confirmation once the message has been successfully sent through Twilio.

## Example

```bash
Enter the recipient name: John Doe
Enter the recipient Whatsapp Number with country code: +919876543210
Enter the message you want to send to John Doe: Hello! This is a scheduled message.
Enter the date to send the message (YYYY-MM-DD): 2025-04-21
Enter the time you want to send the message (HH:MM in 24 hr format): 10:30

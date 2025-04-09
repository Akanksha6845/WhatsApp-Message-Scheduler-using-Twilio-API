# Steps:
# 1.Tiwillio client setup
# 2.User input
# 3.Scheduling logic 
# 4.Sent msg

# step 1: installed all the required libraries
from twilio.rest import Client
from datetime import datetime,timedelta # timedelta is diference of the current time to future send time
import time

#step 2: Twillio Crendentials
account_sid='AC608818189b2479e293e5c7047cccba66'
auth_token='d178b0b3a32aabd13a69d3707ead02dc'

Client=Client(account_sid,auth_token)

#step 3 :Define sent message function
def send_whatsapp_message(recipient_number,message_body):
    try:
        message= Client.messages.create(
            from_='whatsapp:14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent Sucessfully! Message SID {message.sid}')
    except Exception as e:
        print("An error occoured!")
        
#step 4: User Input
name=input("Enter the recipent name: ")
recipient_num=input("Enter the recipient Whatsapp Number with country code : ")
message_body=input(F'Enter the message you want to send to {name}')

#step 5:date time and calculated delay
date_str=input("Enter the date to send the message (YYYY-MM-DD): ")
time_str=input("Enter the time you want to send the message (HH:MM in 24 hr format): ")

#date time
schedule_datetime=datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_date_time=datetime.now()

#delay time
time_difference=schedule_datetime-current_date_time
delay_seconds=time_difference.total_seconds()

if delay_seconds<=0:
    print('The specified time and date is already past, pls provide a future date and time')
else:
    print('Message scheduled to be sent to the {name} at {schedule_datetime}.')
    
# wait untilthe scheduled time
    time.sleep(delay_seconds)

#send the message
    send_whatsapp_message(recipient_num,message_body)

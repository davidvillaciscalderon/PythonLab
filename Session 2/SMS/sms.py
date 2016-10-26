from twilio.rest import TwilioRestClient
# put your own credentials here

ACCOUNT_SID = 'ACCOUNT DATA'
AUTH_TOKEN = 'ACOUNT DATA'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to = 'TO_NUMBER',
    from_ = 'FROM_NUMBER',
    body = 'MESSAGE',
)



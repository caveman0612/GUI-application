from twilio.rest import Client

def sendTextMessage(message):

    # Your Account SID from twilio.com/console
    account_sid = "AC5dd1e1c5f305b831f9b1befedd9541ba"
    # Your Auth Token from twilio.com/console
    auth_token  = "8b83bafc2fcbc7f0a240c85888cc305e"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+12182521896",
        from_="+12014743471",
        body=message)

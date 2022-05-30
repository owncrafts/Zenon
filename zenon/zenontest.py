import zenon

token = "OTgwMTY0ODM5NzE4Njc4NTY4.G9Dcpv.JkGHfbfAIGe3bMc0GHCjIexz10DNK8tf0Xz-7M"

def on_message():
    while True:
        chatid = "409879939400335362"
        message = client.get_message(chatid)
        if message == "!test":
            client.send_message(chatid, "sei grassa!")
        
if __name__ == '__main__':
    client = zenon.Client(token)
    client.func_loop(on_message)

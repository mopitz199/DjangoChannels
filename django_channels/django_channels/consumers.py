from channels import Group

def websocket_receive(message):
    text = message.content.get('text')
    if text:
        Group("anything").add(message.reply_channel)
        message.reply_channel.send({"text": "You said: {}".format(text)})

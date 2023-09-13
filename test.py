from pyrogram import Client

api_id = 22239809
api_hash = 'fc57726d589788687fc518260cfe176d'

# Create a Pyrogram client
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Log in to the account
app.start()

# Get the chat ID of the private chat
chat_id = app.resolve_peer("").user_id

# Send a message to the private chat
app.send_message(chat_id, "Hello, private chat!")

# Stop the client
app.stop()
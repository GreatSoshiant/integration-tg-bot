from telegram.ext import Updater, MessageHandler, Filters
from notion_client import Client

# Set up Notion API client
notion = Client(auth="Notion_API_Token")
database_id = "DB_ID"

# Set up Telegram bot
updater = Updater(token ="Telegram_Token", use_context=True)
dispatcher = updater.dispatcher

# Define a function to handle incoming messages
def handle_message(update, context):
    message = update.message.text
    if "[tech]" in message:
        # If message contains "tech", copy it to a Notion database
        notion.pages.create(parent={"database_id": database_id}, properties={"Name": {"title": [{"text": {"content": message}}]}})
    else:
        # If message does not contain "tech", do nothing
        pass

# Set up message handler
handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(handler)

# Start the bot
updater.start_polling()

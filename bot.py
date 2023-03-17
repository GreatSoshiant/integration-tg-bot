from datetime import datetime
from telegram.ext import Updater, MessageHandler, Filters
from notion_client import Client
from notion_client.errors import *

# Set up Notion API client
notion = Client(auth="Notion_API_Token")
database_id = "DB_ID"

def handle_tech_message(update, context):
    message = update.message
    if 'tech' in message.text:
        # Get the name of the Telegram group/channel
        group_name = message.chat.title
        
        # Get the invite link for the group/channel
        invite_link = context.bot.exportChatInviteLink(message.chat.id)
      
        # Add a new entry to the Notion database
        new_page = {
            "Message": {"title": [{"text": {"content": message.text}}]},
            "Group Name": {"rich_text": [{"text": {"content": group_name}}]},
            "Invite Link": {"url": invite_link}
        }
        try:
            notion.pages.create(parent={"database_id": database_id}, properties=new_page)
        except (BadRequestError, APIResponseError) as e:
            print(e)

# Create an Updater instance and register the message handler
updater = Updater(token ="Telegram_Token", use_context=True)
tech_handler = MessageHandler(Filters.text & (~Filters.command), handle_tech_message)
updater.dispatcher.add_handler(tech_handler)

# Start the bot
updater.start_polling()
updater.idle()

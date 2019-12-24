#Email Bot Service
from __future__ import print_function
import json
import pickle
import os.path
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64

class EmailBotService:
    """Service for communicate with bot and gmail."""
    def __init__(self, access_token: str):
        """Initialize bot work."""
        self.updater = Updater(token=access_token, use_context=True)
        self.track_message = None

        start_handler = CommandHandler(command="start",
                                       callback=self.start_command)

        cancel_handler = CommandHandler(command="cancel",
                                        callback=self.cancel_command)
        self.updater.dispatcher.add_handler(start_handler)
        self.updater.dispatcher.add_handler(cancel_handler)

    def run_bot(self):
        """Running bot."""
        self.updater.start_polling()

    def cancel_command(self, bot, update):
        pass
        """Bot cancel command"""
        text_message = "If you want start again please enter /start."
        print(text_message)
        self.track_message = None
        bot.send_message(chat_id=update.message.chat_id, text=text_message)

    def start_command(self, update, context):
        """Bot start command"""
        SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        # if os.path.exists('token.pickle'):
        #     with open('token.pickle', 'rb') as token:
        #         creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        # Call the Gmail API
        # results = service.users().labels().list(userId='me').execute()
        # labels = results.get('labels', [])
        #
        # if not labels:
        #     context.bot.send_message(chat_id=update.message.chat_id, text='No labels found.')
        # else:
        #     labels_names = [label['name'] for label in labels]
        #     context.bot.send_message(chat_id=update.message.chat_id, text="\n".join(labels_names))


        # работает
        # получаем последние сообщения с ящика
        messages = []
        response = service.users().messages().list(userId='me').execute()
        messages.extend(response['messages'])

        # у каждого из сообщений достаем id
        for message in messages[0:3]:
            mid = message['id']

            # получаем сообщение по id
            message_message = service.users().messages().get(userId='me', id=mid).execute()

            # информация об отправителе, получателе и теме сообщения хранится в ключе 'payload' --> 'headers'
            headers = message_message['payload']['headers']

            from_who = None
            to_whom = None
            subject = None

            for item in headers:

                if item['name'] == 'From':
                    from_who = item['value']
                elif item['name'] == 'To':
                    to_whom = item['value']
                elif item['name'] == 'Subject':
                    subject = item['value']

            # ищем текст сообщения
            # достаем из сообщения его части
            text_find = message_message['payload']['parts']
            body_of_part = None
            # достаем из нужной части (текст сообщения хранится под нулевым индексом) текст сообщения закодированный в
            # формате "utf-8" и "base64"
            for part in text_find:
                if part['partId'] == '0':
                    body_of_part = part['body']
            # декодируем
            encoded_text = body_of_part['data']
            decodedBytes = base64.urlsafe_b64decode(encoded_text)
            # текст сообщения сохраняем в переменную
            decoded_text = str(decodedBytes, "utf-8")
            telebot_message_text = f'Sender: {from_who}.\n' \
                                   f'Receiver: {to_whom}.\n' \
                                   f'Subject: {subject}.\n' \
                                   f'Text of message: {decoded_text}'

            context.bot.send_message(chat_id=update.message.chat_id, text=telebot_message_text)







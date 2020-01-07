#Email Bot Service
from __future__ import print_function
import json
import pickle
import os.path
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow, Flow
from google.auth.transport.requests import Request
import base64
import sqlalchemy as db
import time

class EmailBotService:
    """Service for communicate with bot and gmail."""
    def __init__(self, access_token: str):
        """Initialize bot work."""
        self.updater = Updater(token=access_token, use_context=True)
        self.track_message = None

        self.chat_id = self.updater.bot

        start_handler = CommandHandler(command="start",
                                       callback=self.start_command)
        # cancel_handler = CommandHandler(command="cancel",
        #                                 callback=self.cancel_command)
        get_message_handler = CommandHandler(command="getmessage",
                                             callback=self.getmessage)
        self.updater.dispatcher.add_handler(start_handler)
        self.updater.dispatcher.add_handler(get_message_handler)
        # self.updater.dispatcher.add_handler(cancel_handler)

    def run_bot(self):
        """Running bot."""
        self.updater.start_polling()

    # def cancel_command(self, bot, update):
    #     """Bot cancel command"""
    #     text_message = "If you want start again please enter /start."
    #     print(text_message)
    #     bot.send_message(chat_id=update.message.chat_id, text=text_message)

    def get_chat_id(self, update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def getmessage(self, update, context):

        redirect_uri = f"http://localhost:8000/"
        flow = Flow.from_client_secrets_file(
            'credentials.json',
            scopes=['https://mail.google.com/',
                    'https://www.googleapis.com/auth/gmail.readonly'],
            redirect_uri=redirect_uri)

        engine = db.create_engine('sqlite:////home/denis/udemy_django/project_1/helloworld/db.sqlite3')
        connection = engine.connect()
        metadata = db.MetaData()
        hola_bottable = db.Table('hola_bottable', metadata, autoload=True, autoload_with=engine)

        # Equivalent to 'SELECT * FROM census'
        query = db.select([hola_bottable])
        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()

        code = ResultSet[-1][1]
        flow.fetch_token(code=code, code_verifier="111")

        # You can use flow.credentials, or you can just get a requests session
        # using flow.authorized_session.
        session = flow.authorized_session()
        # print(session.get('https://www.googleapis.com/userinfo/v2/me').json())

        messages = []
        response = session.users().messages().list(userId='me').execute()
        messages.extend(response['messages'])

        # у каждого из сообщений достаем id
        for message in messages[0:3]:
            mid = message['id']

            # получаем сообщение по id
            message_message = session.users().messages().get(userId='me', id=mid).execute()

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





    def start_command(self, update, context):
        """Bot start command"""
        SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        creds = None
        redirect_uri = f"http://localhost:8000/"
        flow = Flow.from_client_secrets_file(
            'credentials.json',
            scopes=['profile', 'email'],
            redirect_uri=redirect_uri
        )
        flow.code_verifier = "111"


        # Tell the user to go to the authorization URL.
        auth_url, _ = flow.authorization_url(prompt='consent',  access_type='offline', include_granted_scopes='true')

        telebot_message_text = 'Please go to this URL: {}'.format(auth_url)
        context.bot.send_message(chat_id=update.message.chat_id, text=telebot_message_text)








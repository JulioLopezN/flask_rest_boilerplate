import smtplib
import ssl
from email.mime.text import MIMEText


class SmtpEmailService:

    def __init__(self, hostname='localhost', port=25, ssl=False, username='', password='', from_address='noreply@localhost'):
        self.hostname = hostname
        self.port = port
        self.ssl = ssl
        self.username = username
        self.password = password
        self.from_address = from_address

    def set_default_from_address(self, from_address):
        self.from_address = from_address

    def send(self, message, to_address, from_address=None):
        if not from_address:
            from_address = self.from_address

        server = self.__get_server()
        return server.sendmail(from_address, to_address, message.encode('utf-8'))

    def __get_server(self):
        context = ssl.create_default_context()

        if self.ssl:
            server = smtplib.SMTP_SSL(self.hostname, self.port, context=context)
        else:
            server = smtplib.SMTP(self.hostname, self.port)

        if self.username:
            server.login(self.username, self.password)

        server.connect()

        return server

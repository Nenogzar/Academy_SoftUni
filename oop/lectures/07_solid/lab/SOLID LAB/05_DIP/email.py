class Email:
    def send_email(self):
        pass
class Notification:
    def __init__(self):
        self._email = Email()
    def promotional_notification(self):
        self._email.send_email()
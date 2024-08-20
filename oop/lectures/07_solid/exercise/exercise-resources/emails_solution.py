from abc import ABC, abstractmethod

class IContent(ABC):

    @abstractmethod
    def format(self):
        pass

class MyContent(IContent):
    def __init__(self, content):
        self.content = content

    def format(self):
        return f"<MyML>{self.content}</MyML>"

class Email:
    def __init__(self, protocol):
        self.protocol = protocol
        self.sender = None
        self.receiver = None
        self.content = None

    def set_sender(self, sender):
        self.sender = f"I'm {sender}"

    def set_receiver(self, receiver):
        self.receiver = f"I'm {receiver}"

    def set_content(self, content: IContent):
        self.content = content.format()

    def __str__(self):
        return f"Sender: {self.sender}\nReceiver: {self.receiver}\nContent:\n{self.content}"



# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)


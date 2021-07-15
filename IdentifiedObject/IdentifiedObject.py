from abc import ABC, abstractmethod
import yagmail


class IdentifiedObject(ABC):

    @abstractmethod
    def __init__(self, oid):
        self.oid = oid

    def __eq__(self, other):
        if self.oid == other.oid:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.oid)


class Emailer:
    _sole_instance = None

    def __new__(cls):
        cls.yag = yagmail.SMTP()
        if cls._sole_instance is None:
            cls._sole_instance = super(Emailer, cls).__new__(cls)
        return cls._sole_instance

    def configure(self, sender_address):
        self.yag.STMP(sender_address)

    def instance(self):
        return self._sole_instance

    def send_plain_email(self, recipients, subject, message):
        if isinstance(recipients, list):
            for recipient in recipients:
                self.yag.send(recipient, subject, message)
        else:
            self.yag.send(recipients, subject, message)
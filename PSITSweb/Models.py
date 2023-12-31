from warnings import warn
from Util import GetPriceRef

from Util import deprecated, DecimalEncoder, DateTimeEncoder, GetReference
from enum import Enum
#import json


class Announcement:
    def __init__(self, uid, title, date, content):
        self.uid = uid
        self.title = title
        self.date = date
        self.content = content
        self.image_location = ''
        self.image_file_extras: list = []

    def __repr__(self):
        return str(self.uid)


class Account:
    def __init__(self, uid, rfid, firstname, lastname, course, year, email):
        self.uid = uid
        self.rfid = rfid
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.year = year
        self.email = email
        self.img = ''
        self.password = ''
    
    def toJSON(self):
        data: dict = {
            'uid' : self.uid,
            'rfid' : self.rfid,
            'firstname' : self.firstname,
            'lastname' : self.lastname,
            'course' : self.course,
            'year' : self.year,
            'email' : self.email,
            'password': self.password
        }
        return data
        #return json.dumps(data, indent=4, sort_keys=False, default=str)


@deprecated("Events class is deprecated, use Event")
class Events:
    def __init__(self, uid, title, date_held, info, required_payment, item, amount, open):
        self.uid = uid
        self.title = title
        self.date_held = date_held
        self.info = info
        self.required_payment = required_payment
        self.item = item
        self.amount = amount
        self.open_for_payment = open
        if not self.requirePayment():
            self.open_for_payment = 'NO'

    def requirePayment(self) -> bool:
        return self.required_payment == "YES"


@deprecated("OrderAccount class is deprecated, use Orders")
class OrderAccount:
    def __init__(self, uid, event_uid, account_uid, status, quantity, reference):
        warn("This class is deprecated", DeprecationWarning, stacklevel=2)
        self.uid = uid
        self.event_uid = event_uid
        self.account_uid = account_uid
        self.status = status
        self.quantity = quantity
        self.reference = reference


class Email:
    def __init__(self, title, recipient, content):
        self.title: str = title
        self.recipient: str = recipient
        self.content: str = content


@deprecated("Order class is deprecated, use Orders")
class Order:
    def __init__(self, event: Events, account: Account, order_account: OrderAccount):
        self.event = event
        self.account = account
        self.order_account = order_account
        self.total = float(event.amount)*int(order_account.quantity)


"""
    Version 1.1
    Classes Order, OrderAccount and Events are deprecated
    
    use Event, Merchandise and Orders
"""


class Event:
    def __init__(self, uid, title, date_published, information, image_file):
        self.uid = uid
        self.title = title
        self.date_published = date_published
        self.information = information
        self.image_file = image_file


class Merchandise:
    def __init__(self, uid, title, info, price, discount, stock):
        self.uid = uid
        self.title = title
        self.info = info
        self.price = price
        self.discount = discount
        self.stock = stock
        self.image_file = ""
        self.image_file_extras = []
    
    def toJSON(self):
        data: dict = {
            'uid' : self.uid,
            'title' : self.title,
            #'info' : self.info,
            'price' : self.price,
            'discount' : self.discount,
            #'stock' : self.stock,
            #'image_file' : self.image_file,
            #'image_file_extras' : self.image_file_extras,
        }
        return data
        #return json.dumps(data, indent=4, sort_keys=False, default=str)


class MerchOrder:
    def __init__(self, uid, acc_id, order_date, merch_id, status: Enum, quantity, add_info, reference):
        self.uid = uid
        self.account_id = acc_id
        self.order_date = order_date
        self.merchandise_id = merch_id
        self.status = status
        self.quantity = quantity
        self.additional_info = add_info
        self.reference = reference
    
    def getStatus(self) -> Enum:
        return self.status

    def __str__(self):
        return f"REF: {GetReference(self.reference)} - {self.account_id} -> INFO: [{self.additional_info}]"

    def setStatus(self, status: str):
        if status == 'ORDERED':
            self.status = ORDER_STATUS.ORDERED.value
        elif status == 'PAID':
            self.status = ORDER_STATUS.PAID.value
        elif status == 'CLAIMED':
            self.status = ORDER_STATUS.CLAIMED.value
        elif status == 'CANCELLED':
            self.status = ORDER_STATUS.CANCELLED.value

    def toJSON(self):
        data: dict = {
            'uid' : self.uid,
            'account_id' : self.account_id,
            'order_date' : self.order_date,
            'merchandise_id' : self.merchandise_id,
            'status' : self.status,
            'quantity' : self.quantity,
            'additional_info' : self.additional_info,
            'reference' : self.reference,
        }
        return data
        #return json.dumps(data, indent=4, sort_keys=False, default=str)


class PSITSOfficer(Account):
    def __init__(self, account: Account, position, birthday):
        super().__init__(
            account.uid, 
            account.rfid, 
            account.firstname, 
            account.lastname, 
            account.course, 
            account.year, 
            account.email
            )
        self.position = position
        self.birthday = birthday
        self.image_src = ""

    def __str__(self):
        return "OFFICER: "+self.lastname + ", " + self.firstname + f" [{self.uid}]"

class FacultyMember:
    def __init__(self, uid, name, position, description, job):
        self.uid = uid
        self.name = name
        self.position = position
        self.description = description
        self.job = job
        self.image_src = ''


class AccountOrders():
    def __init__(self, account: Account, merch: Merchandise, order: MerchOrder):
        self.account = account
        self.merch = merch
        self.order = order
        self.reference = ''

    def getStatus(self) -> Enum:
        return self.order.status

    def getTotal(self):
        return GetPriceRef(self.order.reference)

    def toJSON(self):
        data: dict = {
            'account' : {
                'account_id': self.account.uid,
                'fullname': f'{self.account.firstname} {self.account.lastname}',
                'course': f'{self.account.course}',
                'year': self.account.year,
            },
            'merch' : {'uid':self.merch.uid},
            'order' : {
                'uid':self.order.uid,
                'order_date': f'{self.order.order_date}',
                'quantity': self.order.quantity,
                'additional_info': self.order.additional_info
            },
            'reference' : self.reference,
            'getTotal': self.getTotal(),
            'getStatus': self.getStatus() 
        }
        #return json.dumps(data,  indent=4, sort_keys=False, default=str)
        return data


class ORDER_STATUS(Enum):
    NONE = 'NONE'
    ORDERED = 'ORDERED'
    PAID = 'PAID'
    CLAIMED = 'CLAIMED'
    CANCELLED = 'CANCELLED'


class STATIC_DATA:
    PRINTING: dict = {
        'PRICE_BW': 5.0,
        'PRICE_CL': 8.0,
        'TITLE': 'Document Printing',
        'SCHED': '(Mon-Fri) 8:00am - 4:00pm'
    }


class PROMO:
    def __init__(self, uid, code, merch, discount, slot):
        self.uid: int = uid
        self.code: str = code
        self.merch: int = merch
        self.discount: float = discount
        self.slot: int = slot


class AccountOrdersLW:
    def __init__(self,idno, email, reference_code, fullname, product, info, qty, amt, status, discounted_price, order_date, size):
        self.ref_code = reference_code
        self.fullname = fullname
        self.product = product
        self.info = info
        self.quantity = qty
        self.amount = amt
        self.status = status
        self.discounted_price = discounted_price
        self.order_date = order_date
        self.size = size
        self.idno = idno
        self.email = email
        self.course_year = '';

    @staticmethod
    def parse(accountOrder: AccountOrders):
        # Determine the sizes
        size: str = ''
        for item in accountOrder.order.additional_info.split('\n'):
            if 'size' in item.lower():
                if len(item.split(':')) > 1:
                    size = size + item.split(':')[1].strip() + ', '
        a_data = AccountOrdersLW(
            accountOrder.account.uid,
            accountOrder.account.email,
            accountOrder.reference,
            f'{accountOrder.account.lastname}, {accountOrder.account.firstname}',
            accountOrder.merch.title,
            accountOrder.order.additional_info,
            accountOrder.order.quantity,
            accountOrder.merch.price,
            accountOrder.getStatus(),
            GetPriceRef(accountOrder.order.reference),
            accountOrder.order.order_date,
            size[:-2]
            )
        a_data.course_year =f'{accountOrder.account.course}-{accountOrder.account.year}'
        return a_data

    def toJSON(self):
        data: dict = {
            "reference": self.ref_code,
            "fullname": self.fullname,
            "product": self.product,
            "info": self.info,
            "size": self.size,
            "quantity": self.quantity,
            "amount": self.amount,
            "discounted_price": self.discounted_price,
            "order_date":self.order_date,
            "status": self.status,
        }
        #return json.dumps(data,  indent=4, sort_keys=False, default=str)
        return data
    
    def equals(self, __o: object) -> bool:
        # Only the status, info and quantity will be compared
        if str(self.ref_code) == str(__o.ref_code) and self.quantity == __o.quantity and str(self.status) == str(__o.status) and str(self.info) == str(__o.info) and str(self.size) == str(__o.size):
            return True
        return False

class Quiz:
    def __init__(self, QuizTopic, Questionaires, QuizOwner, CreationDate, CreationTime):
        self.QuizTopic = QuizTopic
        self.Quiz: list = Questionaires
        self.QuizOwner = QuizOwner
        self.CreationDate = CreationDate
        self.CreationTime = CreationTime
        self.ShowProfile = ''

    def toJSON(self):
        return {
            'QuizTopic':self.QuizTopic,
            'Quiz': [x.toJSON() for x in self.Quiz],
            'QuizOwner': self.QuizOwner,
            'CreationDate': self.CreationDate,
            'CreationTime': self.CreationTime,
            'ShowProfile': self.ShowProfile
        }

class Questionaires:
    def __init__(self, QuizID, QuizQuestion, QuizAnswers, QuizAnswer, QuestionTimer, Type):
        self.QuizID = QuizID
        self.QuizQuestion = QuizQuestion
        self.QuizAnswers = QuizAnswers
        self.QuizAnswer = QuizAnswer
        self.QuestionTimer = QuestionTimer
        self.Type = Type
        

    def toJSON(self):
        return {
            'QuizID': self.QuizID,
            'QuizQuestion': self.QuizQuestion,
            'QuizAnswers': self.QuizAnswers,
            'QuizAnswer': self.QuizAnswer,
            'QuestionTimer': self.QuestionTimer,
            'Type': self.Type,
        }

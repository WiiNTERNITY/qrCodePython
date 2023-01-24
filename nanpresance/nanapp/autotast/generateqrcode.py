import hashlib
# import uuid
from ..models import *
import random
import string

def sendrandomnumber():
    return random.randrange(50)

def randomString(stringLength):

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generateqr():
    number = sendrandomnumber()
    mot = randomString(number)
    m = hashlib.sha224('{}'.format(mot).encode()).hexdigest()

    try:
        new_qr_code = Qrcode.objects.filter(jours=date.today(),status=True)[:1].get()
        new_qr_code.titre_slug= m
        new_qr_code.save()
    except:
        pass
    return m

 
    








# Python3.9.18
# Overwrite from old component

import os

from datetime import datetime
from pypromptpay import qr_code


# Set global path
## EX. os.path.join(BASE_DIR, 'next_folder/')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.join(BASE_DIR, 'THAI_QRCODE/')

def generate_qr_code(account:str, currency:str, money:str):
    # Check if the directory 'QRCODE' exists; create it if not
    qr_code_dir = os.path.join(PROJECT_PATH, 'QRCODE/')
    print(qr_code_dir)
    if not os.path.exists(qr_code_dir):
        os.makedirs(name=qr_code_dir)

    # Generate QRCode
    qr_code(
        account=account,
        one_time=False, 
        path_qr_code=os.path.join(qr_code_dir, f"qrcode_{account}_{currency}_{datetime.now().strftime('%Y%m%d%H%M%S')}.PNG"), 
        country="TH", 
        money=money, 
        currency=currency
    )

if __name__ == "__main__":
    generate_qr_code(
        account='1409800272962',
        currency='THB',
        money='20'
    )
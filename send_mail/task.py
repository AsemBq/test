from celery import shared_task,app
from .sendMail import SendEmail
from .models import Plan
import requests
import time


def ETH_Checker(Amount):
    walletadrres = '0x0A1262EBF4229a7Bbf9A621b1da446e92992F279'
    url = f"https://api-sepolia.etherscan.io/api?module=account&action=txlist&address={walletadrres}&startblock=4758223&endblock=99999999&offset=10&sort=desc&apikey=DM2GJAWGAPN23P59NKRTIQTXVNAKKEZNKN"
    block = requests.get(url).json()
    block = block['result']
    block = int(block[0]['blockNumber'])
    url = f"https://api-sepolia.etherscan.io/api?module=account&action=txlist&address={walletadrres}&startblock={block + 1}&endblock=99999999&offset=10&sort=desc&apikey=DM2GJAWGAPN23P59NKRTIQTXVNAKKEZNKN"
    x = 1
    print("Start checking")
    while x <= 40:
        x += 1
        h = requests.get(url).json()
        for i in h['result']:
            if i['to'] == walletadrres.lower():
                value = i['value']
                value = float(value) * 10 ** -18
                value = round(value, 4)
                if value == Amount:
                    print('finded')
                    return True
                else:
                    print('Chacking Again')
        time.sleep(60)
        if x == 60:
            return False
@shared_task(bind=True,name='hahaha')
def Deposit_maker(self,*args,**kwargs):

    SendEmail('asem.b7460611@gmail.com')

    return 'ok'
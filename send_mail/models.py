import qrcode
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

class Plan(models.Model):
    title=models.CharField(max_length=50)
    day=models.IntegerField()
    ex=models.BooleanField()

    def __str__(self):
        return f'{self.id}---{self.ex}'








# class Wallets(models.Model):
#     name=models.CharField(max_length=20)
#     Crypto_wallet=models.CharField(max_length=100)
#     qr_code=models.ImageField(upload_to='qrCode',blank=True)
#
#     def __str__(self):
#         return self.name
#
#     def save(self,*args,**kwargs):
#         qrcode_img=qrcode.make(self.Crypto_wallet)
#         canves=Image.new('RGB',(290,290),'white')
#         draw=ImageDraw.Draw(canves)
#         canves.paste(qrcode_img)
#         fname=f'qr_code{self.name}.png'
#         buffer=BytesIO()
#         canves.save(buffer,'PNG')
#         self.qr_code.save(fname,File(buffer),save=False)
#         canves.close()
#         super().save(*args,**kwargs)
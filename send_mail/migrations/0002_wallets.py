# Generated by Django 4.2.7 on 2023-11-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Crypto_wallet', models.CharField(max_length=100)),
                ('qr_code', models.ImageField(blank=True, upload_to='qrCode')),
            ],
        ),
    ]
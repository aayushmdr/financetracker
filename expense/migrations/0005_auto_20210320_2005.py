# Generated by Django 3.1.6 on 2021-03-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_auto_20210320_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images/incomes'),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-09 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20210709_0836'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sale',
            new_name='Order',
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['-quantity']},
        ),
    ]

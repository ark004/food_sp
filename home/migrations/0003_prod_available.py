# Generated by Django 2.2 on 2022-05-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220422_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
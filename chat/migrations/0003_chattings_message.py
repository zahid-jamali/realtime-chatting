# Generated by Django 4.1.7 on 2023-04-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_rooms_chattings'),
    ]

    operations = [
        migrations.AddField(
            model_name='chattings',
            name='message',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]

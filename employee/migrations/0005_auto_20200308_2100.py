# Generated by Django 3.0.3 on 2020-03-08 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_reply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name': 'Reply', 'verbose_name_plural': 'Replies'},
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_status',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-09 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='country',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default=1010, max_length=250),
            preserve_default=False,
        ),
    ]
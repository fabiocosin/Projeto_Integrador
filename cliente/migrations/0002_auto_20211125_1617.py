# Generated by Django 3.2.9 on 2021-11-25 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='data_nascimento',
            new_name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='ativa',
        ),
    ]

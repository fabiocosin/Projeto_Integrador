# Generated by Django 3.2.9 on 2021-11-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20211125_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_alter_contato_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

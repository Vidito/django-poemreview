# Generated by Django 4.2.2 on 2023-06-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0004_alter_poem_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='excerpt',
            field=models.TextField(max_length=100, null=True),
        ),
    ]

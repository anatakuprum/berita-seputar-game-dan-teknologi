# Generated by Django 4.1.2 on 2022-12-09 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='posting',
            options={'verbose_name_plural': 'Posting'},
        ),
    ]
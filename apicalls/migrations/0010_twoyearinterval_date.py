# Generated by Django 3.1.2 on 2021-05-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0009_twoyearinterval'),
    ]

    operations = [
        migrations.AddField(
            model_name='twoyearinterval',
            name='date',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
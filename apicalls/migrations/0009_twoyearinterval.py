# Generated by Django 3.1.2 on 2021-05-08 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0008_averagesale'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoYearInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apicalls.petroleum')),
            ],
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0002_auto_20210115_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/%Y%m%d/')),
            ],
        ),
    ]

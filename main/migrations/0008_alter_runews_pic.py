# Generated by Django 4.0.6 on 2022-08-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_runews_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runews',
            name='pic',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
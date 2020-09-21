# Generated by Django 3.1.1 on 2020-09-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='imageUrl',
            field=models.ImageField(blank=True, null=True, upload_to='menu/'),
        ),
        migrations.AddField(
            model_name='category',
            name='linkUrl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
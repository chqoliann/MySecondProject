# Generated by Django 5.0.4 on 2024-05-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumiluxe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='image',
            field=models.ImageField(upload_to='perfume_images/'),
        ),
    ]

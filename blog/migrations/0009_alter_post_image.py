# Generated by Django 4.2.17 on 2025-01-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog\\default.jpg', upload_to='blog/'),
        ),
    ]

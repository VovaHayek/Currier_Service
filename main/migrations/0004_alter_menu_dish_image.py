# Generated by Django 4.1.7 on 2023-02-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_menu_dish_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dish_image',
            field=models.ImageField(upload_to='dishes/'),
        ),
    ]

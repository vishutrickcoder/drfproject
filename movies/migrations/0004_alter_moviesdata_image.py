# Generated by Django 4.0.3 on 2023-01-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_moviesdata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdata',
            name='image',
            field=models.ImageField(default='Images/None/no_img.png', upload_to='Images/'),
        ),
    ]

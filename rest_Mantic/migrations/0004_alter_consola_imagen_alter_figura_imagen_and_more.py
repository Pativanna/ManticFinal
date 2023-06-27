# Generated by Django 4.2.1 on 2023-06-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_Mantic', '0003_rename_nombrecategoria_categoria_idcategoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consola',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media-files/consolapictures/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='figura',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media-files/figurapictures/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media-files/juegopictures/%Y/%m/%d/'),
        ),
    ]

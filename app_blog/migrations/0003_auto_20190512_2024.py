# Generated by Django 2.1.7 on 2019-05-12 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_auto_20190512_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='data_piblicacao',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='descricao',
            field=models.CharField(max_length=256, verbose_name='Descriçaõ'),
        ),
    ]

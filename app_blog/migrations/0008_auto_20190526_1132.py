# Generated by Django 2.1.7 on 2019-05-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0007_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensagemDeContato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('mensagem', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Mensagem de Contato',
                'verbose_name_plural': 'Mensagens de Contato',
            },
        ),
        migrations.DeleteModel(
            name='Contato',
        ),
    ]
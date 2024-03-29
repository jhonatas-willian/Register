# Generated by Django 5.0.1 on 2024-01-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nascimento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='phone',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sobrenome',
            field=models.TextField(blank=True),
        ),
    ]

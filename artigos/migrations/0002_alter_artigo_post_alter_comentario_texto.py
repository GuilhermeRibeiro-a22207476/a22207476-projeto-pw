# Generated by Django 4.0.6 on 2024-03-19 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='post',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(),
        ),
    ]

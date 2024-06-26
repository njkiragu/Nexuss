# Generated by Django 5.0.2 on 2024-02-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_remove_block_block_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chain',
            name='code',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='chain',
            name='name',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='chain',
            name='sem',
            field=models.CharField(default='null', max_length=30),
        ),
        migrations.AlterField(
            model_name='chain',
            name='slot',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='chain',
            name='strength',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='chain',
            name='year',
            field=models.IntegerField(default='null'),
        ),
    ]

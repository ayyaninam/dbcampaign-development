# Generated by Django 4.2.5 on 2023-09-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_newsletteremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newsletteremail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

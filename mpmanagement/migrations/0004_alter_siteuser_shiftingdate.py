# Generated by Django 4.0.1 on 2022-01-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpmanagement', '0003_siteuser_shiftingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='shiftingdate',
            field=models.DateField(null=True),
        ),
    ]
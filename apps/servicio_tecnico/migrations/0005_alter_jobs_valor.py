# Generated by Django 3.2.9 on 2021-11-03 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_tecnico', '0004_auto_20210909_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
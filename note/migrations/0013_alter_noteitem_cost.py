# Generated by Django 4.0.1 on 2022-04-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0012_noteitem_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteitem',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]

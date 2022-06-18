# Generated by Django 4.0.4 on 2022-06-07 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0017_alter_product_carat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carat',
            name='carat',
            field=models.SmallIntegerField(default=21),
        ),
        migrations.AlterField(
            model_name='cost',
            name='carat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='note.carat'),
        ),
        migrations.AlterField(
            model_name='product',
            name='carat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='note.carat'),
        ),
    ]

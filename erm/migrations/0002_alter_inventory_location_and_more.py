# Generated by Django 4.0.1 on 2022-02-10 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0001_initial'),
        ('erm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='erm.location'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='util.userprofile'),
        ),
        migrations.AlterField(
            model_name='purchaseorderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erm.product'),
        ),
    ]
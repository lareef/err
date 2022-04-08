# Generated by Django 4.0.1 on 2022-02-11 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0001_initial'),
        ('erm', '0004_alter_purchaseorder_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='util.userprofile'),
        ),
    ]

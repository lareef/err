# Generated by Django 4.0.1 on 2022-04-09 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_alter_client_client_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='note.location'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-04-11 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_inv_updated_on_noteitem_updated_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='PR',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.note')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.note',),
        ),
        migrations.CreateModel(
            name='PRItem',
            fields=[
                ('noteitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.noteitem')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.noteitem',),
        ),
        migrations.CreateModel(
            name='SR',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.note')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.note',),
        ),
        migrations.CreateModel(
            name='SRItem',
            fields=[
                ('noteitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.noteitem')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.noteitem',),
        ),
        migrations.CreateModel(
            name='WI',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.note')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.note',),
        ),
        migrations.CreateModel(
            name='WIItem',
            fields=[
                ('noteitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.noteitem')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.noteitem',),
        ),
        migrations.CreateModel(
            name='WR',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.note')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.note',),
        ),
        migrations.CreateModel(
            name='WRItem',
            fields=[
                ('noteitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.noteitem')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.noteitem',),
        ),
    ]

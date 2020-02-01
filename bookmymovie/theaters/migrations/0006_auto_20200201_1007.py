# Generated by Django 3.0.2 on 2020-02-01 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theaters', '0005_row'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='theater',
        ),
        migrations.AlterField(
            model_name='seat',
            name='row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theaters.Row'),
        ),
    ]
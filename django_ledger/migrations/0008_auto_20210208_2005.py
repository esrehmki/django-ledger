# Generated by Django 3.1.4 on 2021-02-09 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0007_auto_20210208_2005'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='ledgermodel',
            index=models.Index(fields=['unit'], name='django_ledg_unit_id_32f073_idx'),
        ),
    ]
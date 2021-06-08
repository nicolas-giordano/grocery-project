# Generated by Django 3.2.4 on 2021-06-07 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_storeitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitems',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pages.store'),
        ),
    ]
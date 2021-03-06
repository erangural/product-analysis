# Generated by Django 2.1.5 on 2019-04-09 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190409_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rating',
            new_name='review',
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]

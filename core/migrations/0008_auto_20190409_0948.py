# Generated by Django 2.1.5 on 2019-04-09 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190409_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-11-03 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20221102_2149'),
        ('reviews', '0003_auto_20221102_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='foodtag_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='stores.foodtag'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='thematag_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='stores.thematag'),
            preserve_default=False,
        ),
    ]
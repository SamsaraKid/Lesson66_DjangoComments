# Generated by Django 4.2.7 on 2023-11-01 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='kino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='comments.kino'),
        ),
    ]

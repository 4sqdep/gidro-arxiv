# Generated by Django 4.2.16 on 2024-10-14 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_files_calendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='doc_type',
            field=models.BooleanField(default=False, verbose_name='Dokumoent turi'),
        ),
        migrations.AlterField(
            model_name='folders',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category', verbose_name='Kategoriya'),
        ),
    ]

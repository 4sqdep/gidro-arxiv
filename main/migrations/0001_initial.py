# Generated by Django 4.2.16 on 2024-11-24 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kategoriya nomi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kategoriya kiritilgan vaqti')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Hujjat turi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan vaqti')),
            ],
            options={
                'verbose_name': 'Hujjat turi',
                'verbose_name_plural': 'Hujjat turlari',
            },
        ),
        migrations.CreateModel(
            name='Folders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=25, verbose_name='Papka nomeri')),
                ('name', models.CharField(max_length=500, verbose_name='Papka nomi')),
                ('doc_type', models.BooleanField(default=False, verbose_name='Hujjat turi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Papka kiritilgan vaqti')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category', verbose_name='Kategoriya')),
            ],
            options={
                'verbose_name': 'Papka',
                'verbose_name_plural': 'Papakalar',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar', models.CharField(blank=True, max_length=20, null=True, verbose_name='Hujjat sanasi')),
                ('file_code', models.CharField(max_length=20, verbose_name='Fayil kodi')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d', verbose_name='Fayil')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan vaqti')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.documenttype', verbose_name='Hujjat turi')),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.folders', verbose_name='Papka')),
            ],
            options={
                'verbose_name': 'Fayil',
                'verbose_name_plural': 'Fayillar',
            },
        ),
    ]

# Generated by Django 3.2.11 on 2022-03-13 21:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=250, verbose_name='rank')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('artist', models.CharField(max_length=250, verbose_name='artist')),
                ('peak', models.CharField(max_length=250, verbose_name='peak')),
                ('weeks', models.CharField(max_length=250, verbose_name='weeks')),
            ],
        ),
        migrations.CreateModel(
            name='CancionesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduccion', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
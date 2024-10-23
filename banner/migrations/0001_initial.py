# Generated by Django 5.1.1 on 2024-10-23 11:18

import django.db.models.manager
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=250, verbose_name='message de la bannière')),
                ('date_de_publication', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de la publication du message')),
            ],
            options={
                'verbose_name': 'Message de la bannière',
                'verbose_name_plural': 'Messages de la bannière',
                'ordering': ['-date_de_publication'],
            },
            managers=[
                ('objects_random', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel', verbose_name='image du carousel')),
                ('categorie', models.CharField(choices=[('evenement', 'évènement'), ('billet', 'billet de blog'), ('livre', 'livre'), ('news', 'news'), ('technique', 'technique')], max_length=250, verbose_name='catégorie du carousel')),
                ('titre', models.CharField(max_length=250, verbose_name='titre du carousel')),
                ('date_de_publication', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de publication')),
                ('state', models.BooleanField(verbose_name='état de publication')),
                ('texte', models.CharField(default='Aucun texte descriptif', max_length=250, verbose_name='texte brève decrivant le carousel')),
                ('slug', models.SlugField(max_length=250, verbose_name='Slug pour le lien')),
            ],
            options={
                'verbose_name': 'Element du carousel',
                'verbose_name_plural': 'Elements du carousel',
                'ordering': ['-date_de_publication'],
            },
            managers=[
                ('publicated_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
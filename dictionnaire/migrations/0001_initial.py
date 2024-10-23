# Generated by Django 5.1.1 on 2024-10-23 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terme', models.CharField(help_text='Entrez le mot à définir', max_length=250, verbose_name='Mot défini')),
                ('definition', models.TextField(help_text='Entrez la définition du mot en détaillant le plus possible (vous pouvez utilisez les outils de codification )', verbose_name='Définition du mot')),
                ('slug', models.SlugField(help_text='Entrez un slug valide pour le référencement du mot sur le web', verbose_name='Slug pour le référencement')),
            ],
        ),
        migrations.CreateModel(
            name='ImageMot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='dictionnaire/mot/%Y', verbose_name='Photo descriptif du mot')),
                ('publier', models.BooleanField(verbose_name='La Photo doit-elle être publier')),
                ('credit', models.CharField(blank=True, max_length=50, null=True, verbose_name='Credit de la photo')),
                ('mot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionnaire.mot', verbose_name='mot lié à la photo')),
            ],
            options={
                'verbose_name': 'ImageMot',
                'verbose_name_plural': 'ImageMots',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auteur', models.CharField(max_length=250, verbose_name="Nom de l'auteur ou des auteurs de la source")),
                ('nom', models.CharField(max_length=100, verbose_name="Titre du livre ou nom de l'article de parution du mot")),
                ('year', models.CharField(max_length=6, verbose_name='Annee de la publication')),
                ('site', models.URLField(verbose_name='Url du site web de la publication')),
                ('mot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionnaire.mot', verbose_name='mot lié à la source')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
    ]

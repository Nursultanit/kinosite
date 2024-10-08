# Generated by Django 4.2.15 on 2024-08-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='actor_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='actor_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='bio_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='bio_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='bio_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='bio_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='director_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='director_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

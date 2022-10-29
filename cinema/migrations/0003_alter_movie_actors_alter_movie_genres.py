# Generated by Django 4.1 on 2022-10-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(blank=True, to="cinema.actor"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(blank=True, to="cinema.genre"),
        ),
    ]

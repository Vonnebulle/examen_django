# Generated by Django 2.2.1 on 2019-06-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0008_remove_auteur_manga'),
    ]

    operations = [
        migrations.AddField(
            model_name='auteur',
            name='histoire',
            field=models.TextField(null=True),
        ),
    ]
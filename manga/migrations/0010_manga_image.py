# Generated by Django 2.2.1 on 2019-06-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0009_auteur_histoire'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]

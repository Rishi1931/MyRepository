# Generated by Django 3.1.1 on 2020-09-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_destination1'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination1',
            name='desc1',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination1',
            name='desc2',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination1',
            name='desc3',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination1',
            name='desc4',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination1',
            name='desc5',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]

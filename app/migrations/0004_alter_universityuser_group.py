# Generated by Django 3.2.7 on 2021-09-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210917_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityuser',
            name='group',
            field=models.ManyToManyField(blank=True, default=None, to='app.UserGroup'),
        ),
    ]

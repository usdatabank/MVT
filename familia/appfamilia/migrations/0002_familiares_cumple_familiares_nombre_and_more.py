# Generated by Django 4.0.3 on 2022-04-06 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfamilia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiares',
            name='cumple',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='familiares',
            name='nombre',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='familiares',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-31 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stduent',
            name='IsDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stduent',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stduent',
            name='email',
            field=models.EmailField(default='chadaniale123@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='stduent',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0006_group_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupuser',
            name='status',
            field=models.CharField(choices=[('C', 'Creator'), ('M', 'Member'), ('I', 'Invited')], max_length=1),
        ),
    ]

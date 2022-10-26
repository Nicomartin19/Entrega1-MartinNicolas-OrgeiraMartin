# Generated by Django 4.1.2 on 2022-10-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]

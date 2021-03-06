# Generated by Django 2.1.7 on 2019-11-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('meal', models.CharField(blank=True, choices=[('Breakfast', 'breakfast'), ('Brunch', 'brunch'), ('Lunch', 'lunch'), ('Dinner', 'dinner')], max_length=255)),
                ('location', models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-29 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('average_rating', models.IntegerField(default=0)),
                ('brewery', models.CharField(max_length=200)),
                ('beer_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=256)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate_beer.Beer')),
            ],
        ),
    ]

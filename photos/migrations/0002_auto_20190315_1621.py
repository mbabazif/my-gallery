# Generated by Django 2.1.7 on 2019-03-15 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image']},
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Category'),
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
        ),
    ]

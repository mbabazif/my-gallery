# Generated by Django 2.1.7 on 2019-03-18 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_image_p_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='Images/')),
                ('name', models.CharField(max_length=30)),
                ('descripton', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='location',
            name='location_name',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='images',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Category'),
        ),
        migrations.AddField(
            model_name='images',
            name='location_taken',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
        ),
    ]

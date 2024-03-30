# Generated by Django 4.2.10 on 2024-03-30 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='created_at',
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='recipe_images/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=''),
        ),
    ]
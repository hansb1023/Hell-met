# Generated by Django 3.2.4 on 2021-06-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='run_images')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
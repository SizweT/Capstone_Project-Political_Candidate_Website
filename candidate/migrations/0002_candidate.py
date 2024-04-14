# Generated by Django 5.0.3 on 2024-03-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='candidate_photos/')),
            ],
        ),
    ]
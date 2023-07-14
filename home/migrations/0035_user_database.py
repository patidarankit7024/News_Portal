# Generated by Django 4.1.5 on 2023-07-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_rename_heading_upload_caption_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('midlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(default='0000000000', max_length=10)),
                ('adress', models.CharField(default='no', max_length=50)),
                ('school', models.CharField(default='no', max_length=50)),
                ('collage', models.CharField(default='no', max_length=60)),
                ('qualification', models.ImageField(upload_to='img/%y')),
                ('image', models.ImageField(upload_to='img/%y')),
                ('usertype', models.CharField(default='user', max_length=50)),
            ],
        ),
    ]
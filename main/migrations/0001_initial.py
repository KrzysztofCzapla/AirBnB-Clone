# Generated by Django 3.2.5 on 2023-01-20 16:37

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='User', max_length=20)),
                ('bio', models.CharField(default='No Description', max_length=50)),
                ('phoneNumber', models.CharField(default='Not Added', max_length=15)),
                ('eMail', models.CharField(default='Not Added', max_length=50)),
                ('user', models.OneToOneField(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OffertType', models.CharField(choices=[('Buy', 'Buy'), ('Rent', 'Rent')], default='Rent', max_length=4)),
                ('PropertyType', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment')], default='House', max_length=9)),
                ('title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Published: ')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=15)),
                ('meters', models.DecimalField(decimal_places=0, default=0, max_digits=15)),
                ('city', models.CharField(default=None, max_length=50)),
                ('author', models.ForeignKey(default=main.models.Profile, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='images/', verbose_name='Image')),
                ('post', models.ForeignKey(default=main.models.Post, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='main.post')),
            ],
        ),
    ]
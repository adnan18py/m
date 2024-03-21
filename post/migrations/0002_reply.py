# Generated by Django 5.0.1 on 2024-03-18 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='نام کاربری')),
                ('text', models.TextField(verbose_name='متن پاسخ')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.comment')),
            ],
        ),
    ]

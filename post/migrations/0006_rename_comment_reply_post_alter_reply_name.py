# Generated by Django 5.0.1 on 2024-03-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_rename_post_reply_comment_alter_reply_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='comment',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='reply',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='نام کاربری'),
        ),
    ]
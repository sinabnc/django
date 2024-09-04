# Generated by Django 5.1 on 2024-09-04 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_article_contact_article_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='meta_tag',
        ),
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='meta_title',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]

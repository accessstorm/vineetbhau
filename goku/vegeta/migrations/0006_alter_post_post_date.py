# Generated by Django 4.2.16 on 2024-10-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegeta', '0005_rename_category_post_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

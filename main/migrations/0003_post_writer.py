# Generated by Django 4.1.6 on 2023-03-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_post_updated_at_alter_post_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="writer",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
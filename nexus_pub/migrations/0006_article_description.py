# Generated by Django 3.2 on 2023-07-02 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_pub', '0005_auto_20230702_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]

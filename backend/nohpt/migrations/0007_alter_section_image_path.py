# Generated by Django 4.0.5 on 2024-02-17 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nohpt', '0006_alter_section_audio_path_alter_section_image_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='image_path',
            field=models.URLField(blank=True, max_length=700, null=True),
        ),
    ]

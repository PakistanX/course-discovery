# Generated by Django 2.2.16 on 2022-07-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0251_add_honor_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='card_image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='card_image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='leveltypetranslation',
            name='name_t',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
    ]
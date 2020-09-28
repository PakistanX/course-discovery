# Generated by Django 2.2.13 on 2020-08-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0252_auto_20200624_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'get_latest_by': 'created', 'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='leveltypetranslation',
            name='name_t',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
    ]
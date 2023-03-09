# Generated by Django 4.1.7 on 2023-03-09 14:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=400, unique=True, verbose_name='slug')),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='datetime_created')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='categories.category', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
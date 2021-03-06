# Generated by Django 4.0.4 on 2022-04-28 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=200)),
                ('book_cat', models.CharField(choices=[('CO', 'COMIC'), ('FA', 'FANTASY'), ('AC', 'ACTION'), ('TH', 'THRILLER'), ('CN', 'CONTEMPORARY')], max_length=2)),
                ('book_cover', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('book_desc', models.CharField(max_length=200)),
                ('book_pubd', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_uuid', models.UUIDField(editable=False, unique=True)),
                ('last_viewed', models.DateTimeField()),
                ('archived', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

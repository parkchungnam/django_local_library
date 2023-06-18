# Generated by Django 4.0.2 on 2023-04-12 12:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book.', to='catalog.Genre'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid1, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]

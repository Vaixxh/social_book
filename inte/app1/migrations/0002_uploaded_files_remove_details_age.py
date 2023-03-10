# Generated by Django 4.1.5 on 2023-01-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploaded_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Visibility', models.BooleanField(default=False)),
                ('Cost', models.PositiveIntegerField(null=True)),
                ('Year', models.SmallIntegerField(null=True)),
                ('Cover', models.ImageField(upload_to='media/image/')),
                ('Book', models.FileField(upload_to='media/pdf/')),
            ],
        ),
        migrations.RemoveField(
            model_name='details',
            name='age',
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Anonymous', max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]

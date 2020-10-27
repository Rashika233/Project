# Generated by Django 2.1.7 on 2020-10-20 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='first_app.training'),
        ),
    ]
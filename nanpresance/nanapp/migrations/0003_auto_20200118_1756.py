# Generated by Django 2.2.5 on 2020-01-18 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nanapp', '0002_auto_20200112_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='decompte',
            field=models.TimeField(default='08:00', null=True),
        ),
        migrations.AlterField(
            model_name='groupe',
            name='nom',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contacts',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genre',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='groupe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_groupe', to='nanapp.Groupe'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='specialite',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
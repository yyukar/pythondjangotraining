# Generated by Django 3.2.13 on 2023-11-22 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gelisimTakip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ipsumuyebilgi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinsiyet', models.CharField(max_length=50)),
                ('yas', models.IntegerField()),
                ('uye', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gelisimTakip.ipsumuye')),
            ],
        ),
    ]
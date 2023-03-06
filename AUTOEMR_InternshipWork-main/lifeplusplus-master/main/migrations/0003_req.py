# Generated by Django 2.2 on 2019-06-10 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_delete_req'),
    ]

    operations = [
        migrations.CreateModel(
            name='Req',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('req_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_by', to='main.Profile')),
                ('req_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_for', to='main.Profile')),
            ],
        ),
    ]

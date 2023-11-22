# Generated by Django 4.2.6 on 2023-10-28 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_delete_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='Media/Yt_Thumbnail')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='video%y')),
                ('time_duration', models.FloatField(null=True)),
                ('preview', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lessons')),
            ],
        ),
    ]

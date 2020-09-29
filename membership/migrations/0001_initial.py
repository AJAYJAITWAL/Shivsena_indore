# Generated by Django 3.0.5 on 2020-08-31 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=250)),
                ('last_name', models.SlugField(max_length=250)),
                ('ward_no', models.IntegerField(max_length=3)),
                ('assembly', models.CharField(max_length=50)),
                ('contact', models.PositiveIntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('post', models.CharField(max_length=100)),
                ('tenure1', models.PositiveIntegerField(max_length=4)),
                ('tenure2', models.PositiveIntegerField(default='Till-Now', max_length=4)),
                ('position', models.CharField(max_length=250)),
                ('blood_g', models.CharField(max_length=20)),
                ('education', models.CharField(max_length=200)),
                ('pyear', models.IntegerField(max_length=4)),
                ('occupation', models.CharField(max_length=220)),
                ('uidai', models.PositiveIntegerField(max_length=12)),
            ],
        ),
    ]

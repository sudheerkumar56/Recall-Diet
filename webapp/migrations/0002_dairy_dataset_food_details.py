# Generated by Django 3.1.3 on 2024-02-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dairy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=149)),
                ('food_name', models.CharField(max_length=149)),
                ('dat_e', models.CharField(max_length=149)),
                ('wee_k', models.CharField(max_length=149)),
                ('mont_h', models.CharField(max_length=149)),
                ('v_a', models.FloatField()),
                ('v_b', models.FloatField()),
                ('v_c', models.FloatField()),
                ('v_b12', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fiber', models.FloatField()),
                ('sugars', models.FloatField()),
                ('calcium', models.FloatField()),
                ('iron', models.FloatField()),
                ('iodine', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=149)),
                ('gender', models.CharField(max_length=149)),
                ('period', models.CharField(max_length=149)),
                ('v_a', models.FloatField()),
                ('v_b', models.FloatField()),
                ('v_c', models.FloatField()),
                ('v_b12', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fiber', models.FloatField()),
                ('sugars', models.FloatField()),
                ('calcium', models.FloatField()),
                ('iron', models.FloatField()),
                ('iodine', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='food_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=149)),
                ('v_a', models.FloatField()),
                ('v_b', models.FloatField()),
                ('v_c', models.FloatField()),
                ('v_b12', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fiber', models.FloatField()),
                ('sugars', models.FloatField()),
                ('calcium', models.FloatField()),
                ('iron', models.FloatField()),
                ('iodine', models.FloatField()),
            ],
        ),
    ]

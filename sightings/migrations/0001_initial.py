# Generated by Django 2.2.7 on 2019-11-29 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=10, help_text='Latitude', max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=10, help_text='Longitude', max_digits=15)),
                ('unique_squirrel_id', models.IntegerField(help_text='ID')),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift', max_length=16)),
                ('date', models.DateField(help_text='Date')),
                ('age', models.CharField(choices=[('Juvenile', 'Juvenile'), ('Adult', 'Adult')], help_text='Age', max_length=16)),
                ('primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Primary Fur Color', max_length=16)),
                ('location', models.CharField(choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], help_text='Location', max_length=16)),
                ('specific_location', models.TextField(help_text='Commentart')),
                ('running', models.BooleanField(help_text='Squirrel was seen running')),
                ('chasing', models.BooleanField(help_text='Squirrel was seen chasing')),
                ('climbing', models.BooleanField(help_text='Squirrel was seen climbing')),
                ('eating', models.BooleanField(help_text='Squirrel was seen eating')),
                ('foraging', models.BooleanField(help_text='Squirrel was seen foraging')),
                ('other_activities', models.TextField(help_text='Other Activities')),
                ('kuks', models.BooleanField(help_text='Squirrel was heard kukking')),
                ('quaas', models.BooleanField(help_text='Squirrel was heard quaaing')),
                ('moans', models.BooleanField(help_text='Squirrel was heard moaning')),
                ('tail_flags', models.BooleanField(help_text='Squirrel was seen flagging its tail')),
                ('tail_twitches', models.BooleanField(help_text='Squirrel was seen twitching its tail')),
                ('approaches', models.BooleanField(help_text='Squirrel was seen approaching human')),
                ('indifferent', models.BooleanField(help_text='Squirrel was indifferent to human presence')),
                ('runs_from', models.BooleanField(help_text='Squirrel was seen running from humans')),
            ],
        ),
    ]

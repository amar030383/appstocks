# Generated by Django 4.0.1 on 2022-01-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nse', '0005_remove_getstocksdailydata_isincode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Down1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Down2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Down3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Down4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Down5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Jump10',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Jump12',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Jump15',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Jump5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='Jump8',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='rise2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='rise3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='rise4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='rise5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysedstocksdata',
            name='rise6',
            field=models.IntegerField(null=True),
        ),
    ]

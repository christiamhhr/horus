# Generated by Django 3.2.8 on 2021-10-15 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20211015_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categoria',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='categ',
            field=models.ManyToManyField(to='erp.Category'),
        ),
    ]

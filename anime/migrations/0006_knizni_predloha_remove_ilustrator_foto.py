# Generated by Django 4.2 on 2023-05-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_autor_alter_ilustrator_options_ilustrator_foto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knizni_predloha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titul', models.CharField(help_text='Zadej název knižní předlohy', max_length=50, verbose_name='Název knižní předlohy')),
                ('rok_vydani', models.IntegerField(help_text='Zadej rok vydání knižní předlohy', verbose_name='Rok vydání knižní předlohy')),
                ('pocet_stran', models.IntegerField(help_text='Zadej počet stran', verbose_name='Počet stran')),
                ('hodnoceni', models.CharField(help_text='Zadej hodnocení', max_length=2, verbose_name='Hodnocení')),
                ('obalka', models.ImageField(blank=True, help_text='Nahrejte obálku', null=True, upload_to='knizni_predlohy', verbose_name='Obálka knižní předlohy')),
            ],
            options={
                'verbose_name': 'Knižní předloha',
                'verbose_name_plural': 'Knižní předlohy',
                'ordering': ['titul'],
            },
        ),
        migrations.RemoveField(
            model_name='ilustrator',
            name='foto',
        ),
    ]
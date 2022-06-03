# Generated by Django 4.0.4 on 2022-05-12 10:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cat', models.CharField(max_length=155)),
                ('image_cat', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('Description', models.TextField()),
                ('date_add', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='newCommands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_nom', models.CharField(max_length=55)),
                ('client_prenom', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=13)),
                ('name_command', models.CharField(max_length=255)),
                ('ville', models.CharField(choices=[('casa', 'CasaBlanca')], default='casa', max_length=255)),
                ('Description', models.TextField()),
                ('Adreess', models.TextField()),
                ('date_Start', models.DateField()),
                ('argunce', models.CharField(choices=[('Intervention urgente', 'Intervention urgente'), ('Intervention non urgente', 'Intervention non urgente')], max_length=255)),
                ('Durre_work', models.CharField(choices=[('un jour', 'un jour '), ('2 jour', '2 jour '), ('3 jour', '3 jour '), ('4 jour', '7 jour '), ('Plus ', 'Plus')], max_length=255)),
                ('Status', models.BooleanField(default=False)),
                ('image', models.ImageField(default='logo.jpg', upload_to='ImgField')),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stmkissan.categorie')),
            ],
        ),
    ]

# Generated by Django 3.1.14 on 2023-12-15 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('fichier', models.FileField(upload_to='media/fichier/')),
                ('image', models.ImageField(upload_to='media/article_photos/')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/gallerie/')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_validite', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.article')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.photos')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.articletype'),
        ),
    ]
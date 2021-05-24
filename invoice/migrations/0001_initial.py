# Generated by Django 2.2.6 on 2021-05-24 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Un Known', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PdfUplaod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(default='', upload_to='pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Un Known', max_length=15)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=10)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ORDER', to='invoice.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PRODUCT', to='invoice.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='from_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SENDER', to='invoice.Organisation'),
        ),
        migrations.AddField(
            model_name='order',
            name='pdf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.PdfUplaod'),
        ),
        migrations.AddField(
            model_name='order',
            name='to_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RECIEVER', to='invoice.Organisation'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.User'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-07-30 16:01

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('policyid', models.AutoField(primary_key=True, serialize=False)),
                ('policy', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datein', models.DateField()),
                ('dateout', models.DateField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_receipt', jsonfield.fields.JSONField()),
                ('timestamp_stored', models.DateTimeField(auto_now_add=True)),
                ('timestamp_created', models.DateTimeField()),
                ('stayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stay')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('entityid', models.AutoField(primary_key=True, serialize=False)),
                ('entity', models.CharField(max_length=100)),
                ('policyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.policy')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('deviceid', models.AutoField(primary_key=True, serialize=False)),
                ('device', models.CharField(max_length=100)),
                ('policyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.policy')),
            ],
        ),
        migrations.CreateModel(
            name='Consent_Entity',
            fields=[
                ('consentid', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('consent', models.BooleanField()),
                ('entityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.entity')),
                ('stayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stay')),
            ],
        ),
        migrations.CreateModel(
            name='Consent_Device',
            fields=[
                ('consentid', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('consent', models.BooleanField()),
                ('deviceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.device')),
                ('stayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stay')),
            ],
        ),
        migrations.CreateModel(
            name='Stay_Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiptid', models.UUIDField()),
                ('stayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stay')),
            ],
            options={
                'unique_together': {('stayid', 'receiptid')},
            },
        ),
    ]

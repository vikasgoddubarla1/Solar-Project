# Generated by Django 4.2.1 on 2024-07-31 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('iso3', models.CharField(max_length=100)),
                ('iso2', models.CharField(max_length=100)),
                ('numeric_code', models.CharField(max_length=100)),
                ('phone_code', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('currency_symbol', models.CharField(max_length=100)),
                ('tld', models.CharField(max_length=100)),
                ('native', models.CharField(max_length=100, null=True)),
                ('region', models.CharField(max_length=100)),
                ('sub_region', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('emoji', models.CharField(max_length=100)),
                ('emojiU', models.CharField(max_length=100)),
                ('translations', models.JSONField(default=dict)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=100, null=True, unique=True)),
                ('phone', models.CharField(max_length=20, null=True, unique=True)),
                ('partner_logo', models.ImageField(blank=True, null=True, upload_to='partner_logo')),
                ('support_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('support_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('sales_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('sales_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('address_line_1', models.CharField(max_length=100, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, max_length=2000, null=True)),
                ('website', models.CharField(blank=True, max_length=555, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zoneName', models.CharField(max_length=100)),
                ('gmtOffset', models.CharField(max_length=100)),
                ('gmtOffsetName', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=100)),
                ('tzName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_fixed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('role_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.role')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerTypesRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.partner')),
                ('role_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.role')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.type')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerTypeRolesUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('partner_types_role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.partnertypesrole')),
            ],
        ),
    ]
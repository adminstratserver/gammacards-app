# Generated by Django 3.0.7 on 2020-07-04 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.EmailField(max_length=100, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(choices=[('Sales', 'SALES'), ('Business Development', 'BUSINESS DEVELOPMENT'), ('Marketing', 'MARKETING'), ('Technical Support', 'TECHNICAL SUPPORT'), ('Research & Development', 'RESEARCH & DEVELOPMENT'), ('Finance', 'FINANCE'), ('Legal', 'LEGAL')], default='Sales', max_length=50)),
                ('photo', models.ImageField(default='members/default/pic1.png', upload_to='members/photos/%Y/%m/%d/')),
                ('company', models.CharField(blank=True, max_length=100)),
                ('join_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=True)),
                ('is_activated', models.BooleanField(default=False)),
                ('brochure_country', models.CharField(choices=[('ALL COUNTRIES', 'All Countries'), ('BRUNEI', 'Brunei'), ('CAMBODIA', 'Cambodia'), ('HONG KONG', 'Hong Kong'), ('INDONESIA', 'Indonesia'), ('LAOS', 'Laos'), ('MALAYSIA', 'Malaysia'), ('MONGOLIA', 'Mongolia'), ('MYANMAR', 'Myanmar'), ('PAKISTAN', 'Pakistan'), ('PHILIPPINES', 'Philippines'), ('SINGAPORE', 'Singapore'), ('THAILAND', 'Thailand'), ('VIETNAM', 'Vietnam')], default='ALL COUNTRIES', max_length=50)),
                ('certificate_country', models.CharField(choices=[('ALL COUNTRIES', 'All Countries'), ('BRUNEI', 'Brunei'), ('CAMBODIA', 'Cambodia'), ('HONG KONG', 'Hong Kong'), ('INDONESIA', 'Indonesia'), ('LAOS', 'Laos'), ('MALAYSIA', 'Malaysia'), ('MONGOLIA', 'Mongolia'), ('MYANMAR', 'Myanmar'), ('PAKISTAN', 'Pakistan'), ('PHILIPPINES', 'Philippines'), ('SINGAPORE', 'Singapore'), ('THAILAND', 'Thailand'), ('VIETNAM', 'Vietnam')], default='ALL COUNTRIES', max_length=50)),
                ('eproof_country', models.CharField(choices=[('ALL COUNTRIES', 'All Countries'), ('BRUNEI', 'Brunei'), ('CAMBODIA', 'Cambodia'), ('HONG KONG', 'Hong Kong'), ('INDONESIA', 'Indonesia'), ('LAOS', 'Laos'), ('MALAYSIA', 'Malaysia'), ('MONGOLIA', 'Mongolia'), ('MYANMAR', 'Myanmar'), ('PAKISTAN', 'Pakistan'), ('PHILIPPINES', 'Philippines'), ('SINGAPORE', 'Singapore'), ('THAILAND', 'Thailand'), ('VIETNAM', 'Vietnam')], default='ALL COUNTRIES', max_length=50)),
                ('manual_country', models.CharField(choices=[('ALL COUNTRIES', 'All Countries'), ('BRUNEI', 'Brunei'), ('CAMBODIA', 'Cambodia'), ('HONG KONG', 'Hong Kong'), ('INDONESIA', 'Indonesia'), ('LAOS', 'Laos'), ('MALAYSIA', 'Malaysia'), ('MONGOLIA', 'Mongolia'), ('MYANMAR', 'Myanmar'), ('PAKISTAN', 'Pakistan'), ('PHILIPPINES', 'Philippines'), ('SINGAPORE', 'Singapore'), ('THAILAND', 'Thailand'), ('VIETNAM', 'Vietnam')], default='ALL COUNTRIES', max_length=50)),
                ('proposal_country', models.CharField(choices=[('ALL COUNTRIES', 'All Countries'), ('BRUNEI', 'Brunei'), ('CAMBODIA', 'Cambodia'), ('HONG KONG', 'Hong Kong'), ('INDONESIA', 'Indonesia'), ('LAOS', 'Laos'), ('MALAYSIA', 'Malaysia'), ('MONGOLIA', 'Mongolia'), ('MYANMAR', 'Myanmar'), ('PAKISTAN', 'Pakistan'), ('PHILIPPINES', 'Philippines'), ('SINGAPORE', 'Singapore'), ('THAILAND', 'Thailand'), ('VIETNAM', 'Vietnam')], default='ALL COUNTRIES', max_length=50)),
                ('powerpoint_country', models.CharField(choices=[('ALL COUNTRIES', 'All Countries'), ('BRUNEI', 'Brunei'), ('CAMBODIA', 'Cambodia'), ('HONG KONG', 'Hong Kong'), ('INDONESIA', 'Indonesia'), ('LAOS', 'Laos'), ('MALAYSIA', 'Malaysia'), ('MONGOLIA', 'Mongolia'), ('MYANMAR', 'Myanmar'), ('PAKISTAN', 'Pakistan'), ('PHILIPPINES', 'Philippines'), ('SINGAPORE', 'Singapore'), ('THAILAND', 'Thailand'), ('VIETNAM', 'Vietnam')], default='ALL COUNTRIES', max_length=50)),
                ('quotation_country', models.CharField(choices=[('ALL COUNTRIES', 'All Countries'), ('BRUNEI', 'Brunei'), ('CAMBODIA', 'Cambodia'), ('HONG KONG', 'Hong Kong'), ('INDONESIA', 'Indonesia'), ('LAOS', 'Laos'), ('MALAYSIA', 'Malaysia'), ('MONGOLIA', 'Mongolia'), ('MYANMAR', 'Myanmar'), ('PAKISTAN', 'Pakistan'), ('PHILIPPINES', 'Philippines'), ('SINGAPORE', 'Singapore'), ('THAILAND', 'Thailand'), ('VIETNAM', 'Vietnam')], default='ALL COUNTRIES', max_length=50)),
                ('items_per_page', models.IntegerField(default=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileFeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
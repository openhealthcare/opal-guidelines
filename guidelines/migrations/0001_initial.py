from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0006_auto_20151109_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guideline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField(null=True, blank=True)),
                ('source', models.CharField(max_length=200)),
                ('diagnosis', models.ManyToManyField(help_text=b'Canonical terms only', to='opal.Condition')),
            ],
        ),
        migrations.CreateModel(
            name='GuidelineConsultation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consulted', models.DateTimeField(auto_now_add=True)),
                ('guideline', models.ForeignKey(to='guidelines.Guideline')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

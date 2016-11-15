# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    dependencies = [
        ('opal', '0025_merge'),
    ]

    def forwards(self, orm):
        # Adding model 'Guideline'
        db.create_table(u'guidelines_guideline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'guidelines', ['Guideline'])

        # Adding M2M table for field diagnosis on 'Guideline'
        m2m_table_name = db.shorten_name(u'guidelines_guideline_diagnosis')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guideline', models.ForeignKey(orm[u'guidelines.guideline'], null=False)),
            ('condition', models.ForeignKey(orm[u'opal.condition'], null=False))
        ))
        db.create_unique(m2m_table_name, ['guideline_id', 'condition_id'])


    def backwards(self, orm):
        # Deleting model 'Guideline'
        db.delete_table(u'guidelines_guideline')

        # Removing M2M table for field diagnosis on 'Guideline'
        db.delete_table(db.shorten_name(u'guidelines_guideline_diagnosis'))


    models = {
        u'guidelines.guideline': {
            'Meta': {'object_name': 'Guideline'},
            'diagnosis': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['opal.Condition']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'opal.condition': {
            'Meta': {'ordering': "['name']", 'object_name': 'Condition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['guidelines']

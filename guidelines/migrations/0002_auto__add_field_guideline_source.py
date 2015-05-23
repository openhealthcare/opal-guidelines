# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Guideline.source'
        db.add_column(u'guidelines_guideline', 'source',
                      self.gf('django.db.models.fields.CharField')(default='BIA', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Guideline.source'
        db.delete_column(u'guidelines_guideline', 'source')


    models = {
        u'guidelines.guideline': {
            'Meta': {'object_name': 'Guideline'},
            'diagnosis': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['opal.Condition']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'opal.condition': {
            'Meta': {'ordering': "['name']", 'object_name': 'Condition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['guidelines']
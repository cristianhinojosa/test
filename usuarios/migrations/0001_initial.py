# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Usuario'
        db.create_table('usuarios_usuario', (
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, primary_key=True)),
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telefono_fijo', self.gf('django.db.models.fields.IntegerField')(default='')),
            ('celular', self.gf('django.db.models.fields.IntegerField')(default='')),
        ))
        db.send_create_signal('usuarios', ['Usuario'])


    def backwards(self, orm):
        
        # Deleting model 'Usuario'
        db.delete_table('usuarios_usuario')


    models = {
        'usuarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'celular': ('django.db.models.fields.IntegerField', [], {'default': "''"}),
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono_fijo': ('django.db.models.fields.IntegerField', [], {'default': "''"})
        }
    }

    complete_apps = ['usuarios']

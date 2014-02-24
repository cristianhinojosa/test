# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Producto'
        db.create_table('productos_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('valor', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuarios.Usuario'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('productos', ['Producto'])


    def backwards(self, orm):
        
        # Deleting model 'Producto'
        db.delete_table('productos_producto')


    models = {
        'productos.producto': {
            'Meta': {'object_name': 'Producto'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['usuarios.Usuario']"}),
            'valor': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
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

    complete_apps = ['productos']

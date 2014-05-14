# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Producto.imagen_3'
        db.delete_column('productos_producto', 'imagen_3')

        # Deleting field 'Producto.estado'
        db.delete_column('productos_producto', 'estado')

        # Deleting field 'Producto.imagen_2'
        db.delete_column('productos_producto', 'imagen_2')

        # Deleting field 'Producto.imagen_4'
        db.delete_column('productos_producto', 'imagen_4')

        # Deleting field 'Producto.imagen_5'
        db.delete_column('productos_producto', 'imagen_5')

        # Adding field 'Producto.estado_producto'
        db.add_column('productos_producto', 'estado_producto', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Producto.estado_publicacion'
        db.add_column('productos_producto', 'estado_publicacion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Changing field 'Producto.usuario'
        db.alter_column('productos_producto', 'usuario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'Producto.valor'
        db.alter_column('productos_producto', 'valor', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Producto.descripcion'
        db.alter_column('productos_producto', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Producto.nombre'
        db.alter_column('productos_producto', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))


    def backwards(self, orm):
        
        # Adding field 'Producto.imagen_3'
        db.add_column('productos_producto', 'imagen_3', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'Producto.estado'
        db.add_column('productos_producto', 'estado', self.gf('django.db.models.fields.CharField')(default=0, max_length=200), keep_default=False)

        # Adding field 'Producto.imagen_2'
        db.add_column('productos_producto', 'imagen_2', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'Producto.imagen_4'
        db.add_column('productos_producto', 'imagen_4', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'Producto.imagen_5'
        db.add_column('productos_producto', 'imagen_5', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True), keep_default=False)

        # Deleting field 'Producto.estado_producto'
        db.delete_column('productos_producto', 'estado_producto')

        # Deleting field 'Producto.estado_publicacion'
        db.delete_column('productos_producto', 'estado_publicacion')

        # Changing field 'Producto.usuario'
        db.alter_column('productos_producto', 'usuario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuarios.Usuario'], null=True))

        # Changing field 'Producto.valor'
        db.alter_column('productos_producto', 'valor', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Producto.descripcion'
        db.alter_column('productos_producto', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Producto.nombre'
        db.alter_column('productos_producto', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 14, 16, 53, 27, 24564)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 14, 16, 53, 27, 24364)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'productos.producto': {
            'Meta': {'object_name': 'Producto'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'estado_producto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'estado_publicacion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'valor': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['productos']

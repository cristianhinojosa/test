# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Producto.fotografia'
        db.delete_column('productos_producto', 'fotografia')

        # Deleting field 'Producto.fotografia2'
        db.delete_column('productos_producto', 'fotografia2')

        # Adding field 'Producto.fotografia_1'
        db.add_column('productos_producto', 'fotografia_1', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Producto.fotografia_2'
        db.add_column('productos_producto', 'fotografia_2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Producto.fotografia_3'
        db.add_column('productos_producto', 'fotografia_3', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Producto.fotografia_4'
        db.add_column('productos_producto', 'fotografia_4', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Producto.fotografia_5'
        db.add_column('productos_producto', 'fotografia_5', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Producto.fotografia'
        db.add_column('productos_producto', 'fotografia', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Producto.fotografia2'
        db.add_column('productos_producto', 'fotografia2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Producto.fotografia_1'
        db.delete_column('productos_producto', 'fotografia_1')

        # Deleting field 'Producto.fotografia_2'
        db.delete_column('productos_producto', 'fotografia_2')

        # Deleting field 'Producto.fotografia_3'
        db.delete_column('productos_producto', 'fotografia_3')

        # Deleting field 'Producto.fotografia_4'
        db.delete_column('productos_producto', 'fotografia_4')

        # Deleting field 'Producto.fotografia_5'
        db.delete_column('productos_producto', 'fotografia_5')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 30, 12, 33, 37, 177730)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 30, 12, 33, 37, 177645)'}),
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
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fotografia_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'fotografia_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'fotografia_3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'fotografia_4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'fotografia_5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'valor': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['productos']

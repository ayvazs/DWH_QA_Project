from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django.urls import reverse
from .models import DataBase, Schema, Table
from . import test_execution as te
import pyodbc
import json


def index(request):
	db = DataBase.objects.all()[0]
	context = {'db': db, }
	return render(request, 'tester/index.html', context)


def settings(request):
	db = DataBase.objects.all()[0]
	context = {'db': db, }
	return render(request, 'tester/settings.html', context)


def schemas_refresh(request):
	db = DataBase.objects.all()[0]
	cnxn = pyodbc.connect(db.dev_connection_string)
	cursor = cnxn.cursor()
	cursor.execute(db.script_get_schemas_list)
	rows = cursor.fetchall()
	cnxn.close()
	for row in rows:
		try:
			schema = db.schema_set.get(schema_name = row.Database)
		except (KeyError, Schema.DoesNotExist):
			db.schema_set.create(schema_name = row.Database)
	db.save()
	return HttpResponseRedirect(reverse('tester:settings'))


def set_active_schemas(request):
	db = DataBase.objects.all()[0]
	for schema in db.schema_set.all():
		try:
			checkbox_value = request.POST[schema.schema_name]
			schema.is_active = True
			tables_refresh(schema.id)
		except:
			schema.is_active = False
		schema.save()
	return HttpResponseRedirect(reverse('tester:settings'))


def tables_refresh(schema_id):
	schema = get_object_or_404(Schema, pk=schema_id)
	cnxn = pyodbc.connect(schema.data_base.dev_connection_string)
	cursor = cnxn.cursor()
	cursor.execute(schema.data_base.script_set_active_schema + ' ' + schema.schema_name)
	cursor.execute(schema.data_base.script_get_tables_list)
	rows = cursor.fetchall()
	cnxn.close()
	for row in rows:
		try:
			table = schema.table_set.get(table_name = row[0])
		except:
			schema.table_set.create(table_name = row[0])
	schema.save()


def table(request, table_id):
	table_object = get_object_or_404(Table, pk = table_id)
	if request.method == 'GET':
		context = {'table': table_object,}
		return render(request, 'tester/table.html', context)
	elif request.method == 'POST':
		if request.POST['test_script_dev_to_prod_compare'] == '':
			table_object.test_script_dev_to_prod_compare = None
		else:
			table_object.test_script_dev_to_prod_compare = request.POST['test_script_dev_to_prod_compare']
		if request.POST['test_script_uniqueness'] == '':
			table_object.test_script_uniqueness = None
		else:
			table_object.test_script_uniqueness = request.POST['test_script_uniqueness']
		if request.POST['test_script_completeness_source'] == '':
			table_object.test_script_completeness_source = None
		else:
			table_object.test_script_completeness_source = request.POST['test_script_completeness_source']
		if request.POST['test_script_completeness_target'] == '':
			table_object.test_script_completeness_target = None
		else:
			table_object.test_script_completeness_target = request.POST['test_script_completeness_target']
		table_object.save()
		return HttpResponseRedirect(reverse('tester:index'))


def do_test_exists_on_prod_view(request, table_id):
	if request.is_ajax():
		data = te.do_test_exists_on_prod(table_id)
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404


def do_test_dtpc_view(request, table_id):
	if request.is_ajax():
		data = te.do_test_dtpc(table_id)
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404


def do_test_uniq_dev_view(request, table_id):
	if request.is_ajax():
		data = te.do_test_uniq_dev(table_id)
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404


def do_test_uniq_prod_view(request, table_id):
	if request.is_ajax():
		data = te.do_test_uniq_prod(table_id)
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404


def do_test_complete_dev_view(request, table_id):
	if request.is_ajax():
		data = te.do_test_complete_dev(table_id)
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404


def do_test_complete_prod_view(request, table_id):
	if request.is_ajax():
		data = te.do_test_complete_prod(table_id)
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

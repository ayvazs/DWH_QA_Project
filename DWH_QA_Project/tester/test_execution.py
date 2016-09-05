from django.shortcuts import render, get_object_or_404
from .models import DataBase, Schema, Table
import pyodbc


def script_execute(conn_str, script):
	try:
		cnxn = pyodbc.connect(conn_str)
		cursor = cnxn.cursor()
		cursor.execute(script)
	except pyodbc.Error as e:
		return e

	row = cursor.fetchone()
	cursor.close()
	cnxn.close()
	return int(row[0])


def do_test_exists_on_prod(table_id):
	table_object = get_object_or_404(Table, pk = table_id)
	if table_object.schema.data_base.prod_connection_string is not None and table_object.schema.data_base.prod_connection_string != '':
		cnxn = pyodbc.connect(table_object.schema.data_base.prod_connection_string)
		cursor = cnxn.cursor()
		cursor.execute("USE " + table_object.schema.schema_name)
		cursor.execute("SHOW TABLES")
		rows = cursor.fetchall()
		cnxn.close()
		for row in rows:
			if table_object.table_name == row[0]:
				table_object.exist_in_prod = True
				table_object.save()
	test_status, test_message = table_object.get_exist_on_prod_status()
	return {'table_id': table_id, 'test_status': test_status, 'test_message': test_message}


def do_test_dtpc(table_id):
	table_object = get_object_or_404(Table, pk = table_id)
	if table_object.test_script_dev_to_prod_compare is not None and table_object.test_script_dev_to_prod_compare != '':
		dev_value = script_execute(table_object.schema.data_base.dev_connection_string, table_object.test_script_dev_to_prod_compare)
		table_object.test_value_dev_to_prod_compare_dev = dev_value
		prod_value = script_execute(table_object.schema.data_base.dev_connection_string, table_object.test_script_dev_to_prod_compare)
		table_object.test_value_dev_to_prod_compare_prod = prod_value
		table_object.save()
	test_status, test_message = table_object.get_dev_to_prod_compare_status()
	return {'table_id': table_id, 'test_status': test_status, 'test_message': test_message}


def do_test_uniq_dev(table_id):
	table_object = get_object_or_404(Table, pk = table_id)
	if table_object.test_script_uniqueness is not None and table_object.test_script_uniqueness != '':
		dev_value = script_execute(table_object.schema.data_base.dev_connection_string, table_object.test_script_uniqueness)
		table_object.test_value_uniqueness_dev = dev_value
		table_object.save()
	test_status, test_message = table_object.get_uniqueness_status_dev()
	return {'table_id': table_id, 'test_status': test_status, 'test_message': test_message}


def do_test_uniq_prod(table_id):
	table_object = get_object_or_404(Table, pk = table_id)
	if table_object.test_script_uniqueness is not None and table_object.test_script_uniqueness != '':
		prod_value = script_execute(table_object.schema.data_base.prod_connection_string, table_object.test_script_uniqueness)
		table_object.test_value_uniqueness_prod = prod_value
		table_object.save()
	test_status, test_message = table_object.get_uniqueness_status_prod()
	return {'table_id': table_id, 'test_status': test_status, 'test_message': test_message}


def do_test_complete_dev(table_id):
	table_object = get_object_or_404(Table, pk = table_id)
	if table_object.test_script_completeness_source is not None and table_object.test_script_completeness_source != '' and table_object.test_script_completeness_target is not None and table_object.test_script_completeness_target != '':
		source_value = script_execute(table_object.schema.data_base.dev_connection_string, table_object.test_script_completeness_source)
		table_object.test_value_completeness_source_dev = source_value
		target_value = script_execute(table_object.schema.data_base.dev_connection_string, table_object.test_script_completeness_target)
		table_object.test_value_completeness_target_dev = target_value
		table_object.save()
	test_status, test_message = table_object.get_complete_status_dev()
	return {'table_id': table_id, 'test_status': test_status, 'test_message': test_message}


def do_test_complete_prod(table_id):
	table_object = get_object_or_404(Table, pk = table_id)
	if table_object.test_script_completeness_source is not None and table_object.test_script_completeness_source != '' and table_object.test_script_completeness_target is not None and table_object.test_script_completeness_target != '':
		source_value = script_execute(table_object.schema.data_base.prod_connection_string, table_object.test_script_completeness_source)
		table_object.test_value_completeness_source_prod = source_value
		target_value = script_execute(table_object.schema.data_base.prod_connection_string, table_object.test_script_completeness_target)
		table_object.test_value_completeness_target_prod = target_value
		table_object.save()
	test_status, test_message = table_object.get_complete_status_prod()
	return {'table_id': table_id, 'test_status': test_status, 'test_message': test_message}

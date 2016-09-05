from django.db import models
from django.urls import reverse

# Create your models here.
# todo Добавить модель типа подключения с типовыми запросами на список схем и таблиц


class DataBase(models.Model):
	database_name = models.CharField(max_length = 50)
	dev_connection_string = models.CharField(max_length = 200, null = True)
	prod_connection_string = models.CharField(max_length = 200, null = True)
	script_get_schemas_list = models.CharField(max_length = 2000, null = True)
	script_set_active_schema = models.CharField(max_length = 2000, null = True)
	script_get_tables_list = models.CharField(max_length = 2000, null = True)

	def __str__(self):
		return self.database_name


class Schema(models.Model):
	data_base = models.ForeignKey(DataBase, on_delete = models.CASCADE)
	schema_name = models.CharField(max_length = 50)
	is_active = models.BooleanField(default = False)
	exist_in_prod = models.BooleanField(default = False)

	def __str__(self):
		return self.schema_name


class Table(models.Model):
	schema = models.ForeignKey(Schema, on_delete = models.CASCADE)
	table_name = models.CharField(max_length = 200)
	exist_in_prod = models.BooleanField(default = False)
	test_script_dev_to_prod_compare = models.TextField(null = True)
	test_value_dev_to_prod_compare_dev = models.BigIntegerField(null = True)
	test_value_dev_to_prod_compare_prod = models.BigIntegerField(null = True)
	test_script_uniqueness = models.TextField(null = True)
	test_value_uniqueness_dev = models.BigIntegerField(null = True)
	test_value_uniqueness_prod = models.BigIntegerField(null = True)
	test_script_completeness_source = models.TextField(null = True)
	test_value_completeness_source_dev = models.BigIntegerField(null = True)
	test_value_completeness_source_prod = models.BigIntegerField(null = True)
	test_script_completeness_target = models.TextField(null = True)
	test_value_completeness_target_dev = models.BigIntegerField(null = True)
	test_value_completeness_target_prod = models.BigIntegerField(null = True)

	def __str__(self):
		return self.table_name

	def get_absolute_url(self):
		return reverse('table_detail', kwargs = {'pk': self.pk})

	def get_exist_on_prod_status(self):
		if self.exist_in_prod:
			return 'success', 'Да'
		else:
			return 'warn', 'Нет'

	def get_dev_to_prod_compare_status(self):
		if self.test_script_dev_to_prod_compare is None or self.test_script_dev_to_prod_compare == '':
			return 'warn', 'Нет скрипта'
		elif self.test_value_dev_to_prod_compare_dev is None:
			return 'warn', 'Запустите'
		elif self.test_value_dev_to_prod_compare_dev != self.test_value_dev_to_prod_compare_prod:
			return 'fail', 'Ошибка'
		elif self.test_value_dev_to_prod_compare_dev == self.test_value_dev_to_prod_compare_prod:
			return 'success', 'Успешно'
		else:
			return 'fail', 'Неизвестная ошибка'

	def get_uniqueness_status_dev(self):
		if self.test_script_uniqueness is None or self.test_script_uniqueness == '':
			return 'warn', 'Нет скрипта'
		elif self.test_value_uniqueness_dev is None:
			return 'warn', 'Запустите'
		elif self.test_value_uniqueness_dev > 0:
			return 'fail', 'Ошибка'
		elif self.test_value_uniqueness_dev == 0:
			return 'success', 'Успешно'
		else:
			return 'fail', 'Неизвестная ошибка'

	def get_uniqueness_status_prod(self):
		if self.test_script_uniqueness is None or self.test_script_uniqueness == '':
			return 'warn', 'Нет скрипта'
		elif self.test_value_uniqueness_prod is None:
			return 'warn', 'Запустите'
		elif self.test_value_uniqueness_prod > 0:
			return 'fail', 'Ошибка'
		elif self.test_value_uniqueness_prod == 0:
			return 'success', 'Успешно'
		else:
			return 'fail', 'Неизвестная ошибка'

	def get_complete_status_dev(self):
		if self.test_script_completeness_source is None or self.test_script_completeness_source == '':
			return 'warn', 'Нет исходносго скрипта'
		elif self.test_script_completeness_target is None or self.test_script_completeness_target == '':
			return 'warn', 'Нет целевого скрипта'
		elif self.test_value_completeness_source_dev is None or self.test_value_completeness_target_dev is None:
			return 'warn', 'Запустите'
		elif self.test_value_completeness_source_dev != self.test_value_completeness_target_dev:
			return 'fail', 'Ошибка'
		elif self.test_value_completeness_source_dev == self.test_value_completeness_target_dev:
			return 'success', 'Успешно'
		else:
			return 'fail', 'Неизвестная ошибка'

	def get_complete_status_prod(self):
		if self.test_script_completeness_source is None or self.test_script_completeness_source == '':
			return 'warn', 'Нет исходного скрипта'
		elif self.test_script_completeness_target is None or self.test_script_completeness_target == '':
			return 'warn', 'Нет целевого скрипта'
		elif self.test_value_completeness_source_prod is None or self.test_value_completeness_target_prod is None:
			return 'warn', 'Запустите'
		elif self.test_value_completeness_source_prod != self.test_value_completeness_target_prod:
			return 'fail', 'Ошибка'
		elif self.test_value_completeness_source_prod == self.test_value_completeness_target_prod:
			return 'success', 'Успешно'
		else:
			return 'fail', 'Неизвестная ошибка'

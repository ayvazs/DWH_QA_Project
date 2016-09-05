from django.conf.urls import url

from . import views

app_name = 'tester'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^settings$', views.settings, name = 'settings'),
	url(r'^set_active_schemas$', views.set_active_schemas, name = 'set_active_schemas'),
	url(r'^schemas_refresh$', views.schemas_refresh, name = 'schemas_refresh'),
	url(r'^table/(?P<table_id>[0-9]+)/$', views.table, name = 'table'),
	url(r'^table/(?P<table_id>[0-9]+)/do_test_exists_on_prod/$', views.do_test_exists_on_prod_view, name = 'do_test_exists_on_prod'),
	url(r'^table/(?P<table_id>[0-9]+)/do_test_dtpc/$', views.do_test_dtpc_view, name = 'do_test_dtpc'),
	url(r'^table/(?P<table_id>[0-9]+)/do_test_uniq_dev/$', views.do_test_uniq_dev_view, name = 'do_test_uniq_dev'),
	url(r'^table/(?P<table_id>[0-9]+)/do_test_uniq_prod/$', views.do_test_uniq_prod_view, name = 'do_test_uniq_prod'),
	url(r'^table/(?P<table_id>[0-9]+)/do_test_complete_dev/$', views.do_test_complete_dev_view, name = 'do_test_complete_dev'),
	url(r'^table/(?P<table_id>[0-9]+)/do_test_complete_prod/$', views.do_test_complete_prod_view, name = 'do_test_complete_prod'),
]

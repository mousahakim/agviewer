"""morph2o URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from visualizer import views, test_view, get_records
from visualizer.views import ANAuthenticationForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^admin/', include(admin.site.urls)),
    url(r'^visualizer/', views.index, name='index1'),
    url(r'^accounts/login/$', auth_views.login, {'authentication_form': ANAuthenticationForm, 'extra_context':{'next': '/'}}),
   url(r'^log_out/',auth_views.logout, {'next_page': 'index'}, name="log_out" ),
   url(r'^test/', get_records.get_widget, name="get_widget"),
   url(r'^gis/', views.gis_view, name="gis_view"),
   url(r'^load_widgets/', views.get_widgets, name="get_widgets"),
   url(r'^load_settings/', views.get_settings, name="get_settings"),
   url(r'^settings/', views.settings_index, name="settings"),
   url(r'^add_station/', views.add_station, name="add_station"),
   url(r'^list_files', views.load_files, name='load_files'),
   url(r'^file_upload', views.file_upload, name='file_upload'),
   url(r'^delete_files', views.delete_files, name='delete_files'),
   url(r'^download_file', views.download_file, name='download_file'), 
   url(r'^get_url', views.get_url, name='get_url'),
   url(r'^remove_widget', views.remove_widget, name='remove_widget'),
   url(r'^change_alias', views.change_alias, name='change_alias'),
   url(r'^widget_lst', views.widget_lst, name='widget_lst'),
   url(r'^widget', views.widget, name='widget'),
   url(r'^remove_station', views.remove_station, name='remove_station'),
   url(r'^change_setting', views.change_setting, name='change_setting'),
   url(r'^alert_action', views.alert_action, name='alert_action'), 
   url(r'^changedaterange', views.changedaterange, name='changedaterange'), 
   url(r'^adddashboard', views.adddashboard, name='adddashboard'),
   url(r'^removedashboard', views.removedashboard, name='removedashboard'),
   url(r'^editdashboard', views.editdashboard, name='editdashboard'), 
   url(r'^snooze_state_change', views.snooze_state_change, name='snooze_state_change'),
   url(r'^add_stat_widget', views.add_stat_widget, name='add_stat_widget'), 
   url(r'^delete_stat_widget', views.delete_stat_widget, name='delete_stat_widget'),
   url(r'^fetch_stat_widget', views.fetch_stat_widget, name='fetch_stat_widget'),
   url(r'^change_stat_widget', views.change_stat_widget, name='change_stat_widget'),
   url(r'^add_stat_data', views.add_stat_data, name='add_stat_data'),
   url(r'^change_stat_data', views.change_stat_data, name='change_stat_data'),
   url(r'^fetch_stat_data', views.fetch_stat_data, name='fetch_stat_data'),
   url(r'^delete_stat_data', views.delete_stat_data, name='delete_stat_data')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

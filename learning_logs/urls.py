from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # main page
    path('', views.index, name='index'),
    # page with list of topics
    path('topics/', views.topics, name='topics'),
    # topic page with id
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # new topic page
    path('new_topic/', views.new_topic, name='new_topic'),
    # new entry page
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]
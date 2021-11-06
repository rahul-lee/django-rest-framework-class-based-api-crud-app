from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crudapp.views import NoteList, NoteCreate, NoteDetail, NoteUpdate, NoteDelete

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('notelist/', NoteList.as_view()),
    path('notedetail/<int:pk>/', NoteDetail.as_view()),
    path('notecreate/', NoteCreate.as_view()),
    path('noteupdate/<int:pk>/', NoteUpdate.as_view()),
    path('notedelete/<int:pk>/', NoteDelete.as_view()),
]

from django.urls import path
from .views import landing, contents

urlpatterns = [
    path('', landing, name='landing'),
    path('contents', contents, name='contents')
]
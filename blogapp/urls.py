from django.urls import path
from .import views
from blogproject.settings import DEBUG,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('search',views.index,name='index'),
    path('contact',views.contact,name='contact')

]

if DEBUG:
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT,)
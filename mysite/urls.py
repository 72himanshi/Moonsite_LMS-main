
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .import views
urlpatterns = [
path('admin/', admin.site.urls),
path('base/',views.base,name='base'),
path('',views.home,name='home'),
path('aboutus',views.aboutus,name='aboutus'),
path('contact',views.contact,name='contact'),
path('accounts/login',views.loginpage,name='login'),
path("logout",views.logoutpage,name='logout'),
path('accounts/register',views.register,name='register'),
path('courses',views.course,name='course'),
path('search/courses',views.search_courses,name='search_courses'),
path('accounts/profile',views.profile,name='profile'),
path('accounts/profile/update',views.profile_update,name='profile_update'),
path('products/filter_courses',views.filter_courses,name='filter_courses'),
path('course/<slug:slug>',views.course_detalis,name='course_details'),
path('error/404',views.page_not_found,name='error'),
path('assignment/<slug:slug>',views.assignment,name='assignment'),
path('discuss/<slug:slug>',views.discuss,name="discuss"),
path ('froala_editor/', include ( 'froala_editor.urls' ) ),
path('game/',views.game,name='game'),
path('game2/',views.game2,name='game2'),
path('treasure_hunt/',views.treasure_hunt,name='treasure_hunt'),
path('enrollment/<slug:slug>',views.enrollment,name="enrollment"),
    url ( r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT} ),
    url ( r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT} )

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

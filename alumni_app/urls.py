from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from alumni_app import views

app_name='link'

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^signin/$',views.signin, name='signin'),
    url(r'^about_page/$',views.about_page, name='about_page'),
    url(r'^signin/edit_profile/$',views.edit_profile, name='edit_profile'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^signin/forum_view/forum/$',views.forum, name='contact'),
    # url(r'^aiding/signin/forum_view/forum/$',views.comments, name='contact'),
    url(r'^signin/forum_view/$',views.forumView, name='contact'),
    url(r'^aiding/signin/forum_view/comment$',views.comment_page, name='comment_page'),
    url(r'^council/$',views.council_page, name='contact'),
    url(r'^event/$',views.event_page, name='contact'),
    # url(r'^comment_form/$',views.comments, name='contact'),
    url(r'^aiding/$',views.aiding, name='aiding'),
    url(r'^$',views.logout_view, name='logout'),





#   url(r'^middetails/$',views.middetails, name='middetails'),


    #url(r'^signin/$',views.signinforms, name='signin'),



]

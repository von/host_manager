from django.conf.urls.defaults import *
from models import Host

info_dict = {
    "queryset": Host.objects.all(),
}

urlpatterns = patterns('',
                       (r'^$',
                        'django.views.generic.list_detail.object_list',
                        dict(info_dict,
                             template_name="host_list.tmpl",
                             mimetype="text/plain",
                             )
                        ),

                       )

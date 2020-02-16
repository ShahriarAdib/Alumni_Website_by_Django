from django.contrib import admin
from alumni_app.models import user_signup,notice,post,comment,event,track,upcoming_event

# Register your models here.
admin.site.register(user_signup)
admin.site.register(notice)
admin.site.register(post)
admin.site.register(comment)
admin.site.register(event)
admin.site.register(track)
admin.site.register(upcoming_event)

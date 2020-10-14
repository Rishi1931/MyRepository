from django.contrib import admin
from .models import destination
from .models import destination1
from .models import newspost
from .models import newspage
from .models import Feedback
from embed_video.admin import AdminVideoMixin
from .models import Item
from .models import Subscribe

# Register your models here.

admin.site.register(destination)
admin.site.register(destination1)
admin.site.register(newspost)
admin.site.register(newspage)
admin.site.register(Feedback)
admin.site.register(Subscribe)



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)

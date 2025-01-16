from django.contrib import admin
from . models import shoes
from . models import watches,dresses,bags,menshirts


# Register your models here.
admin.site.register(shoes)
admin.site.register(watches)
admin.site.register(bags)
admin.site.register(dresses)
admin.site.register(menshirts)


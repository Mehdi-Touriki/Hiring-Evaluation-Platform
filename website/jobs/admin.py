from django.contrib import admin
from .models import Post, ApplyJob,Profil,SavedPostt,JobCategory

admin.site.register(Post)
admin.site.register(ApplyJob)
admin.site.register(Profil)
admin.site.register(SavedPostt) # hadi tzadt

admin.site.register(JobCategory)

from hosts.models import Host,Alias,IPAddr
from django.contrib import admin

class IPAddrInline(admin.StackedInline):
    model = IPAddr
    extra = 1

class AliasInline(admin.StackedInline):
    model = Alias
    extra = 1

class HostAdmin(admin.ModelAdmin):
    inlines = [AliasInline, IPAddrInline]
    search_firlds = ['hostname']

admin.site.register(Host, HostAdmin)

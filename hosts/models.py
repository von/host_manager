from django.db import models

maxHostLength=512

class Host(models.Model):
    hostname = models.CharField(max_length=maxHostLength)
    comment = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.hostname

class IPAddr(models.Model):
    host = models.ForeignKey(Host)
    ipaddr = models.IPAddressField()

    def __unicode__(self):
        return self.ipaddr

class Alias(models.Model):
    alias = models.CharField(max_length=maxHostLength)
    host = models.ForeignKey(Host)

    def __unicode__(self):
        return self.alias

    

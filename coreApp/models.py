from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.db.models.signals import post_save  # type: ignore
from django.dispatch import receiver  # type: ignore


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpr = models.CharField(max_length=255, blank=True)  # Add your cpr field here

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class depotcases2024(models.Model):
    id = models.AutoField(primary_key=True)
    REFRENCENUMBER = models.CharField(max_length=20)
    DEPOT = models.CharField(max_length=100)
    AREA_ENGINEER_NAME = models.CharField(max_length=100)
    BLOCKNUMBER = models.CharField(max_length=20)
    SUBSTATIONNUMBER = models.CharField(max_length=20)
    TX = models.CharField(max_length=10)
    FEEDERNUMBER = models.CharField(max_length=10)
    LVBNUMBER = models.CharField(max_length=10)
    TYPE = models.CharField(max_length=50)
    WAYLEAVENUMBER = models.CharField(max_length=100)
    USPDATE = models.DateField(null=True, blank=True)
    PASSEDDATE = models.DateField(null=True, blank=True)
    REMARKES = models.TextField(blank=True)
    PlanStatus = models.CharField(max_length=50)
    ConStatus = models.CharField(max_length=50)
    GISDATE = models.DateField(null=True, blank=True)
    RCCDATE = models.DateField(null=True, blank=True)
    MSPDATE = models.DateField(null=True, blank=True)
    labourcost = models.FloatField()
    ministrycost = models.FloatField()
    cable_length = models.FloatField()
    Area = models.CharField(max_length=100, blank=True)
    gov = models.CharField(max_length=100)
    sentDate = models.DateField(null=True, blank=True)
    noOfServ = models.FloatField()
    noOfFaults = models.FloatField()
    areaEngEmail = models.EmailField(blank=True)
    EngPhoneNumber = models.CharField(max_length=15, blank=True)
    AreaOfAe = models.CharField(max_length=100)
    totalcost = models.FloatField()

    class Meta:
        db_table = "depotcases2024"  # Use your schema name

    def __str__(self):
        return self.areaOfAe

    def __str__(self):
        return f"{self.REFRENCENUMBER} - {self.AREA_ENGINEER_NAME}"


class depotcases2025(models.Model):
    id = models.AutoField(primary_key=True)
    REFRENCENUMBER = models.CharField(max_length=20)
    DEPOT = models.CharField(max_length=100)
    AREA_ENGINEER_NAME = models.CharField(max_length=100)
    BLOCKNUMBER = models.CharField(max_length=20)
    SUBSTATIONNUMBER = models.CharField(max_length=20)
    TX = models.CharField(max_length=10)
    FEEDERNUMBER = models.CharField(max_length=10)
    LVBNUMBER = models.CharField(max_length=10)
    TYPE = models.CharField(max_length=50)  # e.g., "Replacement Only"
    WAYLEAVENUMBER = models.CharField(max_length=100)
    USPDATE = models.DateField(null=True, blank=True)  # Assuming this can be empty
    PASSEDDATE = models.DateField(null=True, blank=True)
    REMARKES = models.TextField(blank=True)
    PlanStatus = models.CharField(max_length=50)
    ConStatus = models.CharField(max_length=50)
    GISDATE = models.DateField(null=True, blank=True)  # Assuming this can be empty
    RCCDATE = models.DateField(null=True, blank=True)  # Assuming this can be empty
    MSPDATE = models.DateField(null=True, blank=True)  # Assuming this can be empty
    labourcost = models.FloatField()
    ministrycost = models.FloatField()
    cable_length = models.FloatField()
    Area = models.CharField(max_length=100, blank=True)
    gov = models.CharField(max_length=100)  # Governorate
    sentDate = models.DateField(null=True, blank=True)  # Assuming this can be empty
    noOfServ = models.FloatField()
    noOfFaults = models.FloatField()
    areaEngEmail = models.EmailField(blank=True)
    EngPhoneNumber = models.CharField(max_length=15, blank=True)
    AreaOfAe = models.CharField(max_length=100)
    totalcost = models.FloatField()

    class Meta:
        db_table = "depotcases2025"

    def __str__(self):
        return f"{self.REFRENCENUMBER} - {self.AREA_ENGINEER_NAME}"


from django.db import models
from django.utils import timezone


class Permit(models.Model):
    id = models.AutoField(primary_key=True)
    Number = models.CharField(max_length=50, unique=True, verbose_name="Permit Number")
    parcel_number = models.CharField(max_length=50, verbose_name="Parcel Number")
    block = models.CharField(max_length=50, verbose_name="Block")
    kw = models.FloatField()
    kva = models.FloatField()
    planeng = models.CharField(max_length=100, verbose_name="Plan Engineer")
    plan_status = models.CharField(max_length=100, verbose_name="Plan Status")
    passed_date = models.DateField(verbose_name="Passed Date")
    to_wl_date = models.DateField(verbose_name="To WL Date")
    to_gis_date = models.DateField(verbose_name="To GIS Date")
    wl_number = models.CharField(max_length=100, verbose_name="WL_NUMBER")
    ref_no = models.CharField(max_length=100, verbose_name="REF_NO")
    comment = models.CharField(max_length=100, verbose_name="comment")

    class Meta:
        db_table = "Permit"

    def __str__(self):
        return self.number

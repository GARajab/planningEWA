from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.db.models.signals import post_save  # type: ignore
from django.dispatch import receiver  # type: ignore


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpr = models.CharField(max_length=255, blank=True, null=True)  # Updated

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
    REFRENCENUMBER = models.CharField(max_length=20, blank=True, null=True)  # Updated
    AREA_ENGINEER_NAME = models.CharField(
        max_length=100, blank=True, null=True
    )  # Updated
    BLOCKNUMBER = models.CharField(max_length=20, blank=True, null=True)  # Updated
    SUBSTATIONNUMBER = models.CharField(max_length=20, blank=True, null=True)  # Updated
    TX = models.CharField(max_length=10, blank=True, null=True)  # Updated
    FEEDERNUMBER = models.CharField(max_length=10, blank=True, null=True)  # Updated
    LVBNUMBER = models.CharField(max_length=10, blank=True, null=True)  # Updated
    TYPE = models.CharField(max_length=50, blank=True, null=True)  # Updated
    WAYLEAVENUMBER = models.CharField(max_length=100, blank=True, null=True)  # Updated
    USPDATE = models.DateField(null=True, blank=True)  # Updated
    PASSEDDATE = models.DateField(null=True, blank=True)  # Updated
    REMARKES = models.TextField(blank=True, null=True)  # Updated
    PlanStatus = models.CharField(max_length=50, blank=True, null=True)  # Updated
    ConStatus = models.CharField(max_length=50, blank=True, null=True)  # Updated
    GISDATE = models.DateField(null=True, blank=True)  # Updated
    RCCDATE = models.DateField(null=True, blank=True)  # Updated
    MSPDATE = models.DateField(null=True, blank=True)  # Updated
    labourcost = models.FloatField(blank=True, null=True, default=0.0)  # Updated
    ministrycost = models.FloatField(blank=True, null=True)  # Updated
    cable_length = models.FloatField(blank=True, null=True)  # Updated
    noOfServ = models.FloatField(blank=True, null=True)  # Updated
    noOfFaults = models.FloatField(blank=True, null=True)  # Updated
    areaEngEmail = models.EmailField(blank=True, null=True)  # Updated
    totalcost = models.FloatField(blank=True, null=True)  # Updated

    class Meta:
        db_table = "depotcases2024"

    def __str__(self):
        return f"{self.REFRENCENUMBER} - {self.AREA_ENGINEER_NAME}"

    def save(self, *args, **kwargs):
        # Convert empty strings to None for date fields
        if self.USPDATE == "":
            self.USPDATE = None
        if self.PASSEDDATE == "":
            self.PASSEDDATE = None
        if self.GISDATE == "":
            self.GISDATE = None
        if self.RCCDATE == "":
            self.RCCDATE = None
        if self.MSPDATE == "":
            self.MSPDATE = None
        if self.labourcost == "":
            self.labourcost = None
        if self.ministrycost == "":
            self.ministrycost = None
        if self.cable_length == "":
            self.cable_length = None
        if self.noOfServ == "":
            self.noOfServ = None
        if self.noOfFaults == "":
            self.noOfFaults = None
        if self.totalcost == "":
            self.totalcost = None
        super().save(*args, **kwargs)


class depotcases2025(models.Model):
    id = models.AutoField(primary_key=True)
    REFRENCENUMBER = models.CharField(max_length=20, blank=True, null=True)  # Updated
    AREA_ENGINEER_NAME = models.CharField(
        max_length=100, blank=True, null=True
    )  # Updated
    BLOCKNUMBER = models.CharField(max_length=20, blank=True, null=True)  # Updated
    SUBSTATIONNUMBER = models.CharField(max_length=20, blank=True, null=True)  # Updated
    TX = models.CharField(max_length=10, blank=True, null=True)  # Updated
    FEEDERNUMBER = models.CharField(max_length=10, blank=True, null=True)  # Updated
    LVBNUMBER = models.CharField(max_length=10, blank=True, null=True)  # Updated
    TYPE = models.CharField(max_length=50, blank=True, null=True)  # Updated
    WAYLEAVENUMBER = models.CharField(max_length=100, blank=True, null=True)  # Updated
    USPDATE = models.DateField(null=True, blank=True)  # Updated
    PASSEDDATE = models.DateField(null=True, blank=True)  # Updated
    REMARKES = models.TextField(blank=True, null=True)  # Updated
    PlanStatus = models.CharField(max_length=50, blank=True, null=True)  # Updated
    ConStatus = models.CharField(max_length=50, blank=True, null=True)  # Updated
    GISDATE = models.DateField(null=True, blank=True)  # Updated
    RCCDATE = models.DateField(null=True, blank=True)  # Updated
    MSPDATE = models.DateField(null=True, blank=True)  # Updated
    labourcost = models.FloatField(blank=True, null=True, default=0.0)  # Updated
    ministrycost = models.FloatField(blank=True, null=True)  # Updated
    cable_length = models.FloatField(blank=True, null=True)  # Updated
    noOfServ = models.FloatField(blank=True, null=True)  # Updated
    noOfFaults = models.FloatField(blank=True, null=True)  # Updated
    areaEngEmail = models.EmailField(blank=True, null=True)  # Updated
    totalcost = models.FloatField(blank=True, null=True)  # Updated

    class Meta:
        db_table = "depotcases2025"

    def __str__(self):
        return f"{self.REFRENCENUMBER} - {self.AREA_ENGINEER_NAME}"

    def save(self, *args, **kwargs):
        # Convert empty strings to None for date fields
        if self.USPDATE == "":
            self.USPDATE = None
        if self.PASSEDDATE == "":
            self.PASSEDDATE = None
        if self.GISDATE == "":
            self.GISDATE = None
        if self.RCCDATE == "":
            self.RCCDATE = None
        if self.MSPDATE == "":
            self.MSPDATE = None
        if self.labourcost == "":
            self.labourcost = None
        if self.ministrycost == "":
            self.ministrycost = None
        if self.cable_length == "":
            self.cable_length = None
        if self.noOfServ == "":
            self.noOfServ = None
        if self.noOfFaults == "":
            self.noOfFaults = None
        if self.totalcost == "":
            self.totalcost = None
        super().save(*args, **kwargs)


class Permit(models.Model):
    id = models.AutoField(primary_key=True)
    Number = models.CharField(
        max_length=50, unique=True, verbose_name="Permit Number", blank=True, null=True
    )  # Updated
    parcel_number = models.CharField(
        max_length=50, verbose_name="Parcel Number", blank=True, null=True
    )  # Updated
    block = models.CharField(
        max_length=50, verbose_name="Block", blank=True, null=True
    )  # Updated
    kw = models.FloatField(blank=True, null=True)  # Updated
    kva = models.FloatField(blank=True, null=True)  # Updated
    planeng = models.CharField(
        max_length=100, verbose_name="Plan Engineer", blank=True, null=True
    )  # Updated
    plan_status = models.CharField(
        max_length=100, verbose_name="Plan Status", blank=True, null=True
    )  # Updated
    passed_date = models.DateField(
        null=True, blank=True, verbose_name="Passed Date"
    )  # Updated
    to_wl_date = models.DateField(
        null=True, blank=True, verbose_name="To WL Date"
    )  # Updated
    to_gis_date = models.DateField(
        null=True, blank=True, verbose_name="To GIS Date"
    )  # Updated
    wl_number = models.CharField(
        max_length=100, verbose_name="WL_NUMBER", blank=True, null=True
    )  # Updated
    ref_no = models.CharField(
        max_length=100, verbose_name="REF_NO", blank=True, null=True
    )  # Updated
    comment = models.CharField(
        max_length=100, verbose_name="comment", blank=True, null=True
    )  # Updated

    class Meta:
        db_table = "Permit"

    def __str__(self):
        return self.Number

    def save(self, *args, **kwargs):
        # Convert empty strings to None for date fields
        if self.passed_date == "":
            self.passed_date = None
        if self.to_wl_date == "":
            self.to_wl_date = None
        if self.to_gis_date == "":
            self.to_gis_date = None
        super().save(*args, **kwargs)


class LoadReading2024(models.Model):
    id = models.AutoField(primary_key=True)
    ssno = models.CharField(max_length=20, verbose_name="SSNO")

    txno = models.CharField(max_length=20, blank=True, null=True, verbose_name="TXNO")

    block = models.CharField(max_length=20, blank=True, null=True, verbose_name="BLOCK")
    lvb_fdr = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="LVB FDR"
    )

    kva = models.CharField(max_length=20, blank=True, null=True, verbose_name="kVA")
    worktype = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="WorkType"
    )
    plan_status = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Plan Status"
    )
    wl_no = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="WL NO"
    )

    sch_ref = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Sch Ref"
    )
    title = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Title"
    )
    job_no = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Job no"
    )
    rcvd_date = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Rcvd Date"
    )
    planeng = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="PlanEng"
    )
    plan_rem = models.TextField(blank=True, null=True, verbose_name="Plan Rem")
    cons_rem = models.TextField(blank=True, null=True, verbose_name="Cons Rem")
    labour = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Labour"
    )
    material = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Material"
    )

    completed_by_construction = models.TextField(
        blank=True, null=True, verbose_name="Completed By Construction"
    )

    wayleave = models.TextField(blank=True, null=True, verbose_name="wayleave")
    passed_date = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="passed date"
    )

    gisdate = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="GISDATE"
    )
    uspdate = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="USPDATE"
    )
    rccdate = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="RCCDATE"
    )
    mspdate = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="MSPDATE"
    )
    labourcost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="labourcost",
    )
    ministrycost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="ministrycost",
    )
    cable_length = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="cable length",
    )
    totalcost = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="totalcost"
    )

    def __str__(self):
        return f"LoadReading {self.id}"

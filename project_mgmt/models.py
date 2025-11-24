from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class ContactInfo(models.Model):
    """An abstract class to represent a contact instance."""

    email = models.EmailField(db_column="email")
    phone = models.CharField(db_column="phone")
    street = models.CharField(db_column="street")
    street_number = models.CharField(db_column="street_number")
    street_box = models.CharField(db_column="street_box")
    zipcode = models.CharField(db_column="zipcode")
    municipity = models.CharField(db_column="municipity")
    country = models.CharField(db_column="country", max_length=2)

    class Meta:
        abstract = True


class Company(ContactInfo):
    """A class to represent a company"""

    uid = models.CharField(
        db_column="uid",
        primary_key=True,
        max_length=10,
        validators=[
            RegexValidator(r'^\d{10}$', message="Must be exactly 10 digits")
        ],
    )
    denomination = models.CharField(
        db_column="denomination",
        max_length=23,
        help_text="Name of the company."
    )
    invoice_recipient = models.EmailField(
        db_column="invoice_recipient",
        help_text="Where to send the invoice."
    )

    def __str__(self):
        return f"{self.denomination}"

    class Meta(ContactInfo.Meta):
        db_table = "companies"


class Client(ContactInfo):
    """A class to represent a client."""

    client_id = models.AutoField(
        primary_key=True
    )
    first_name = models.CharField(
        db_column="fname"
    )
    last_name = models.CharField(
        db_column="lname"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta(ContactInfo.Meta):
        db_table = "clients"


class Invoice(models.Model):
    """A class to represent an invoice instance."""

    uuid = models.UUIDField(
        db_column="invoice_uuid"
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.RESTRICT,
        db_column="company_id"
    )


class Project():
    pass


class Entry():
    pass

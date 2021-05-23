from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


"""
### Many-to-one relationship example ###

class Manufacturer(models.Model):
    # ......
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.Cascade)


### Manu-to-many relationship ###


class Topping(models.Model):
    # ......
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)


"""


# Extra Field on many to many relationship


class Human(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Human, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Human, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


"""

### Models across files ###

from geography.models import ZipCode
class Restaurant(models.Model):
    zip_code = models.ForeignKey(ZipCode, on_delete=models.SET_NULL,blank=True,null=True)

"""

"""
Field name restrictions 
1- Should not be python reserved keyword.
2- Field name should not contains more than one underscore in a row.
3- A field name cannot end with an underscore, for similar reasons.
"""

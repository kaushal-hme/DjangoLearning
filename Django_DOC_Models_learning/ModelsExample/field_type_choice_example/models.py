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

"""
### Meta options ###

Give your model metadata by using an inner class Meta.
Model (metadata) is "anything that is not a field"

"""


class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"


### Model attribute s###
"""
objects
-------
1- Through manager database operations are provided to Django.
2- Used to retrive instances from database.
3- Default name is 'objects'
4- Only accessible from model classes not model instances.

model methsods
--------------
Define custom methods on a model to add custom "row_level" functionality to your objects.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status"
        import datetime
        if self.birth_date < datetime.date(1945,8,1):
            return "Pre-boomer"
        elif self.birth_date<datetime.date(1965,1,1):
            return "Baby boomer"
        else:
            return "Post-boomer"
    
    @Property
    def full_name(self):
        "Returns the person's full name"
        return '%s %s' %( self.first_name, self.last_name)

overriding perdefined model methods
-----------------------------------

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self,*args, **kwargs):
        do_something()
        super().save(*args,**kwargs) #Call the 'real' save() method.
        do_something_else()

#you can also prevent saving
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self,*args,**kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super().save(*args,**kwargs) #Call the real save() method.


"""
"""
### Abstract base classes ###

1 - use to put common funtionality to number of other models.
2 - put "abstract=True" in meta class.
3 - this model is not used to create any database table.

"""


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

# Student model have three attributes.


"""
### Multi-table inheritance ###

1- When each model in the hierarchy is a model all by itself.
2- Each model corresponds to its own database table and can be queried and created individually.
3- Inheritance links b/w the child modela and each of it's parent(via automatically created OneToOneField)

"""


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restuarant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

# example:-
# Place.objects.filter(name="Bob's Cafe")
# Restaurant.objects.filter(name="Bob's Cafe")


"""
to be continued from Proxy models.
"""

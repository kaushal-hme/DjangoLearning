from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


"""
Chaining filters Example:
-------------------------
    Entry.objects.filter(
        headline__startswith='What'
    ).exclude(
        pub_date__gte = datetime.date.today()
    ).filter(pub_date__gte = datetime.date(2005,1,30)

    )

Filtered QuerySets are unique
-----------------------------
1- Each time you refine a QuerySet, you get a brand new QuerySet.


Retrieving a single object with get()
--------------------------------------

one_entry = Entry.objects.get(pk=1)

note - 
1 - if no result Django raise 'Entry.DoesnotExist'
2- if multiple results Django raise 'Entry.MultipleObjecgtsReturned'


Limiting QuerySets
-----------------------

1- Same as SQL LIMIT  and OFFSET clauses.

example - 
1 - Entry.objects.all()[:5]   #return first 5 objects.
2 - Entry.objects.all()[5:10] #return sixth through tenth objects.

note- 
1 - It does not actually executed the query.
2- Exception - if we are using step paramter then it executed the query in ordere to return list.
ex - Entry.objects.all()[:10:2] #return every second object of the first 10.

3- Futher filtering and ordering of sliced query is prohibited.
4- For reterieving single object use index
ex - Entry,objects.order_by('headline')[0]

"""

"""
Fields lookup
-------------
example -
Entry.objects.filter(pub_date__lte='2006-01-01')

Note - 
1-  The field specified in lookup has to be the name of a model field.
2-  Exception- ForeignKey - Field name suffixed with '_id'.
    ex - Entry.objects.filter(blog_id=4)
3- For invalid field it raises 'TypeError'

Other lookup type
------------------
##exact
example- 
    Django Query - Entry.objects.get(headline__exact="Cat bites dog")
    Equi SQL Query - Select * from table_name where headline = "Cat bites dog";

##iexact - case insensitive match
example - Blog.objects.get(name__iexact='beatles blog')

##contains - Case-sensitive containment test
example - 
    Django Query - Entry.objects.get(headline__contains = 'Lennon')
    Equi SQL Query - Select * from table_name where headline like '%Lennon%';

###others are following:-
1- startswith
2- endswith
3- istartswith
4- iendswith

Lookup that span relationships
------------------------------
Django perform 'JOINS' automatically.

"""

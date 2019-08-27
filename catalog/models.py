import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# genre
class Genre(models.Model):
    """Book genre class."""

    name = models.CharField(max_length=30, help_text='enter book genre')

    def __str__(self):
        """Representation Text"""
        return self.name

# language
class Language(models.Model):
    """Book language class"""

    name = models.CharField(max_length=30, help_text='enter book language')

    def __str__(self):
        """Representation Text"""
        return self.name


# author
class Author(models.Model):
    """Author class"""

    name = models.CharField(max_length=30, help_text ='enter author pen name')

    first_name = models.CharField(
        max_length=30, 
        help_text='enter author first name'
        )

    last_name = models.CharField(
        max_length = 100, 
        help_text='enter author last name , max 100 chars.'
        )

    date_of_birth = models.DateField(null=True, blank=True)

    date_of_deth = models.DateField(null=True, blank=True)

    def __str__(self):
        """Representation text"""

        return self.name

# book
class Book(models.Model):
    """Book model"""

    isbn = models.CharField(
        'ISBN',
        max_length =13,  
        primary_key=True, 
        help_text ='ISBN for book max 13 chars.'
        )
    
    title = models.CharField(max_length=100, help_text='books title')

    summary = models.CharField(max_length=1000, help_text='book summary text.')

    # many relationships
    language = models.ForeignKey(
        Language, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
        )

    genre = models.ManyToManyField(Genre, blank=True)

    # deleting author will not delete books 
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Representation text"""
        return self.title

# book instance
class Book_Instance(models.Model):
    """Book intance object"""

    guid = models.UUIDField(
        'GUID', 
    default=uuid.uuid4, 
    primary_key=True,
    )

    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('o','on loane'),
        ('a', 'available'),
        ('m', 'maintenance'),
    )

    status = models.CharField(
        max_length=1, 
        choices=LOAN_STATUS,
        default='a',
        )

    # many fields
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Book Instance'
        

    def __str__(self):
        """Representation text"""
        return f'{self.guid}, {self.book.title}'

from django.db import models

# models are Python classes that represent the structure of your database tables

# models is a module that contains Model class and various field classes (like CharField, IntegerField, etc.)

#When you define __str__ in your model, you specify what 
# should be shown when you print an instance of the model or view it in an interactive console.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



# more examples of models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} by {self.author}"


# a room like a chat room
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True) 
    # null is for database, blank is for form validation












#     class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-One
#     bio = models.TextField()
#     website = models.URLField()

#     def __str__(self):
#         return f"{self.user.username}'s profile"
# on_delete=models.CASCADE: If a user is deleted, their profile will also be deleted.
# Usage :
# To create a profile for an existing user:


# user = User.objects.get(username="niraj")
# profile = Profile.objects.create(user=user, bio="Backend Developer", website="https://niraj.me")
# To access the profile of a user:


# user_profile = user.profile  # Accesses the Profile instance directly
# To access the user from the profile:


# profile_user = profile.user  # Accesses the User instance directly



# Relationship Type	Field Type	Usage Example

# One-to-Many	ForeignKey	Book to Genre
# Many-to-Many	ManyToManyField	Book to Tag
# One-to-One	OneToOneField	User to Profile
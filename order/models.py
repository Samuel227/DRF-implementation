from django.db import models

# Create your models here.
class Order(models.Model):
    TYPE_BREAKFAST = 'Breakfast'
    TYPE_BRUNCH = "Brunch"
    TYPE_LUNCH = "Lunch"
    TYPE_DINNER = "Dinner"
    TYPE_CHOICES= [(TYPE_BREAKFAST, "breakfast"), (TYPE_BRUNCH, "brunch"), 
                    (TYPE_LUNCH, "lunch"), (TYPE_DINNER, "dinner")]
    
    name = models.CharField(max_length=255)
    meal = models.CharField(max_length=255, choices=TYPE_CHOICES, blank=True)
    location = models.CharField(max_length=255, unique=True, null=True)
    #created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
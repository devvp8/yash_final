from django.db import models

# Create your models here.


# class Schema(models.Model):
#     schema = models.TextField()

#     def __str__(self) -> str:
#         return self.id


# class Language(models.Model):
#     language = models.CharField(max_length=150)

#     def __str__(self) -> str:
#         return self.language

# class Prompt(models.Model):
    

# class SchemaGenerator(models.Model):
#     schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
#     language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
#     prompt = models.TextField()
#     code = models.TextField(null=True, blank=True)


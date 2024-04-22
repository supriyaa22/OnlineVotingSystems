from django.db import models

# ... edits start from here ...
class Question(models.Model):
    
    image = models.ImageField(upload_to='questions_images/', blank=True, null=True)

    def __str__(self):
        return self.question_text
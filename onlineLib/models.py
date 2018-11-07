from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from PIL import Image

# Create your models here.
class Post(models.Model):
    book_name = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)
    image = models.ImageField( default = "book_default.jpg", upload_to='book_pics')
    description = models.TextField()
    current_holder = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 185 or img.width > 275:
            output_size = (185, 275)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

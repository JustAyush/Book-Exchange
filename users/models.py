from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 80 or img.width > 80:
            output_size = (80, 80)
            img.thumbnail(output_size)
            img.save(self.image.path)

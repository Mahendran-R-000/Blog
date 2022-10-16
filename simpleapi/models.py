from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    image = models.ImageField(upload_to='postimages', blank=True)
    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
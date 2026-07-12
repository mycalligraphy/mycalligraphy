<<<<<<< HEAD
from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from gallery.models import Artwork

class Comment(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="متن نظر")
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"نظر {self.user} برای {self.artwork.title}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

=======
from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from gallery.models import Artwork

class Comment(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="متن نظر")
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"نظر {self.user} برای {self.artwork.title}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

>>>>>>> 7956767a86adae2d1e0b7eff85090f4301cedb4a

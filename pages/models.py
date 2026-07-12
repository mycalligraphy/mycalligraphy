<<<<<<< HEAD
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیام")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
    
    def __str__(self):
        return f"پیام از {self.name}"
    
    class Meta:
        verbose_name = "پیام تماس"
=======
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیام")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
    
    def __str__(self):
        return f"پیام از {self.name}"
    
    class Meta:
        verbose_name = "پیام تماس"
>>>>>>> 7956767a86adae2d1e0b7eff85090f4301cedb4a
        verbose_name_plural = "پیام‌های تماس"  
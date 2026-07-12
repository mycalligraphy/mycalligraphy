<<<<<<< HEAD
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته"
        verbose_name_plural = "دسته‌بندی‌ها"

class Artwork(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    image = models.ImageField(upload_to='gallery/', verbose_name="تصویر")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="دسته"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    views = models.IntegerField(default=0, verbose_name="تعداد بازدید")
    likes = models.IntegerField(default=0, verbose_name="تعداد لایک")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اثر هنری"
=======
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته"
        verbose_name_plural = "دسته‌بندی‌ها"

class Artwork(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    image = models.ImageField(upload_to='gallery/', verbose_name="تصویر")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="دسته"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    views = models.IntegerField(default=0, verbose_name="تعداد بازدید")
    likes = models.IntegerField(default=0, verbose_name="تعداد لایک")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اثر هنری"
>>>>>>> 7956767a86adae2d1e0b7eff85090f4301cedb4a
        verbose_name_plural = "آثار هنری"
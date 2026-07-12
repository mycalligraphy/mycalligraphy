<<<<<<< HEAD

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # ذخیره در دیتابیس
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # پیام موفقیت به کاربر
        messages.success(request, 'پیام شما با موفقیت ارسال شد. سپاسگزارم!')
        return redirect('pages:contact')
    
    return render(request, 'pages/contact.html')



    from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # ذخیره در دیتابیس
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # ارسال ایمیل به شما (مدیر سایت)
        try:
            send_mail(
                subject=f'پیام جدید از {name}',
                message=f'''
                نام: {name}
                ایمیل: {email}
                
                پیام:
                {message}
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['your_email@gmail.com'],  # ایمیل خودتان
                fail_silently=False,
            )
            
            # ارسال ایمیل تأیید به کاربر
            send_mail(
                subject='تأیید دریافت پیام شما',
                message=f'''
                سلام {name} عزیز،

                پیام شما با موفقیت دریافت شد.
                در اسرع وقت پاسخ شما را خواهم داد.

                با تشکر
                تیم خوشنویسی هنر جاودان
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            messages.success(request, 'پیام شما با موفقیت ارسال شد و ایمیل تأیید برای شما ارسال گردید.')
            
        except Exception as e:
            messages.warning(request, 'پیام شما ذخیره شد اما ارسال ایمیل با مشکل مواجه شد.')
            print(f'خطا در ارسال ایمیل: {e}')
        
        return redirect('pages:contact')
    
=======

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # ذخیره در دیتابیس
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # پیام موفقیت به کاربر
        messages.success(request, 'پیام شما با موفقیت ارسال شد. سپاسگزارم!')
        return redirect('pages:contact')
    
    return render(request, 'pages/contact.html')



    from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # ذخیره در دیتابیس
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # ارسال ایمیل به شما (مدیر سایت)
        try:
            send_mail(
                subject=f'پیام جدید از {name}',
                message=f'''
                نام: {name}
                ایمیل: {email}
                
                پیام:
                {message}
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['your_email@gmail.com'],  # ایمیل خودتان
                fail_silently=False,
            )
            
            # ارسال ایمیل تأیید به کاربر
            send_mail(
                subject='تأیید دریافت پیام شما',
                message=f'''
                سلام {name} عزیز،

                پیام شما با موفقیت دریافت شد.
                در اسرع وقت پاسخ شما را خواهم داد.

                با تشکر
                تیم خوشنویسی هنر جاودان
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            messages.success(request, 'پیام شما با موفقیت ارسال شد و ایمیل تأیید برای شما ارسال گردید.')
            
        except Exception as e:
            messages.warning(request, 'پیام شما ذخیره شد اما ارسال ایمیل با مشکل مواجه شد.')
            print(f'خطا در ارسال ایمیل: {e}')
        
        return redirect('pages:contact')
    
>>>>>>> 7956767a86adae2d1e0b7eff85090f4301cedb4a
    return render(request, 'pages/contact.html')
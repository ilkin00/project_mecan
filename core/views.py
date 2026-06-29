from django.shortcuts import render, get_object_or_404
from .models import Hizmet, Proje, IletisimMesaji, SiteSettings, GaleriResim
from django.contrib import messages
from django.shortcuts import redirect

def get_settings():
    settings, created = SiteSettings.objects.get_or_create(pk=1)
    return settings

def index(request):
    settings = get_settings()
    hizmetler = Hizmet.objects.filter(is_active=True)[:3]
    projeler = Proje.objects.filter(is_active=True)[:3]
    return render(request, 'core/index.html', {
        'settings': settings,
        'hizmetler': hizmetler,
        'projeler': projeler
    })

def hakkimizda(request):
    settings = get_settings()
    return render(request, 'core/hakkimizda.html', {
        'settings': settings
    })

def hizmetler(request):
    settings = get_settings()
    hizmetler = Hizmet.objects.filter(is_active=True)
    return render(request, 'core/hizmetler.html', {
        'settings': settings,
        'hizmetler': hizmetler
    })

def projeler(request):
    settings = get_settings()
    projeler = Proje.objects.filter(is_active=True)
    return render(request, 'core/projeler.html', {
        'settings': settings,
        'projeler': projeler
    })

def iletisim(request):
    settings = get_settings()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and phone and message:
            IletisimMesaji.objects.create(
                name=name,
                phone=phone,
                email=email or '',
                message=message
            )
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('core:iletisim')
        else:
            messages.error(request, 'Пожалуйста, заполните все обязательные поля.')
    
    return render(request, 'core/iletisim.html', {
        'settings': settings
    })

def hizmet_detay(request, slug):
    settings = get_settings()
    hizmet = get_object_or_404(Hizmet, slug=slug, is_active=True)
    
    # Galeri resimlerini al
    galeri_resimleri = GaleriResim.objects.filter(hizmet=hizmet, is_active=True).order_by('order', 'created_at')
    
    video_source = None
    video_type = None
    if hizmet.video_url:
        video_source = hizmet.video_url
        video_type = 'youtube'
    elif hizmet.video_file and hizmet.video_file.url:
        video_source = hizmet.video_file.url
        video_type = 'file'
    
    image_url = None
    if hizmet.image and hizmet.image.url:
        image_url = hizmet.image.url
    
    return render(request, 'core/hizmet-detay/insaat-ve-iskele.html', {
        'settings': settings,
        'hizmet': hizmet,
        'image_url': image_url,
        'video_source': video_source,
        'video_type': video_type,
        'galeri_resimleri': galeri_resimleri
    })

def proje_detay(request, slug):
    settings = get_settings()
    proje = get_object_or_404(Proje, slug=slug, is_active=True)
    
    # Galeri resimlerini al
    galeri_resimleri = GaleriResim.objects.filter(proje=proje, is_active=True).order_by('order', 'created_at')
    
    video_source = None
    video_type = None
    if proje.video_url:
        video_source = proje.video_url
        video_type = 'youtube'
    elif proje.video_file and proje.video_file.url:
        video_source = proje.video_file.url
        video_type = 'file'
    
    image_url = None
    if proje.image and proje.image.url:
        image_url = proje.image.url
    
    return render(request, 'core/proje-detay/villa-tadilat.html', {
        'settings': settings,
        'proje': proje,
        'image_url': image_url,
        'video_source': video_source,
        'video_type': video_type,
        'galeri_resimleri': galeri_resimleri
    })

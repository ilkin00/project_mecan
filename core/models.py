from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator

# Default İkonlar
DEFAULT_ICONS = [
    ('fa-hard-hat', 'Каска'),
    ('fa-tools', 'Инструменты'),
    ('fa-layer-group', 'Слои'),
    ('fa-water', 'Капля воды'),
    ('fa-bolt', 'Молния'),
    ('fa-paint-roller', 'Валик'),
    ('fa-home', 'Дом'),
    ('fa-building', 'Здание'),
    ('fa-hammer', 'Молоток'),
    ('fa-wrench', 'Гаечный ключ'),
    ('fa-cogs', 'Шестерни'),
    ('fa-plug', 'Вилка'),
    ('fa-lightbulb', 'Лампочка'),
    ('fa-shield-alt', 'Щит'),
    ('fa-ruler-combined', 'Линейка'),
    ('fa-drafting-compass', 'Циркуль'),
    ('fa-cube', 'Куб'),
    ('fa-chart-line', 'График'),
    ('fa-phone-alt', 'Телефон'),
    ('fa-envelope', 'Конверт'),
    ('fa-map-marker-alt', 'Местоположение'),
    ('fa-calendar-alt', 'Календарь'),
    ('fa-clock', 'Часы'),
    ('fa-user', 'Пользователь'),
    ('fa-users', 'Пользователи'),
    ('fa-star', 'Звезда'),
    ('fa-trophy', 'Кубок'),
    ('fa-check-circle', 'Галочка'),
    ('fa-thumbs-up', 'Лайк'),
]

DEFAULT_BG_COLORS = [
    ('#1a1a2e', 'Тёмно-синий'),
    ('#1a2e1a', 'Тёмно-зелёный'),
    ('#2e1a1a', 'Тёмно-красный'),
    ('#1a2e2e', 'Тёмно-бирюзовый'),
    ('#2e2e1a', 'Тёмно-оливковый'),
    ('#2e1a2e', 'Тёмно-фиолетовый'),
    ('#1a1a1a', 'Чёрный'),
    ('#2a2a2a', 'Тёмно-серый'),
    ('#1a2a3a', 'Тёмно-синий'),
    ('#3a2a1a', 'Тёмно-коричневый'),
]


class SiteSettings(models.Model):
    # ==================== 1. ОСНОВНЫЕ НАСТРОЙКИ ====================
    site_title = models.CharField(max_length=200, default='Usta İnşaat', verbose_name="Название сайта")
    site_description = models.TextField(default='Строительная компания с 15-летним опытом', verbose_name="Описание сайта")
    site_logo = models.CharField(max_length=200, default='Ustaİnşaat', verbose_name="Логотип текст")

    # ==================== 2. НАВИГАЦИЯ ====================
    nav_home = models.CharField(max_length=50, default='Главная', verbose_name="Навигация - Главная")
    nav_about = models.CharField(max_length=50, default='О нас', verbose_name="Навигация - О нас")
    nav_services = models.CharField(max_length=50, default='Услуги', verbose_name="Навигация - Услуги")
    nav_projects = models.CharField(max_length=50, default='Проекты', verbose_name="Навигация - Проекты")
    nav_contact = models.CharField(max_length=50, default='Контакты', verbose_name="Навигация - Контакты")

    # ==================== 2.1 NAVİGASYON LİNKLERİ (Admin'den kontrol) ====================
    nav_link_telegram = models.CharField(max_length=200, default='https://t.me/ustainsaat', blank=True, verbose_name="Telegram Linki")
    nav_link_whatsapp = models.CharField(max_length=200, default='https://wa.me/905551234567', blank=True, verbose_name="WhatsApp Linki")
    nav_link_phone = models.CharField(max_length=50, default='05551234567', blank=True, verbose_name="Telefon Numarası")
    nav_link_email = models.CharField(max_length=100, default='info@ustainsaat.com', blank=True, verbose_name="Email Adresi")
    
    # Sosyal Medya Linkleri
    social_facebook = models.CharField(max_length=200, default='https://facebook.com/ustainsaat', blank=True, verbose_name="Facebook")
    social_instagram = models.CharField(max_length=200, default='https://instagram.com/ustainsaat', blank=True, verbose_name="Instagram")
    social_youtube = models.CharField(max_length=200, default='https://youtube.com/ustainsaat', blank=True, verbose_name="YouTube")
    social_telegram = models.CharField(max_length=200, default='https://t.me/ustainsaat', blank=True, verbose_name="Telegram")

    # ==================== 3. ГЛАВНЫЙ ЭКРАН ====================
    hero_title = models.CharField(max_length=200, default='Надёжный Строитель', verbose_name="Hero - Заголовок")
    hero_title_highlight = models.CharField(max_length=200, default='Премиум', verbose_name="Hero - Выделенный текст")
    hero_subtitle = models.TextField(default='15-летний опыт в строительстве, ремонте, отделке и дизайне интерьеров.', verbose_name="Hero - Описание")
    hero_btn_text = models.CharField(max_length=50, default='Получить предложение', verbose_name="Hero - Кнопка 1")
    hero_btn_projects = models.CharField(max_length=50, default='Наши проекты', verbose_name="Hero - Кнопка 2")

    # ==================== 4. СТАТИСТИКА (eski) ====================
    stat_year = models.CharField(max_length=50, default='Лет опыта', verbose_name="Статистика - Лет опыта")
    stat_clients = models.CharField(max_length=50, default='Довольных клиентов', verbose_name="Статистика - Клиентов")
    stat_satisfaction = models.CharField(max_length=50, default='Удовлетворённость %', verbose_name="Статистика - Удовлетворённость")

    # ==================== 4.1 HERO STATS (Admin'den kontrol) ====================
    hero_stats_active = models.BooleanField(default=True, verbose_name="Hero Stats - Aktif/Pasif")
    
    hero_stat_1_number = models.CharField(max_length=50, default='15', verbose_name="Stat 1 - Sayı")
    hero_stat_1_label = models.CharField(max_length=100, default='Лет опыта', verbose_name="Stat 1 - Etiket")
    
    hero_stat_2_number = models.CharField(max_length=50, default='120', verbose_name="Stat 2 - Sayı")
    hero_stat_2_label = models.CharField(max_length=100, default='Довольных клиентов', verbose_name="Stat 2 - Etiket")
    
    hero_stat_3_number = models.CharField(max_length=50, default='98', verbose_name="Stat 3 - Sayı")
    hero_stat_3_label = models.CharField(max_length=100, default='Удовлетворённость %', verbose_name="Stat 3 - Etiket")

    # ==================== 5. УСЛУГИ ====================
    services_title = models.CharField(max_length=200, default='Наши услуги', verbose_name="Услуги - Заголовок")
    services_subtitle = models.CharField(max_length=200, default='Самые востребованные услуги нашей компании', verbose_name="Услуги - Подзаголовок")
    services_all_btn = models.CharField(max_length=50, default='Все услуги', verbose_name="Услуги - Кнопка все")
    services_detail = models.CharField(max_length=50, default='Подробнее', verbose_name="Услуги - Кнопка подробнее")

    # ==================== 6. ПРОЕКТЫ ====================
    projects_title = models.CharField(max_length=200, default='Наши проекты', verbose_name="Проекты - Заголовок")
    projects_subtitle = models.CharField(max_length=200, default='Примеры выполненных работ', verbose_name="Проекты - Подзаголовок")
    projects_all_btn = models.CharField(max_length=50, default='Все проекты', verbose_name="Проекты - Кнопка все")
    projects_detail = models.CharField(max_length=50, default='Подробнее', verbose_name="Проекты - Кнопка подробнее")

    # ==================== 7. О НАС ====================
    about_title = models.CharField(max_length=200, default='О нас', verbose_name="О нас - Заголовок")
    about_highlight = models.CharField(max_length=200, default='Почему Usta İnşaat?', verbose_name="О нас - Выделенный текст")
    about_text = models.TextField(default='С 2008 года мы реализуем проекты в Стамбуле и по всей Турции.', verbose_name="О нас - Текст")
    about_btn = models.CharField(max_length=50, default='Связаться', verbose_name="О нас - Кнопка")
    about_item_1 = models.CharField(max_length=200, default='Квалифицированная команда', verbose_name="О нас - Пункт 1")
    about_item_2 = models.CharField(max_length=200, default='Своевременная сдача объектов', verbose_name="О нас - Пункт 2")
    about_item_3 = models.CharField(max_length=200, default='2 года гарантии на работу', verbose_name="О нас - Пункт 3")
    about_item_4 = models.CharField(max_length=200, default='Полное управление проектом', verbose_name="О нас - Пункт 4")
    about_item_5 = models.CharField(max_length=200, default='Круглосуточная поддержка', verbose_name="О нас - Пункт 5")

    # ==================== 8. КОНТАКТЫ ====================
    contact_title = models.CharField(max_length=200, default='Контакты', verbose_name="Контакты - Заголовок")
    contact_subtitle = models.CharField(max_length=200, default='Свяжитесь с нами для бесплатной консультации', verbose_name="Контакты - Подзаголовок")
    contact_text = models.TextField(default='Звоните или пишите в WhatsApp, или заполните форму', verbose_name="Контакты - Текст")
    contact_phone_label = models.CharField(max_length=50, default='Телефон', verbose_name="Контакты - Телефон")
    contact_phone = models.CharField(max_length=50, default='0555 123 45 67', verbose_name="Контакты - Номер телефона")
    contact_whatsapp_label = models.CharField(max_length=50, default='WhatsApp', verbose_name="Контакты - WhatsApp")
    contact_whatsapp = models.CharField(max_length=50, default='0555 123 45 67', verbose_name="Контакты - Номер WhatsApp")
    contact_email_label = models.CharField(max_length=50, default='Email', verbose_name="Контакты - Email")
    contact_email = models.CharField(max_length=100, default='info@ustainsaat.com', verbose_name="Контакты - Email адрес")
    contact_address_label = models.CharField(max_length=50, default='Адрес', verbose_name="Контакты - Адрес")
    contact_address = models.CharField(max_length=200, default='Стамбул / Турция', verbose_name="Контакты - Адрес текст")

    # ==================== 9. ФОРМА СВЯЗИ ====================
    form_name = models.CharField(max_length=50, default='Ваше имя', verbose_name="Форма - Имя")
    form_phone = models.CharField(max_length=50, default='Ваш телефон', verbose_name="Форма - Телефон")
    form_email = models.CharField(max_length=50, default='Ваш email', verbose_name="Форма - Email")
    form_message = models.CharField(max_length=50, default='Опишите ваш проект...', verbose_name="Форма - Сообщение")
    form_btn = models.CharField(max_length=50, default='Отправить', verbose_name="Форма - Кнопка")

    # ==================== 10. ДЕТАЛЬНЫЕ СТРАНИЦЫ ====================
    detail_price_label = models.CharField(max_length=50, default='Стоимость', verbose_name="Детали - Цена")
    detail_price_note = models.CharField(max_length=200, default='* за м² (начальная цена)', verbose_name="Детали - Примечание к цене")
    detail_features_label = models.CharField(max_length=50, default='Особенности', verbose_name="Детали - Особенности")
    detail_gallery_label = models.CharField(max_length=50, default='Галерея', verbose_name="Детали - Галерея")
    detail_video_label = models.CharField(max_length=50, default='Видео', verbose_name="Детали - Видео")
    detail_back_btn = models.CharField(max_length=50, default='Назад к услугам', verbose_name="Детали - Кнопка назад")
    detail_order_btn = models.CharField(max_length=50, default='Заказать', verbose_name="Детали - Кнопка заказа")

    # ==================== 10.1 ДЕТАЛЬНЫЕ БЛОКИ ====================
    detail_block_1_label = models.CharField(max_length=100, default='Срок', verbose_name="Блок 1 - Этикетка")
    detail_block_1_value = models.CharField(max_length=200, default='3-12 месяцев', verbose_name="Блок 1 - Значение")
    detail_block_1_active = models.BooleanField(default=True, verbose_name="Блок 1 - Активен")
    
    detail_block_2_label = models.CharField(max_length=100, default='Гарантия', verbose_name="Блок 2 - Этикетка")
    detail_block_2_value = models.CharField(max_length=200, default='2 года', verbose_name="Блок 2 - Значение")
    detail_block_2_active = models.BooleanField(default=True, verbose_name="Блок 2 - Активен")
    
    detail_block_3_label = models.CharField(max_length=100, default='Ключи', verbose_name="Блок 3 - Этикетка")
    detail_block_3_value = models.CharField(max_length=200, default='Под ключ', verbose_name="Блок 3 - Значение")
    detail_block_3_active = models.BooleanField(default=True, verbose_name="Блок 3 - Активен")
    
    detail_block_4_label = models.CharField(max_length=100, default='Локация', verbose_name="Блок 4 - Этикетка")
    detail_block_4_value = models.CharField(max_length=200, default='Стамбул и область', verbose_name="Блок 4 - Значение")
    detail_block_4_active = models.BooleanField(default=True, verbose_name="Блок 4 - Активен")
    
    detail_block_5_label = models.CharField(max_length=100, default='', blank=True, verbose_name="Блок 5 - Этикетка")
    detail_block_5_value = models.CharField(max_length=200, default='', blank=True, verbose_name="Блок 5 - Значение")
    detail_block_5_active = models.BooleanField(default=False, verbose_name="Блок 5 - Активен")
    
    detail_block_6_label = models.CharField(max_length=100, default='', blank=True, verbose_name="Блок 6 - Этикетка")
    detail_block_6_value = models.CharField(max_length=200, default='', blank=True, verbose_name="Блок 6 - Значение")
    detail_block_6_active = models.BooleanField(default=False, verbose_name="Блок 6 - Активен")

    # ==================== 11. СТРАНИЦЫ ====================
    page_services_title = models.CharField(max_length=200, default='Наши услуги', verbose_name="Страница - Услуги заголовок")
    page_services_subtitle = models.CharField(max_length=200, default='Профессиональные решения для вашего строительства', verbose_name="Страница - Услуги подзаголовок")
    page_projects_title = models.CharField(max_length=200, default='Наши проекты', verbose_name="Страница - Проекты заголовок")
    page_projects_subtitle = models.CharField(max_length=200, default='Примеры выполненных работ', verbose_name="Страница - Проекты подзаголовок")
    page_about_title = models.CharField(max_length=200, default='О нас', verbose_name="Страница - О нас заголовок")
    page_about_subtitle = models.CharField(max_length=200, default='Более 15 лет опыта в строительной отрасли', verbose_name="Страница - О нас подзаголовок")
    page_contact_title = models.CharField(max_length=200, default='Контакты', verbose_name="Страница - Контакты заголовок")
    page_contact_subtitle = models.CharField(max_length=200, default='Свяжитесь с нами для бесплатной консультации', verbose_name="Страница - Контакты подзаголовок")

    # ==================== 12. FOOTER ====================
    footer_text = models.CharField(max_length=200, default='Качественная работа, надёжные решения.', verbose_name="Footer - Текст")
    footer_copyright = models.CharField(max_length=200, default='Все права защищены.', verbose_name="Footer - Авторские права")
    footer_about = models.CharField(max_length=200, default='Качественная работа, надёжные решения.', verbose_name="Footer - О компании")

    # ==================== 13. LOADER ====================
    loader_text = models.CharField(max_length=50, default='Загрузка...', verbose_name="Загрузка - Текст")

    # ==================== 14. МЕТА ====================
    meta_keywords = models.CharField(max_length=500, default='строительство, ремонт, отделка, дизайн, Стамбул', verbose_name="Meta - Ключевые слова")
    meta_author = models.CharField(max_length=200, default='Usta İnşaat', verbose_name="Meta - Автор")

    # ==================== 15. ЦВЕТА ТЕМЫ ====================
    theme_bg_primary = models.CharField(max_length=50, default='#0a0a0a', verbose_name="Основной фон")
    theme_bg_secondary = models.CharField(max_length=50, default='#111122', verbose_name="Вторичный фон")
    theme_bg_card = models.CharField(max_length=50, default='#1a1a2e', verbose_name="Фон карточек")
    theme_bg_card_hover = models.CharField(max_length=50, default='#222244', verbose_name="Фон карточек (hover)")
    theme_text_primary = models.CharField(max_length=50, default='#ffffff', verbose_name="Основной текст")
    theme_text_secondary = models.CharField(max_length=50, default='#b8b8d0', verbose_name="Вторичный текст")
    theme_text_muted = models.CharField(max_length=50, default='#666688', verbose_name="Тусклый текст")
    theme_gradient_1_start = models.CharField(max_length=50, default='#00d4ff', verbose_name="Градиент 1 - Начало")
    theme_gradient_1_end = models.CharField(max_length=50, default='#7b2ffc', verbose_name="Градиент 1 - Конец")
    theme_gradient_2_start = models.CharField(max_length=50, default='#f093fb', verbose_name="Градиент 2 - Начало")
    theme_gradient_2_end = models.CharField(max_length=50, default='#f5576c', verbose_name="Градиент 2 - Конец")
    theme_gradient_3_start = models.CharField(max_length=50, default='#4facfe', verbose_name="Градиент 3 - Начало")
    theme_gradient_3_end = models.CharField(max_length=50, default='#00f2fe', verbose_name="Градиент 3 - Конец")
    theme_accent_1 = models.CharField(max_length=50, default='#00d4ff', verbose_name="Акцент 1")
    theme_accent_2 = models.CharField(max_length=50, default='#7b2ffc', verbose_name="Акцент 2")
    theme_accent_3 = models.CharField(max_length=50, default='#f5576c', verbose_name="Акцент 3")
    theme_border_color = models.CharField(max_length=50, default='rgba(255, 255, 255, 0.06)', verbose_name="Цвет границы")
    theme_shadow = models.CharField(max_length=100, default='0 8px 40px rgba(0, 0, 0, 0.5)', verbose_name="Тень")
    theme_shadow_glow = models.CharField(max_length=100, default='0 0 60px rgba(0, 212, 255, 0.1)', verbose_name="Свечение")
    theme_btn_primary = models.CharField(max_length=50, default='#00d4ff', verbose_name="Кнопка - Основная")
    theme_btn_primary_hover = models.CharField(max_length=50, default='#7b2ffc', verbose_name="Кнопка - Основная (hover)")
    theme_btn_outline = models.CharField(max_length=50, default='#00d4ff', verbose_name="Кнопка - Контурная")
    theme_hero_bg_start = models.CharField(max_length=50, default='#0a0a0a', verbose_name="Hero - Фон начало")
    theme_hero_bg_end = models.CharField(max_length=50, default='#0a0a0a', verbose_name="Hero - Фон конец")
    theme_hero_glow_1 = models.CharField(max_length=50, default='rgba(0, 212, 255, 0.06)', verbose_name="Hero - Свечение 1")
    theme_hero_glow_2 = models.CharField(max_length=50, default='rgba(123, 47, 252, 0.06)', verbose_name="Hero - Свечение 2")
    theme_card_shadow = models.CharField(max_length=100, default='0 8px 40px rgba(0, 0, 0, 0.4)', verbose_name="Тень карточек")
    theme_card_glow = models.CharField(max_length=100, default='0 0 60px rgba(0, 212, 255, 0.1)', verbose_name="Свечение карточек")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            existing = SiteSettings.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)


# ==================== GALERİ ====================
class GaleriResim(models.Model):
    hizmet = models.ForeignKey('Hizmet', on_delete=models.CASCADE, related_name='resimler', null=True, blank=True)
    proje = models.ForeignKey('Proje', on_delete=models.CASCADE, related_name='resimler', null=True, blank=True)
    image = models.ImageField(upload_to='galeri/%Y/%m/%d/', verbose_name="Resim")
    title = models.CharField(max_length=200, blank=True, verbose_name="Başlık")
    description = models.TextField(blank=True, verbose_name="Açıklama")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Galeri Resmi"
        verbose_name_plural = "Galeri Resimleri"
        ordering = ['order', 'created_at']

    def __str__(self):
        if self.hizmet:
            return f"{self.hizmet.title} - {self.image.name}"
        elif self.proje:
            return f"{self.proje.title} - {self.image.name}"
        return self.image.name


class Hizmet(models.Model):
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    title = models.CharField(max_length=200, verbose_name="Название")
    icon = models.CharField(max_length=50, choices=DEFAULT_ICONS, default='fa-hard-hat', verbose_name="Иконка")
    description = models.TextField(verbose_name="Краткое описание")
    detail = models.TextField(verbose_name="Детальное описание")
    price = models.CharField(max_length=100, verbose_name="Цена")
    price_note = models.CharField(max_length=200, blank=True, verbose_name="Примечание к цене")
    features = models.JSONField(default=list, verbose_name="Особенности")
    image = models.ImageField(upload_to='hizmetler/kapak/', blank=True, null=True, verbose_name="Обложка")
    gallery_images = models.JSONField(default=list, blank=True, verbose_name="Галерея (устаревший)")
    video_url = models.URLField(blank=True, verbose_name="YouTube URL")
    video_file = models.FileField(upload_to='videolar/', blank=True, null=True, verbose_name="Видео файл")
    order = models.IntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Proje(models.Model):
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    title = models.CharField(max_length=200, verbose_name="Название")
    icon = models.CharField(max_length=50, choices=DEFAULT_ICONS, default='fa-home', verbose_name="Иконка")
    bg_color = models.CharField(max_length=50, choices=DEFAULT_BG_COLORS, default='#1a1a2e', verbose_name="Цвет фона")
    description = models.TextField(verbose_name="Краткое описание")
    detail = models.TextField(verbose_name="Детальное описание")
    date = models.CharField(max_length=100, verbose_name="Дата")
    area = models.CharField(max_length=100, verbose_name="Площадь")
    location = models.CharField(max_length=200, verbose_name="Местоположение")
    duration = models.CharField(max_length=100, verbose_name="Длительность")
    price = models.CharField(max_length=100, verbose_name="Стоимость")
    features = models.JSONField(default=list, verbose_name="Особенности")
    image = models.ImageField(upload_to='projeler/kapak/', blank=True, null=True, verbose_name="Обложка")
    gallery_images = models.JSONField(default=list, blank=True, verbose_name="Галерея (устаревший)")
    video_url = models.URLField(blank=True, verbose_name="YouTube URL")
    video_file = models.FileField(upload_to='videolar/', blank=True, null=True, verbose_name="Видео файл")
    order = models.IntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class IletisimMesaji(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d.%m.%Y %H:%M')}"

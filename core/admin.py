from django.contrib import admin
from django.utils.html import format_html
from .models import Hizmet, Proje, IletisimMesaji, SiteSettings, GaleriResim


class GaleriResimInline(admin.TabularInline):
    model = GaleriResim
    extra = 3
    fields = ['image', 'title', 'description', 'order', 'is_active', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit:cover;border-radius:4px;border:1px solid #ddd;" />',
                obj.image.url
            )
        return '-'
    image_preview.short_description = 'Önizleme'


@admin.register(GaleriResim)
class GaleriResimAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview', 'hizmet', 'proje', 'title', 'order', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description', 'hizmet__title', 'proje__title']
    ordering = ['order']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit:cover;border-radius:4px;border:1px solid #ddd;" />',
                obj.image.url
            )
        return '-'
    image_preview.short_description = 'Önizleme'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'site_title']
    fieldsets = (
        ('🏠 ОСНОВНЫЕ НАСТРОЙКИ', {
            'fields': ('site_title', 'site_description', 'site_logo')
        }),
        ('📱 НАВИГАЦИЯ', {
            'fields': ('nav_home', 'nav_about', 'nav_services', 'nav_projects', 'nav_contact')
        }),
        ('🌟 ГЛАВНЫЙ ЭКРАН', {
            'fields': ('hero_title', 'hero_title_highlight', 'hero_subtitle', 'hero_btn_text', 'hero_btn_projects')
        }),
        ('📊 СТАТИСТИКА', {
            'fields': ('stat_year', 'stat_clients', 'stat_satisfaction')
        }),
        ('🛠️ УСЛУГИ', {
            'fields': ('services_title', 'services_subtitle', 'services_all_btn', 'services_detail')
        }),
        ('🏗️ ПРОЕКТЫ', {
            'fields': ('projects_title', 'projects_subtitle', 'projects_all_btn', 'projects_detail')
        }),
        ('ℹ️ О НАС', {
            'fields': ('about_title', 'about_highlight', 'about_text', 'about_btn',
                      'about_item_1', 'about_item_2', 'about_item_3', 'about_item_4', 'about_item_5')
        }),
        ('📞 КОНТАКТЫ', {
            'fields': ('contact_title', 'contact_subtitle', 'contact_text',
                      'contact_phone_label', 'contact_phone',
                      'contact_whatsapp_label', 'contact_whatsapp',
                      'contact_email_label', 'contact_email',
                      'contact_address_label', 'contact_address')
        }),
        ('📝 ФОРМА СВЯЗИ', {
            'fields': ('form_name', 'form_phone', 'form_email', 'form_message', 'form_btn')
        }),
        ('📄 ДЕТАЛЬНЫЕ СТРАНИЦЫ - ОСНОВНЫЕ', {
            'fields': ('detail_price_label', 'detail_price_note', 'detail_features_label',
                      'detail_gallery_label', 'detail_video_label',
                      'detail_back_btn', 'detail_order_btn')
        }),
        ('📄 ДЕТАЛЬНЫЕ СТРАНИЦЫ - ДОП. БЛОКИ (С checkbox)', {
            'fields': (
                ('detail_block_1_label', 'detail_block_1_value', 'detail_block_1_active'),
                ('detail_block_2_label', 'detail_block_2_value', 'detail_block_2_active'),
                ('detail_block_3_label', 'detail_block_3_value', 'detail_block_3_active'),
                ('detail_block_4_label', 'detail_block_4_value', 'detail_block_4_active'),
                ('detail_block_5_label', 'detail_block_5_value', 'detail_block_5_active'),
                ('detail_block_6_label', 'detail_block_6_value', 'detail_block_6_active'),
            ),
            'description': 'Her bloğu aktif/pasif yapabilir, etiket ve değerini değiştirebilirsiniz.'
        }),
        ('📋 СТРАНИЦЫ', {
            'fields': ('page_services_title', 'page_services_subtitle',
                      'page_projects_title', 'page_projects_subtitle',
                      'page_about_title', 'page_about_subtitle',
                      'page_contact_title', 'page_contact_subtitle')
        }),
        ('🦶 FOOTER', {
            'fields': ('footer_text', 'footer_copyright', 'footer_about')
        }),
        ('⏳ ЗАГРУЗКА', {
            'fields': ('loader_text',)
        }),
        ('🔍 МЕТА ТЕГИ', {
            'fields': ('meta_keywords', 'meta_author')
        }),
        ('🎨 ЦВЕТА ТЕМЫ', {
            'fields': (
                ('theme_bg_primary', 'theme_bg_secondary'),
                ('theme_bg_card', 'theme_bg_card_hover'),
                ('theme_text_primary', 'theme_text_secondary', 'theme_text_muted'),
                ('theme_gradient_1_start', 'theme_gradient_1_end'),
                ('theme_gradient_2_start', 'theme_gradient_2_end'),
                ('theme_gradient_3_start', 'theme_gradient_3_end'),
                ('theme_accent_1', 'theme_accent_2', 'theme_accent_3'),
                ('theme_border_color', 'theme_shadow', 'theme_shadow_glow'),
                ('theme_btn_primary', 'theme_btn_primary_hover', 'theme_btn_outline'),
                ('theme_hero_bg_start', 'theme_hero_bg_end'),
                ('theme_hero_glow_1', 'theme_hero_glow_2'),
                ('theme_card_shadow', 'theme_card_glow'),
            ),
        }),
    )

    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return True


@admin.register(Hizmet)
class HizmetAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_preview', 'price', 'image_preview', 'is_active', 'order']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description', 'detail']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['order', 'title']
    inlines = [GaleriResimInline]

    def icon_preview(self, obj):
        return format_html('<i class="fas {}" style="font-size:20px;"></i>', obj.icon)
    icon_preview.short_description = 'Иконка'

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:4px;" />',
                obj.image.url
            )
        return '-'
    image_preview.short_description = 'Обложка'


@admin.register(Proje)
class ProjeAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_preview', 'color_preview', 'image_preview', 'is_active', 'order']
    list_filter = ['is_active', 'location', 'bg_color', 'created_at']
    search_fields = ['title', 'description', 'detail', 'location']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['order', 'title']
    inlines = [GaleriResimInline]

    def icon_preview(self, obj):
        return format_html('<i class="fas {}" style="font-size:20px;"></i>', obj.icon)
    icon_preview.short_description = 'Иконка'

    def color_preview(self, obj):
        return format_html(
            '<div style="width:40px;height:30px;background:{};border-radius:4px;border:1px solid #ccc;"></div>',
            obj.bg_color
        )
    color_preview.short_description = 'Цвет'

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:4px;" />',
                obj.image.url
            )
        return '-'
    image_preview.short_description = 'Обложка'


@admin.register(IletisimMesaji)
class IletisimMesajiAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'phone', 'email', 'message']
    readonly_fields = ['created_at']
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Отметить как прочитанное"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Отметить как непрочитанное"

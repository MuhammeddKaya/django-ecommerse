from .models import Category

# oluşturduğumuz bu fonksiyonu settings.py dosyasında templates altında tanımlıyoruz
# örnek:
            # 'context_processors': [
            #     'django.template.context_processors.debug',
            #     'django.template.context_processors.request',
            #     'django.contrib.auth.context_processors.auth',
            #     'django.contrib.messages.context_processors.messages',
            #     'apps.category.contex_processors.menu_links',
            # ],

# bu sayede istediğimiz herhangi bir template de links objelerini kullanabiliriz

def menu_links(requests):
    links  = Category.objects.all()
    return dict(links=links)
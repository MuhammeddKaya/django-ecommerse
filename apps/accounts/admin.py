from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.


#   Aşağıdaki kod bloğu, Account modelini Django yönetici arayüzüne kaydederken, AccountAdmin classını kullanarak 
# özelleştirilmiş bir görünüm ayarlar. Bu görünümde Account modelinin hangi alanlarının gösterileceği, 
# filtrelerin nasıl uygulanacağı ve daha birçok ayar belirlenebilir.

#   AccountAdmin classı, UserAdmin classından miras alır ve Account modelinin Django yönetici arayüzünde nasıl 
# görüntüleneceğini belirlemek için özelleştirilmiş ayarlar sağlar. Örneğin list_display özelliği, hangi alanların 
# Account modeli için listeleneceğini belirler ve list_display_links özelliği, hangi alanların üzerine tıklandığında 
# ayrıntılı görünümün açılacağını belirler.

#   readonly_fields özelliği, bu alanların düzenlenemez olduğunu belirler. filter_horizontal ve list_filter özellikleri, 
# sırasıyla, çoklu seçim alanlarını daha kullanışlı hale getirmek için özelleştirilmiş bir görünüm sağlar ve liste 
# görüntüsünde filtrelemek için kullanılır. fieldsets özelliği, Account modelinin hangi alanlarının düzenlenebileceğini 
# belirler.

# Son olarak, admin.site.register(Account,AccountAdmin) satırı, Account modelini Django yönetici arayüzüne kaydeder ve 
# özelleştirilmiş AccountAdmin classını kullanarak modelin görünümünü ayarlar.


class AccountAdmin(UserAdmin):
    list_display          = ('email','first_name','last_name','last_login','date_joined','is_active')
    list_display_links    = ('email','first_name','last_name')
    readonly_fields       = ('last_login','date_joined')


    filter_horizontal     = ()
    list_filter           = ()
    fieldsets             = ()

admin.site.register(Account,AccountAdmin)
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_us, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/portfolio-item/<int:pk>', views.portfolio_item, name='portfolio_item'),
    path('services/', views.services, name='services'),
]

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

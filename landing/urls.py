from django.urls import path, include
from rest_framework.routers import DefaultRouter

from landing import views


router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'main-block', views.MainBlockViewSet)
router.register(r'promo', views.PromoViewSet)
router.register(r'trending', views.TrendingViewSet)
router.register(r'size', views.SizeViewSet)
router.register(r'testimonial', views.TestimonialViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'blog', views.BlogViewSet)
router.register(r'feature', views.FeatureViewSet)

urlpatterns = [
    path('landing/', include(router.urls)),
]

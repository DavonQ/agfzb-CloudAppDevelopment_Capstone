from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Existing URL patterns
    path('', views.get_dealerships, name='index'),  # Default home page
    path('about/', views.about, name='about'),  # About Us page

    # path for contact us view
    path('contact/', views.contact, name='contact'),

    # path for registration
    path('registration/', views.registration_request, name='registration'),

    # path for login
    path('login/', views.login_request, name='login'),

    # path for logout
    path('logout/', views.logout_request, name='logout'),

    # path for dealer reviews view
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='get_dealer_details'),

    # path for add a review view
    path('add_review/<int:dealer_id>/', views.add_review, name='add_review'),

    # Default path for index (get_dealerships) view
    path('', views.get_dealerships, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

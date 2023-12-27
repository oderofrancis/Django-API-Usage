from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.endpoint, name='endpoint'),

    # Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('advocate/', views.advocate_list, name='advocates'),
    # path('advocate/<str:username>', views.advocates_detail, name='advocate_detail'),
    path('advocate/<str:username>', views.AdvoctaesDetail.as_view(), name='advocate_detail'),

    #companies
    path('companies/', views.company_list, name='companies'),
    # company/:id
    # path('company/<str:name>', views.CompanyDetail.as_view(), name='company_detail'),  
]
from django.urls import path, include
from .views import LanguageView, DetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', LanguageView.as_view()),
    path('<int:id>/', DetailView.as_view()),
    path('token/', obtain_auth_token),
    path('rest-auth/', include('rest_auth.urls'))

]

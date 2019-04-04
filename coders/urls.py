from django.urls import include, path
from coders import views

app_name = 'coders'
urlpatterns = [
    path('signup/', views.SignUpCreateView.as_view(), name='sign_up'),
    path('profile/<str:username>/', views.UserProfileDetailView.as_view(), name='user_info')

]

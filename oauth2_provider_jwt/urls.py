from django.urls import re_path as url
from oauth2_provider import views

from .views import TokenView

app_name = "oauth2_provider_jwt"

urlpatterns = [
    url(r"^authorize/$", views.AuthorizationView.as_view(), name="authorize"),
    url(r"^token/$", TokenView.as_view(), name="token"),
    url(r"^revoke_token/$", views.RevokeTokenView.as_view(),
        name="revoke-token"),
    url(r"^introspect/$", views.IntrospectTokenView.as_view(),
        name="introspect"),
]

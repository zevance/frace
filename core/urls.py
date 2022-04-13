import imp
from django.urls import path
from .views import(
    AboutUsView,
    ContactUsView,
    IndexView,
    TeamMemberDetailsView,
    TeamMembersView,
    MemberDetailsView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us', AboutUsView.as_view(), name='about-us'),
    path('contact-us', ContactUsView.as_view(), name='contact-us'),
    path('our-team', TeamMembersView.as_view(), name='our-team'),
    path('team-member-details/<uuid:pk>', TeamMemberDetailsView.as_view(), name='team-member-details'),
]

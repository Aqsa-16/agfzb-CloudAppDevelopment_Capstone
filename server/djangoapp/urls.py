from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path(route="add_review/<int:dealer_id>", view=views.add_review, name="add_review"),
    path(route="add_review/<int:dealer_id>/", view=views.add_review, name="add_review_slash"),
    path(route="dealer/<int:dealer_id>", view=views.get_dealer_details, name="dealer_details"),
    path(route="dealer/<int:dealer_id>/", view=views.get_dealer_details, name="dealer_details_slash"),
    path(route="", view=views.get_dealerships, name="index"),
    path(route="sentiment_analyzer/<str:text>", view=views.analyze_review, name="sentiment_analyzer"),
    path(route="analyze/<str:text>", view=views.analyze_review, name="analyze_review"),
    path(route="get_cars", view=views.get_cars, name="get_cars"),
    path(route="get_dealers", view=views.get_dealerships, name="get_dealers"),
    path(route="get_dealers/<str:state>", view=views.get_dealerships, name="get_dealers_by_state"),
    path(route="reviews/dealer/<int:dealer_id>", view=views.get_dealer_reviews, name="dealer_reviews"),
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

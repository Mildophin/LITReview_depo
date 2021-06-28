from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.connexion, name='login'),
    path('logout/', views.deconnexion, name='logout'),
    path('feed/', views.feed, name="feed"),
    path('abonnements/', views.abonnements, name="abonnements"),
    path('posts/', views.posts, name="posts"),
    path('create-ticket/', views.create_ticket, name="create_ticket"),
    path('create-review/', views.create_review, name="create_review"),
    path('delete-ticket/<int:id_ticket>', views.deleteticket, name='delete-ticket'),
    path('delete-review/<int:id_review>', views.deletereview, name='delete-review'),
    path('edit-ticket/<int:id_ticket>', views.editticket, name='edit-ticket'),
    path('edit-review/<int:id_review>', views.editreview, name='edit-review'),
    path('remove-follower/<int:id_follower>', views.removefollower, name='remove-follower'),
    path('create-review/<int:id_ticket>', views.answer_review, name='answer-review')
]

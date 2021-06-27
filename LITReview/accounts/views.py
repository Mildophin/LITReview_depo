# accounts/views.py
import traceback
from itertools import chain

from django.db.models import CharField, Value
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Ticket, Review, UserFollows


def connexion(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('feed')
    else:
        return redirect('home')


def deconnexion(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            User.objects.create_user(username=username,password=password)
            return redirect("home")
        else:
            return render(request, "signup.html")
    else:
        return render(request, 'home')


def get_users_viewable_reviews(user):
    followed_users = UserFollows.objects.filter(user=user)
    flo = []
    for fuser in followed_users:
        flo.append(fuser.followed_user)
    viewable_reviews_followed_users = Review.objects.filter(user__in=flo)
    viewable_reviews = Review.objects.filter(user=user)
    final = viewable_reviews_followed_users|viewable_reviews
    return final


def get_users_viewable_tickets(user):
    followed_users = UserFollows.objects.filter(user=user)
    flo = []
    for fuser in followed_users:
        flo.append(fuser.followed_user)
    viewable_tickets_followed_users = Ticket.objects.filter(user__in=flo)
    viewable_tickets = Ticket.objects.filter(user=user)
    ticket_list = []
    final = viewable_tickets_followed_users|viewable_tickets
    return final


def feed(request):
    reviews = get_users_viewable_reviews(request.user)
    review_list = Review.objects.values_list('ticket_id', flat=True)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = get_users_viewable_tickets(request.user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'feed.html', context={'posts': posts, 'review_list': review_list})


def abonnements(request):
    if request.method == "GET":
        user = request.user
        followers = UserFollows.objects.filter(followed_user=user)
        following = UserFollows.objects.filter(user=user)
        return render(request, "abonnements.html", context={'followers': followers, 'following': following})
    else:
        try:
            follow_user = User.objects.get(username=request.POST['follow_user'])
            user = request.user
            UserFollows.objects.create(user=user, followed_user=follow_user)
        except Exception:
            traceback.print_exc()
        return redirect("abonnements")


def posts(request):
    user = request.user
    reviews = Review.objects.filter(user=user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = Ticket.objects.filter(user=user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'posts.html', context={'posts': posts})


def create_ticket(request):
    if request.method == "GET":
        return render(request, "ticket_template.html")
    else:
        titre = request.POST['titre']
        description = request.POST['description']
        user = request.user
        Ticket.objects.create(title=titre,description=description,user=user)
        return redirect("feed")

def create_review(request):
    if request.method == "GET":
        return render(request, "review_template.html")
    else:
        titre = request.POST['titre']
        description = request.POST['description']
        user = request.user
        ticket = Ticket.objects.create(title=titre, description=description, user=user)
        headline = request.POST['headline']
        commentaire = request.POST['commentaire']
        Review.objects.create(headline=headline, ticket=ticket, body=commentaire, rating=rating,user=user)
        return redirect("feed")

def deleteticket(request, id_ticket):
    ticket = get_object_or_404(Ticket, pk=id_ticket)
    ticket.delete()
    return redirect('posts')

def deletereview(request, id_review):
    review = get_object_or_404(Review, pk=id_review)
    review.delete()
    return redirect('posts')

def removefollower(request, id_follower):
    follower = get_object_or_404(UserFollows, pk=id_follower)
    follower.delete()
    return redirect('abonnements')

def editticket(request, id_ticket):
    ticket = Ticket.objects.get(pk=id_ticket)
    if request.user == ticket.user:
        if request.method == "GET":
            return render(request, 'edit-ticket.html', locals())
        elif request.method == "POST":
            titre = request.POST['titre']
            description = request.POST['description']
            my_ticket = Ticket(title=titre,description=description)
            my_ticket.save()
            return redirect('posts')
    else:
        return redirect('home')

def editreview(request, id_review):
    review = Review.objects.get(pk=id_review)
    ticket = review.ticket
    if request.user == review.user:
        if request.method == "GET":
            return render(request, 'edit-review.html', locals())
        elif request.method == "POST":
            titre = request.POST['titre']
            description = request.POST['description']
            my_ticket = Ticket(title=titre,description=description)
            my_ticket.save()
            return redirect('posts')
    else:
        return redirect('home')
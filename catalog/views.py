from django.shortcuts import render

# Create your views here.

from .models import Team, Player


def index(request):
    num_players = Player.objects.all().count()
    num_teams = Team.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_players': num_players, 'num_teams': num_teams, 'num_visits': num_visits},
    )


from django.views import generic


class PlayerListView(generic.ListView):
    model = Player
    paginate_by = 3


class PlayerDetailView(generic.DetailView):
    model = Player


class TeamListView(generic.ListView):
    model = Team
    paginate_by = 3


class TeamDetailView(generic.DetailView):
    model = Team
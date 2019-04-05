from django.shortcuts import render
from submissions.models import Leaderboard
from django.views.generic import ListView
def homePage(request):
    return render(request,'home.html')
class LeaderboardListView(ListView):
    model = Leaderboard
    template_name = 'leaderboard.html'
    queryset = Leaderboard.objects.all().order_by('rank')
    context_object_name = 'coders_list'
    paginate_by = 20

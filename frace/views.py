import uuid
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, render
from core.models import News, TeamMembers

# Create your views here.
class IndexView(View):
    template_name = 'core/index.html'
    model = News
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class AboutUsView(View):
    template_name = 'core/about_us.html'
        
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 

class ContactUsView(View):
    template_name = 'core/contact_us.html'
        
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 
    
    def post(self, request, *args, **kwargs):
        pass

class TeamMembersView(ListView):
    template_name = 'core/our_team.html'
    model = TeamMembers
    paginate_by = 3
    
class TeamMemberDetailsView(DetailView):
    template_name = 'core/team_member_details.html'
    #model   = TeamMembers
    context_object_name = 'team_member'
    queryset = TeamMembers.objects.all()
    
class MemberDetailsView(View):
    template_name = 'core/team_member_details.html'
    context_object_name = 'team_member'
    
    def get(self, request,  id = None, *args, **kwargs):
        context = {}
        if uuid is None:
            obj = get_object_or_404(TeamMembers, uuid = id)
            context['object'] = obj
        return render(request, self.template_name, context)
    
class NewsDetailsView(View):
    template_name = 'core/news_details.html'
    context_object_name = 'news'
    
    def get(self, request,  id = None, *args, **kwargs):
        context = {}
        if uuid is None:
            obj = get_object_or_404(News, uuid = id)
            context['object'] = obj
        return render(request, self.template_name, context)
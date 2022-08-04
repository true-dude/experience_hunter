from django.db.models import Count, Q
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views import View
from core.models import Topic, Category, UserRegistrationForm, Feedback

# Create your views here.


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['location_name', 'description', 'city', 'way', 'img']
    success_url = '/add_place/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

class HunterProfile(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        return render(request, "core/profile.html", context={
            'user': user
        })

    def post(self, request):
        return HttpResponse(12)



def home(request):
    user = request.user
    feedbacks = Feedback.objects.all()
    cities = list(sorted(set([feedback.city for feedback in feedbacks])))
    needed_cities = request.GET.getlist("city") if request.GET.getlist("city") else cities
    feedbacks = feedbacks.filter(city__in=needed_cities)

    q = request.GET.get("q")
    if q is not None:
        feedbacks = feedbacks.filter(Q(city__icontains=q) |
                                     Q(location_name__icontains=q) |
                                     Q(description__icontains=q) |
                                     Q(city__icontains=q) |
                                     Q(way__icontains= q))
    return render(request, "core/home.html", context={
        'user': user,
        'feedbacks': feedbacks,
        'cities': cities,
    })

def index(request):
    topics = Topic.objects.all().annotate(Count('categories'))
    categories = Category.objects.all()

    q = request.GET.get('q')
    if q is not None:
        topics = topics.filter(title__icontains=q)
    category_pk = request.GET.get('category')
    if category_pk is not None:
        topics = topics.filter(categories__pk=category_pk)

    return render(request, "core/index.html", context={
        'topics': topics,
        'categories': categories,
        'some_list': [1, 2, 3, 4, 5, 6]
    })

def topic_details(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        raise Http404
    return render(request, "core/topic-details.html", context={
        'topic': topic
    })


def feedback_details(request, pk):
    try:
        feedback = Feedback.objects.get(pk=pk)
    except Feedback.DoesNotExist:
        raise Http404
    return render(request, "core/feedback_details.html", context={
        'feedback': feedback
    })
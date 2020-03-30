from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView
from .models import tamashii, Dormitory, School
from django.contrib.auth.models import User
from .forms import SearchForm, UpdateForm


def index(request):
    return render(request, 'douapp/index.html')


@method_decorator(login_required, name='dispatch')
class report(CreateView):
    model = tamashii
    template_name = 'douapp/report.html'

    def get_success_url(self):
        return reverse('tamashi', kwargs={'pk': self.object.pk})
    fields = ['name', 'country', 'sex', 'dormitory', 'room', 'evangelist', 'school', 'status']


@method_decorator(login_required, name='dispatch')
class update(UpdateView):
    model = tamashii
    form_class = UpdateForm
    template_name = 'douapp/update.html'

    def get_success_url(self):
        return reverse('tamashi', kwargs={'pk': self.object.pk})


@login_required
def dormitop(request):
    return render(request, 'douapp/dormitop.html')


@login_required
def search(request):
    form = SearchForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            request.session['search_bun'] = request.POST['search_bun']
            request.session['search_type'] = request.POST['type']
            return redirect('list_result')
    return render(request, 'douapp/search.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class owntama(ListView):
    template_name = 'douapp/owntama.html'

    def get_queryset(self):
        return tamashii.objects.filter(evangelist__contains=self.request.user.get_full_name())


@method_decorator(login_required, name='dispatch')
class list_result(ListView):
    template_name = 'douapp/list_result.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_type'] = self.request.session.get('search_type')
        return context

    def get_queryset(self):
        filter_text = self.request.session.get('search_bun')
        search_type = self.request.session.get('search_type')
        if search_type == 'name':
            return tamashii.objects.filter(name__contains=filter_text)
        if search_type == 'dorm':
            return Dormitory.objects.filter(d_name__contains=filter_text)
        if search_type == 'school':
            return School.objects.filter(s_name__contains=filter_text)


@login_required
def p_detail(request, dplace):
    dorm = Dormitory.objects.get(d_name=dplace)
    list = tamashii.objects.filter(dormitory=dplace).order_by('room')
    return render(request, 'douapp/p_detail.html', {'dorm': dorm, "list": list})


@login_required
def place(request, ku):
    list = Dormitory.objects.filter(ku=ku)
    return render(request, 'douapp/place.html', {'dorm_list': list})


@login_required
def tamashi(request, pk):
    tama = tamashii.objects.get(pk=pk)
    return render(request, 'douapp/tamashi.html', {'tama': tama})

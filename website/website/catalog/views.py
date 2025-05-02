from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Component, Category, Report
from .forms import ReportForm


class CategoryDetailView(ListView):
    model = Component
    template_name = 'catalog/category_detail.html'
    context_object_name = 'components'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Component.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class ComponentDetailView(DetailView):
    model = Component
    template_name = 'catalog/detail.html'
    context_object_name = 'component'

class ComponentListView(ListView):
    model = Component
    template_name = 'catalog/index.html'
    context_object_name = 'components'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Component.objects.filter(
                Q(name__icontains=query) |
                Q(manufacturer__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
        return Component.objects.all()


class AboutView(TemplateView):
    template_name = 'catalog/about.html'


@login_required
def report_component(request, component_id):
    component = get_object_or_404(Component, id=component_id)

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.component = component
            report.user = request.user
            report.save()
            return redirect('component-detail', pk=component.id)
    else:
        form = ReportForm()

    return render(request, 'catalog/report_form.html', {'form': form, 'component': component})


@staff_member_required
def report_list(request):
    reports = Report.objects.select_related('component', 'user').order_by('-date_sent')
    return render(request, 'catalog/report_list.html', {'reports': reports})


@staff_member_required
def toggle_report_read(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    report.is_read = not report.is_read
    report.save()
    return redirect('report_list')

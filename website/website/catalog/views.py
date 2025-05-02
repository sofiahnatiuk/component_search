from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from .models import Component, Category, Report
from .forms import ReportForm, ComponentForm, CategoryForm


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

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class ComponentCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Component
    form_class = ComponentForm
    template_name = 'catalog/component_form.html'
    success_url = reverse_lazy('component-list')  # Change to your actual list view name


class ComponentUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Component
    form_class = ComponentForm
    template_name = 'catalog/component_form.html'
    success_url = reverse_lazy('component-list')


class ComponentDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Component
    template_name = 'catalog/component_confirm_delete.html'
    success_url = reverse_lazy('component-list')


class CategoryTreeView(TemplateView):
    template_name = 'catalog/category_tree.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Only top-level categories (those with no parent)
        context['categories'] = Category.objects.filter(parent__isnull=True)
        return context

class CategoryCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('category_tree')


class CategoryUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('category_tree')


class CategoryDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Category
    template_name = 'catalog/category_confirm_delete.html'
    success_url = reverse_lazy('category_tree')

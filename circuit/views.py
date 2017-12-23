from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView

from .forms import CircuitwithDetail, FamilyMemberFormSet, CircuitwithPrisenCharge
from .models import Circuit, HomeDetail, lesinfos


class CirctuiCreate(LoginRequiredMixin,CreateView):
    model = Circuit
    fields = ['Titre','Description','img']
    template_name = 'circtuit/form.html'

    def get_context_data(self, **kwargs):
        context = super(CirctuiCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['bookimage_form'] = CircuitwithDetail(self.request.POST)
            context['familymembers'] = FamilyMemberFormSet(self.request.POST,self.request.FILES)

        else:
            context['bookimage_form'] = CircuitwithDetail()
            context['familymembers'] = FamilyMemberFormSet()

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        bookimage_form = context['bookimage_form']
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()
            if bookimage_form.is_valid() and familymembers.is_valid():
                bookimage_form.instance = self.object
                bookimage_form.save()
                familymembers.instance = self.object
                familymembers.save()
            else:
                return self.render_to_response(self.get_context_data(form=form))
        return super(CirctuiCreate, self).form_valid(form)


class CircuitUpdate(LoginRequiredMixin,UpdateView):
    model = Circuit
    fields = ['Titre','Description','img']
    template_name = 'circtuit/form.html'

    def get_context_data(self, **kwargs):
        context = super(CircuitUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['bookimage_form'] = CircuitwithDetail(self.request.POST,instance=self.object)
            context['familymembers'] = FamilyMemberFormSet(self.request.POST,self.request.FILES, instance=self.object)
        else:
            context['bookimage_form'] = CircuitwithDetail(instance=self.object)
            context['familymembers'] = FamilyMemberFormSet(instance=self.object)
        return context


    def form_valid(self, form):
        context = self.get_context_data()
        bookimage_form = context['bookimage_form']
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()
            if bookimage_form.is_valid() and familymembers.is_valid():
                print("is valid")
                bookimage_form.instance = self.object
                bookimage_form.save()
                familymembers.instance = self.object
                familymembers.save()
        return super(CircuitUpdate, self).form_valid(form)


class Circuitdelete(LoginRequiredMixin,DeleteView):
    model = Circuit
    template_name = 'circtuit/delete.html'
    success_url = reverse_lazy('moulatitcircuit:CircuitList')


class CircuitList(ListView):
    model = Circuit
    template_name = 'circtuit/list.html'
    queryset = Circuit.objects.all().prefetch_related('imageupload_set')



class CircuitDetail(DetailView):
    model = Circuit
    template_name = 'circtuit/detail.html'





class HomeInfo(LoginRequiredMixin,CreateView):
    model = HomeDetail
    template_name = 'circtuit/myform.html'
    fields = ['logo', 'facebook','Instagram','Email','Fax','Mobile','Adress','img_1','description1','img_2','description2','img_3','description3','histoire']
    success_url = ('.')


class HomeUpdate(LoginRequiredMixin,UpdateView):
    model = HomeDetail
    template_name = 'circtuit/myform.html'
    fields = ['logo', 'facebook','Instagram','Email','Fax','Mobile','Adress','img_1','description1','img_2','description2','img_3','description3','histoire']
    success_url = ('.')

class Prisencharge(LoginRequiredMixin,CreateView):
    model = lesinfos
    fields = ['titre',]
    template_name = 'circtuit/myform.html'
    success_url = reverse_lazy('moulatitcircuit:PrisenchargeList')

    def get_context_data(self, **kwargs):
        context = super(Prisencharge, self).get_context_data(**kwargs)
        if self.request.POST:
            context['bookimage_form'] = CircuitwithPrisenCharge(self.request.POST)

        else:
            context['bookimage_form'] = CircuitwithPrisenCharge()

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        bookimage_form = context['bookimage_form']
        with transaction.atomic():
            self.object = form.save()
            if bookimage_form.is_valid() :
                bookimage_form.instance = self.object
                bookimage_form.save()
            else:
                return self.render_to_response(self.get_context_data(form=form))
        return super(Prisencharge, self).form_valid(form)


class PrisenchargeUpdate(LoginRequiredMixin,UpdateView):
    model = lesinfos
    fields = ['titre',]
    template_name = 'circtuit/myform.html'
    success_url = reverse_lazy('moulatitcircuit:PrisenchargeList')

    def get_context_data(self, **kwargs):
        context = super(PrisenchargeUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['bookimage_form'] = CircuitwithPrisenCharge(self.request.POST,instance=self.object)
        else:
            context['bookimage_form'] = CircuitwithPrisenCharge(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        bookimage_form = context['bookimage_form']

        with transaction.atomic():
            self.object = form.save()
            if bookimage_form.is_valid():
                print("is valid")
                bookimage_form.instance = self.object
                bookimage_form.save()

        return super(PrisenchargeUpdate, self).form_valid(form)

class PrisenchargeList(ListView):
    model = lesinfos
    template_name = 'circtuit/lesinfos.html'

class PrisenchargeDeleteView(LoginRequiredMixin,DeleteView):
    model = lesinfos
    template_name = 'circtuit/delete.html'
    success_url = reverse_lazy('moulatitcircuit:PrisenchargeList')

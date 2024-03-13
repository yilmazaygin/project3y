from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.views import View

from quote_app.models import Quotes
import os

# Create your views here
class GenericQuoteView(View):
    model = Quotes("quotes.json")
    def get(self, request):
        quote_n_header = self.model.get_random_quote()
        request.session['answer'] = quote_n_header[0]
        ctx = {
            'keys': self.model.get_all_keys(),
            'quote': quote_n_header[1],
        }
        return render(request, 'quote_app/index.html', ctx)

    def post(self, request):
        answer = request.session['answer']
        print(request.POST.get('reply'))
        if  answer is not None and request.POST.get('reply') == answer:
            messages.success(request, 'win')
        else:
            messages.error(request, "lose")
        return redirect('holybook')
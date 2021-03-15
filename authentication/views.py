from django.shortcuts import render
from django.views.generic import View


class SignUp(View):
    template_name = ''

    def get(self, request, *args, **kwargs):
        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        pass

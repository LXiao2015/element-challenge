from django.shortcuts import render

def get_result(request):
    context = {}
    context['res_str'] = 'Hello World!'
    return render(request, 'page.html', context)

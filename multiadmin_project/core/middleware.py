from django.http import HttpResponseRedirect

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            # Перенаправляем пользователей в соответствующую админку
            if request.path.startswith('/admin/'):
                if request.user.groups.filter(name='Editors').exists():
                    return HttpResponseRedirect('/editor/')
                elif request.user.groups.filter(name='Publishers').exists():
                    return HttpResponseRedirect('/publisher/')
                elif request.user.groups.filter(name='Archivists').exists():
                    return HttpResponseRedirect('/archive/')
        return None
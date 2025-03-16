import importlib

from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import resolve, Resolver404
from django.http import HttpResponseForbidden
from modules.models import Module
 
def is_block_url(request):
    urls_blocked = []
    # Look for modules with 'uninstalled' status and block their URLs.
    for m in Module.objects.filter(status='uninstalled'):
        try:
            urls = importlib.import_module(f"{m.name}.urls")
            for u in urls.urlpatterns: 
                if hasattr(u, 'url_patterns'):  # Check if this is include()
                    for up in u.url_patterns:
                        if up not in urls_blocked:
                            urls_blocked.append(up)
                else:  # If this is a regular URLPattern
                    if u not in self.urls_blocked:
                        urls_blocked.append(u)
                        
            if urls_blocked: urls_blocked.append('')
    
        except ImportError:
            # if module not found, skip
            continue
            
    # Resolve the requested URL
    try:
        resolved_url = resolve(request.path_info)
    except Resolver404:
        # If URL is not found, proceed to the next middleware.
        return get_response(request)
        
    # Check if the requested URL is blocked
    for blocked_url in urls_blocked:
        # Compare the URL name of resolved_url with blocked_url
        if resolved_url.url_name == getattr(blocked_url, 'name', None):
            # If URL is blocked, return a 403 Forbidden response.
            return HttpResponseForbidden("This module has been Unistalled")

    return None

class AnonymousMixin(UserPassesTestMixin):
    def test_func(self): 
        return True
    
    def dispatch(self, request, *args, **kwargs):
        # Call the is_block_url function to check if a URL is blocked.
        blocked_response = is_block_url(request)
        if blocked_response:
            return blocked_response

        # Lproceed to user permission check
        return super().dispatch(request, *args, **kwargs)


class AdminMixin(UserPassesTestMixin):
    def test_func(self): 
        typed = False
        try:
        	typed = self.request.user.type == '001'
        	
        except:
        	pass
        	
        return typed

    def handle_no_permission(self):
        return HttpResponseForbidden("You don't have permission to access this page.")
        
    def dispatch(self, request, *args, **kwargs):
        # Call the is_block_url function to check if a URL is blocked.
        blocked_response = is_block_url(request)
        if blocked_response:
            return blocked_response

        # Lproceed to user permission check
        return super().dispatch(request, *args, **kwargs)


class ManagerMixin(UserPassesTestMixin):
    def test_func(self):
        typed = False
        try:
        	typed = self.request.user.type in ('001', '002')
        except:
        	pass
        	
        return typed

    def handle_no_permission(self):
        return HttpResponseForbidden("You don't have permission to access this page.")
        
    def dispatch(self, request, *args, **kwargs):
        # Call the is_block_url function to check if a URL is blocked.
        blocked_response = is_block_url(request)
        if blocked_response:
            return blocked_response

        # Lproceed to user permission check
        return super().dispatch(request, *args, **kwargs)

class MemberMixin(UserPassesTestMixin):
    def test_func(self):
        # This for handling Anonymouse User
        typed = False
        try:
        	typed = self.request.user.type in ('001', '002', '003')
        except:
        	pass
        	
        return typed

    def handle_no_permission(self):
        return HttpResponseForbidden("You don't have permission to access this page.")
        
    def dispatch(self, request, *args, **kwargs):
        # Call the is_block_url function to check if a URL is blocked.
        blocked_response = is_block_url(request)
        if blocked_response:
            return blocked_response

        # Lproceed to user permission check
        return super().dispatch(request, *args, **kwargs)
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden

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
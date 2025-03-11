from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

class AdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.type == '001'

class ManagerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.type in ('001', '002')

class MemberMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.type in ('001', '002', '003')
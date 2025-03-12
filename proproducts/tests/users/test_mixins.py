from django.test import TestCase, RequestFactory
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from users.mixins import AdminMixin, ManagerMixin, MemberMixin

User = get_user_model()

# Kelas dummy untuk testing
class DummyView(View):
    def dispatch(self, request, *args, **kwargs):
        # self.request sudah diatur oleh Django
        return HttpResponse("Success")

# View yang menggunakan mixins
class AdminView(AdminMixin, DummyView):
    pass

class ManagerView(ManagerMixin, DummyView):
    pass

class MemberView(MemberMixin, DummyView):
    pass

class MixinsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
        # Buat pengguna dengan tipe berbeda
        self.admin_user = User.objects.create_user(
            username='admin',
            password='adminpassword',
            type='001',  # Admin
            name='Admin User',
            email='admin@example.com',
            gender='m'
        )
        self.manager_user = User.objects.create_user(
            username='manager',
            password='managerpassword',
            type='002',  # Manager
            name='Manager User',
            email='manager@example.com',
            gender='f'
        )
        self.member_user = User.objects.create_user(
            username='member',
            password='memberpassword',
            type='003',  # Member
            name='Member User',
            email='member@example.com',
            gender='m'
        )

    def test_admin_mixin_with_admin_user(self):
        # Admin dapat mengakses view
        request = self.factory.get('/')
        request.user = self.admin_user  # Atur user pada request
        view = AdminView.as_view()  # Buat callable view
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")

    def test_admin_mixin_with_non_admin_user(self):
        # Manager tidak dapat mengakses view
        request = self.factory.get('/')
        request.user = self.manager_user  # Atur user pada request
        view = AdminView.as_view()  # Buat callable view
        with self.assertRaises(PermissionDenied):
            view(request)

        # Member tidak dapat mengakses view
        request.user = self.member_user  # Atur user pada request
        with self.assertRaises(PermissionDenied):
            view(request)

    def test_manager_mixin_with_manager_user(self):
        # Manager dapat mengakses view
        request = self.factory.get('/')
        request.user = self.manager_user  # Atur user pada request
        view = ManagerView.as_view()  # Buat callable view
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")

    def test_manager_mixin_with_non_manager_user(self):
        # Admin dapat mengakses view (karena admin termasuk dalam manager)
        request = self.factory.get('/')
        request.user = self.admin_user  # Atur user pada request
        view = ManagerView.as_view()  # Buat callable view
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")

        # Member tidak dapat mengakses view
        request.user = self.member_user  # Atur user pada request
        with self.assertRaises(PermissionDenied):
            view(request)

    def test_member_mixin_with_member_user(self):
        # Member dapat mengakses view
        request = self.factory.get('/')
        request.user = self.member_user  # Atur user pada request
        view = MemberView.as_view()  # Buat callable view
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")

    def test_member_mixin_with_non_member_user(self):
        # Admin dapat mengakses view (karena admin termasuk dalam member)
        request = self.factory.get('/')
        request.user = self.admin_user  # Atur user pada request
        view = MemberView.as_view()  # Buat callable view
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")

        # Manager dapat mengakses view (karena manager termasuk dalam member)
        request.user = self.manager_user  # Atur user pada request
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")
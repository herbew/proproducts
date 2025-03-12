from django.test import TestCase, RequestFactory, override_settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from users.mixins import AdminMixin, ManagerMixin, MemberMixin

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})

User = get_user_model()

# View dummy for testing mixins
class DummyView:
    def dispatch(self, request, *args, **kwargs):
        return HttpResponse("Success")

# View who uses mixins
class AdminView(AdminMixin, DummyView):
    pass

class ManagerView(ManagerMixin, DummyView):
    pass

class MemberView(MemberMixin, DummyView):
    pass

class MixinsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
        # Create users with different types
        self.admin_user = User.objects.create_superuser(
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
        # Admin can access view
        request = self.factory.get('/')
        request.user = self.admin_user
        view = AdminView()
        response = view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")
	
	def test_admin_mixin_with_non_admin_user(self):
        # Manager cannot access the view
        request = self.factory.get('/')
        request.user = self.manager_user
        view = AdminView()
        with self.assertRaises(PermissionDenied):
            view.dispatch(request)

        # Members cannot access the view
        request.user = self.member_user
        with self.assertRaises(PermissionDenied):
            view.dispatch(request)

    def test_manager_mixin_with_manager_user(self):
        # Manager can access the view
        request = self.factory.get('/')
        request.user = self.manager_user
        view = ManagerView()
        response = view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")

    def test_manager_mixin_with_non_manager_user(self):
        # Admin can access the view (because admin is included in the manager)
        request = self.factory.get('/')
        request.user = self.admin_user
        view = ManagerView()
        response = view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")

        # Members cannot access the view
        request.user = self.member_user
        with self.assertRaises(PermissionDenied):
            view.dispatch(request)
            
    def test_member_mixin_with_member_user(self):
        # Members can access the view
        request = self.factory.get('/')
        request.user = self.member_user
        view = MemberView()
        response = view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")

    def test_member_mixin_with_non_member_user(self):
        # Admin can access the view (because admin is a member)
        request = self.factory.get('/')
        request.user = self.admin_user
        view = MemberView()
        response = view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")

        # Managers can access the view (because managers are members)
        request.user = self.manager_user
        response = view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Success")
        
        

        
        
        
        
        
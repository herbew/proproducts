from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})

class UsersModelTest(TestCase):
    def test_create_user(self):
        # Create a new user
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            name='Test User',
            email='testuser@example.com',
            type='003',  # Member
            gender='m'   # Male
        )
        
        # Check if the user was created successfully
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.type, '003')
        self.assertEqual(user.gender, 'm')
        self.assertTrue(user.check_password('testpassword123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        # Create a new superuser
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username='admin',
            password='adminpassword123',
            name='Admin User',
            email='admin@example.com',
            type='001',  # Admin
            gender='f'   # Female
        )
        
        # Check if superuser was successfully created
        self.assertEqual(superuser.username, 'admin')
        self.assertEqual(superuser.name, 'Admin User')
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertEqual(superuser.type, '001')
        self.assertEqual(superuser.gender, 'f')
        self.assertTrue(superuser.check_password('adminpassword123'))
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_user_type_choices(self):
        # Check the options for the `type` field
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            name='Test User',
            email='testuser@example.com',
            type='003',  # Member
            gender='m'   # Male
        )
        
        # Checking valid options
        valid_types = ['001', '002', '003']
        self.assertIn(user.type, valid_types)
        
        # Checks for invalid choices
        with self.assertRaises(ValidationError):
            user.type = '004'  # Invalid type
            user.full_clean()  # Trigger validation

    def test_user_gender_choices(self):
        # Checking choices for the `gender` field
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            name='Test User',
            email='testuser@example.com',
            type='003',  # Member
            gender='m'   # Male
        )
        
        # Checking valid options
        valid_genders = ['m', 'f']
        self.assertIn(user.gender, valid_genders)
        
        # Checks for invalid choices
        with self.assertRaises(ValidationError):
            user.gender = 'x'  # Gender is invalid
            user.full_clean()  # Trigger validation

    def test_user_str_representation(self):
        # Create a new user
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            name='Test User',
            email='testuser@example.com',
            type='003',  # Member
            gender='m'   # Male
        )
        
        # Checking the string representation of the user
        self.assertEqual(str(user), 'testuser')
        
        
        
        
        
        
        
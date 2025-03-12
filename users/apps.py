from django.apps import AppConfig

class UsersConfig(AppConfig):
    # Default application name (must match the application folder name)
    name = 'users'
    
    # Application label (optional, used for reference in admin or elsewhere)
    label = 'users'
    
    # More readable name (optional, used in Django admin)
    verbose_name = 'Users Management'
    
    # Method executed when the application is ready (optional)
    def ready(self):
        # Import signal handlers or other code that needs to be run when the application is ready.
        import users.signals  # Example: If you use signals
        
        
        
        
        
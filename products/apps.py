from django.apps import AppConfig

class ProductsConfig(AppConfig):
    # Default application name (must match the application folder name)
    name = 'products'
    
    # Application label (optional, used for reference in admin or elsewhere)
    label = 'products'
    
    # More readable name (optional, used in Django admin)
    verbose_name = 'Products Management'
    
    # Method executed when the application is ready (optional)
    def ready(self):
        # Import signal handlers or other code that needs to be run when the application is ready.
        import products.signals  # Example: If you use signals
        
        
        
        
        
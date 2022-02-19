from django.apps import AppConfig
from watson import search as watson

class TicketsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tickets'
    def ready(self):
        category_model = self.get_model("Category")
        watson.register(category_model)
        ticket_model = self.get_model("Ticket")
        watson.register(ticket_model)
        package_model = self.get_model("Package")
        watson.register(package_model)
        actor_model = self.get_model("Actor")
        watson.register(actor_model)

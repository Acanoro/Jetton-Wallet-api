from django.contrib import admin

from admin_dashboard.models import AdminDashboardModel


# Register your models here.
class AdminDashboardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'total_users', 'active_users', 'total_referrals', 'total_tasks_completed', 'total_emission',)


models_and_admins = [
    (AdminDashboardModel, AdminDashboardAdmin),
]

for model, admin_class in models_and_admins:
    admin.site.register(model, admin_class)

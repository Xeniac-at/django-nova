"""
Admin tools for django-nova models
"""

from django.contrib import admin

from nova.models import EmailAddress, Newsletter, NewsletterIssue, Subscription

def send_newsletter_issue(modeladmin, request, queryset):
    for issue in queryset:
        issue.send()

send_newsletter_issue.short_description = "Send to newsletter subscribers"

def send_test_newsletter_issue(modeladmin, request, queryset):
    for issue in queryset:
        issue.send_test()

send_test_newsletter_issue.short_description = "Send to newsletter approvers"

class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ('email', 'token', 'client_addr', 'confirmed', 'confirmed_at', 'created_at',)
    readonly_fields = ('created_at',)
    list_filter = ('confirmed',)
    search_fields = ['email', 'client_addr',]

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'newsletter', 'created_at', 'active',)
    readonly_fields = ('created_at',)
    list_filter = ('newsletter', 'active',)
    search_fields = ['email_address__email',]

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created_at', 'approvers',)    
    readonly_fields = ('created_at',)
    list_filter = ('active',)

class NewsletterIssueAdmin(admin.ModelAdmin):
    list_display = ('subject', 'newsletter', 'sent_at','created_at',)
    list_filter = ('newsletter',)
    search_fields = ['subject',]
    readonly_fields = ('rendered_template', 'sent_at',)

    actions = [send_newsletter_issue,send_test_newsletter_issue]

admin.site.register(EmailAddress, EmailAddressAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(NewsletterIssue, NewsletterIssueAdmin)
admin.site.register(Subscription, SubscriptionAdmin)

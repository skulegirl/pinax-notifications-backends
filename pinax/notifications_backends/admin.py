from django.contrib import admin

from pinax.notifications_backends.models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = [
        "message", "recipient", "sender", "medium", "notice_type", "added",
        "unseen", "exception"]
    list_filter = ["medium", "notice_type", "added"]
    raw_id_fields = ["recipient", "sender"]
    readonly_fields = ["medium", "exception"]
    search_fields = (
        "recipient__username",
        "recipient__email",
    )


admin.site.register(Notice, NoticeAdmin)

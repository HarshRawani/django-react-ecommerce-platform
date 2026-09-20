from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
    User,
    UserShippingAddress,
    Modules,
    UserPermissions,
    ActivityLog,
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "name",
        "phone",
        "role",
        "account_status",
        "domain_name",
        "plan_type",
        "is_active",
        "is_staff",
        "is_superuser",   # added
        "created_at",
    )

    list_display_links = ("id", "username")

    list_filter = (
        "role",
        "account_status",
        "plan_type",
        "departMent",
        "language",
        "country",
        "currency",
        "is_active",
        "is_staff",
        "is_superuser",
        "created_at",
    )

    search_fields = (
        "username",
        "email",
        "name",
        "phone",
        "domain_name",
        "city",
        "state",
        "pincode",
    )

    autocomplete_fields = (
        "domain_user_id",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "last_login",
        "date_joined",
    )

    ordering = ("-created_at",)

    fieldsets = (
        ("Login Information", {
            "fields": (
                "username",
                "password",
            )
        }),
        ("Personal Information", {
            "fields": (
                "name",
                "email",
                "phone",
                "profile_pic",
                "dob",
            )
        }),
        ("Address", {
            "fields": (
                "address",
                "city",
                "state",
                "pincode",
                "country",
            )
        }),
        ("Organization", {
            "fields": (
                "role",
                "departMent",
                "designation",
                "domain_user_id",
                "domain_name",
                "plan_type",
            )
        }),
        ("Preferences", {
            "fields": (
                "language",
                "time_zone",
                "currency",
            )
        }),
        ("Account Status", {
            "fields": (
                "account_status",
                "is_active",
                "is_staff",
                "is_superuser",
            )
        }),
        ("Security / Device", {
            "fields": (
                "last_device",
                "last_ip",
            )
        }),
        ("Additional Information", {
            "fields": (
                "social_media_links",
                "addition_details",
            )
        }),
        ("Permissions", {
            "fields": (
                "groups",
                "user_permissions",
            )
        }),
        ("Dates", {
            "fields": (
                "last_login",
                "date_joined",
                "created_at",
                "updated_at",
            )
        }),
    )


@admin.register(UserShippingAddress)
class UserShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "address_type",
        "city",
        "state",
        "pincode",
        "country",
        "created_at",
    )

    list_display_links = ("id", "user")

    list_filter = (
        "address_type",
        "country",
        "state",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "user__name",
        "address",
        "city",
        "state",
        "pincode",
    )

    autocomplete_fields = (
        "user",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "module_name",
        "parent_id",
        "is_menu",
        "is_active",
        "display_order",
        "module_url",
        "created_at",
    )

    list_display_links = ("id", "module_name")

    list_filter = (
        "is_menu",
        "is_active",
        "created_at",
    )

    search_fields = (
        "module_name",
        "module_description",
        "module_url",
    )

    autocomplete_fields = (
        "parent_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = (
        "display_order",
        "module_name",
    )


@admin.register(UserPermissions)
class UserPermissionsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "module",
        "is_view",
        "is_add",
        "is_edit",
        "is_delete",
        "domain_user_id",
        "created_at",
    )

    list_display_links = ("id", "user")

    list_filter = (
        "is_view",
        "is_add",
        "is_edit",
        "is_delete",
        "module",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "user__name",
        "module__module_name",
        "domain_user_id__username",
        "domain_user_id__email",
    )

    autocomplete_fields = (
        "user",
        "module",
        "domain_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "activity_type",
        "activity",
        "activity_date",
        "activity_ip",
        "activity_device",
        "domain_user_id",
    )

    list_display_links = ("id", "user")

    list_filter = (
        "activity_type",
        "activity_device",
        "activity_date",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "user__name",
        "activity",
        "activity_type",
        "activity_ip",
        "activity_device",
        "domain_user_id__username",
    )

    autocomplete_fields = (
        "user",
        "domain_user_id",
    )

    readonly_fields = (
        "id",
        "activity_date",
        "created_at",
        "updated_at",
    )

    ordering = ("-activity_date",)
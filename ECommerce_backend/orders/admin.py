from django.contrib import admin

from .models import (
    PurchaseOrder,
    PurchaseOrderItems,
    PurchaseOrderInwardedLog,
    PurchaseOrderItemInwardedLog,
    PurchaseOrderLogs,
    SalesOrder,
    SalesOrderOrderItems,
    SalesOrderOutWardedLog,
    SalesOrderItemOutwardedLog,
    SalesOrderLogs,
)


# =========================================================
# Purchase Order
# =========================================================

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "po_code",
        "po_date",
        "supplier_id",
        "warehouse_id",
        "total_amount",
        "paid_amount",
        "due_amount",
        "payment_status",
        "status",
        "expected_delivery_date",
        "created_at",
    )

    list_display_links = ("id", "po_code")

    list_filter = (
        "status",
        "payment_status",
        "payment_terms",
        "shipping_type",
        "discount_type",
        "created_at",
        "po_date",
    )

    search_fields = (
        "po_code",
        "supplier_id__username",
        "supplier_id__email",
        "domain_user_id__username",
    )

    autocomplete_fields = (
        "warehouse_id",
        "supplier_id",
        "last_updated_by_user_id",
        "created_by_user_id",
        "updated_by_user_id",
        "domain_user_id",
        "approved_by_user_id",
        "cancelled_by_user_id",
        "received_by_user_id",
        "returned_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# =========================================================
# Purchase Order Items
# =========================================================

@admin.register(PurchaseOrderItems)
class PurchaseOrderItemsAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "po_id",
        "product_id",
        "quantity_ordered",
        "quantity_received",
        "quantity_cancelled",
        "quantity_returned",
        "buying_price",
        "amount_ordered",
        "status",
        "created_at",
    )

    list_display_links = ("id",)

    list_filter = (
        "status",
        "discount_type",
        "created_at",
    )

    search_fields = (
        "po_id__po_code",
        "product_id__name",
        "product_id__sku",
    )

    autocomplete_fields = (
        "po_id",
        "product_id",
        "created_by_user_id",
        "updated_by_user_id",
        "domain_user_id",
        "approved_by_user_id",
        "cancelled_by_user_id",
        "received_by_user_id",
        "returned_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# =========================================================
# Purchase Order Inwarded Log
# =========================================================

@admin.register(PurchaseOrderInwardedLog)
class PurchaseOrderInwardedLogAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "po_id",
        "invoice_number",
        "inwarded_by_user_id",
        "inwarded_at",
        "status",
        "created_at",
    )

    list_display_links = ("id", "invoice_number")

    list_filter = (
        "status",
        "inwarded_at",
        "created_at",
    )

    search_fields = (
        "invoice_number",
        "po_id__po_code",
        "notes",
        "inwarded_by_user_id__username",
        "inwarded_by_user_id__email",
    )

    autocomplete_fields = (
        "po_id",
        "inwarded_by_user_id",
        "domain_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-inwarded_at",)


# =========================================================
# Purchase Order Item Inwarded Log
# =========================================================

@admin.register(PurchaseOrderItemInwardedLog)
class PurchaseOrderItemInwardedLogAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "po_item_id",
        "inwarded_quantity",
        "price",
        "tax_percentage",
        "discount_amount",
        "shipping_amount",
        "status",
        "created_at",
    )

    list_display_links = ("id",)

    list_filter = (
        "status",
        "discount_type",
        "created_at",
    )

    search_fields = (
        "po_item_id__po_id__po_code",
        "po_item_id__product_id__name",
        "po_item_id__product_id__sku",
    )

    autocomplete_fields = (
        "po_item_id",
        "domain_user_id",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# =========================================================
# Purchase Order Logs
# =========================================================

@admin.register(PurchaseOrderLogs)
class PurchaseOrderLogsAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "po_id",
        "comment",
        "created_by_user_id",
        "domain_user_id",
        "created_at",
    )

    list_display_links = ("id", "po_id")

    list_filter = (
        "created_at",
    )

    search_fields = (
        "po_id__po_code",
        "comment",
        "created_by_user_id__username",
        "created_by_user_id__email",
    )

    autocomplete_fields = (
        "po_id",
        "created_by_user_id",
        "domain_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# =========================================================
# Sales Order
# =========================================================

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "so_code",
        "so_date",
        "customer_id",
        "total_amount",
        "paid_amount",
        "due_amount",
        "payment_status",
        "status",
        "expected_delivery_date",
        "created_at",
    )

    list_display_links = ("id", "so_code")

    list_filter = (
        "status",
        "payment_status",
        "payment_terms",
        "shipping_type",
        "discount_type",
        "created_at",
        "so_date",
    )

    search_fields = (
        "so_code",
        "customer_id__username",
        "customer_id__email",
        "domain_user_id__username",
    )

    autocomplete_fields = (
        "customer_id",
        "last_updated_by_user_id",
        "created_by_user_id",
        "updated_by_user_id",
        "domain_user_id",
        "approved_by_user_id",
        "cancelled_by_user_id",
        "received_by_user_id",
        "returned_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# =========================================================
# Sales Order Items
# =========================================================

@admin.register(SalesOrderOrderItems)
class SalesOrderOrderItemsAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "so_id",
        "product_id",
        "quantity_ordered",
        "quantity_delivered",
        "quantity_shipped",
        "quantity_cancelled",
        "quantity_returned",
        "purchase_price",
        "amount_ordered",
        "status",
        "created_at",
    )

    list_display_links = ("id",)

    list_filter = (
        "status",
        "discount_type",
        "created_at",
    )

    search_fields = (
        "so_id__so_code",
        "product_id__name",
        "product_id__sku",
    )

    autocomplete_fields = (
        "so_id",
        "product_id",
        "created_by_user_id",
        "updated_by_user_id",
        "domain_user_id",
        "approved_by_user_id",
        "cancelled_by_user_id",
        "shipped_by_user_id",
        "returned_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# =========================================================
# Sales Order Outwarded Log
# =========================================================

@admin.register(SalesOrderOutWardedLog)
class SalesOrderOutWardedLogAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "so_id",
        "invoice_number",
        "outwarded_by_user_id",
        "outwared_at",
        "status",
        "created_at",
    )

    list_display_links = ("id", "invoice_number")

    list_filter = (
        "status",
        "outwared_at",
        "created_at",
    )

    search_fields = (
        "invoice_number",
        "so_id__so_code",
        "notes",
        "outwarded_by_user_id__username",
        "outwarded_by_user_id__email",
    )

    autocomplete_fields = (
        "so_id",
        "outwarded_by_user_id",
        "domain_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-outwared_at",)


# =========================================================
# Sales Order Item Outwarded Log
# =========================================================

@admin.register(SalesOrderItemOutwardedLog)
class SalesOrderItemOutwardedLogAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "so_item_id",
        "outwarded_quantity",
        "price",
        "tax_percentage",
        "discount_amount",
        "shipping_amount",
        "status",
        "created_at",
    )

    list_display_links = ("id",)

    list_filter = (
        "status",
        "discount_type",
        "created_at",
    )

    search_fields = (
        "so_item_id__so_id__so_code",
        "so_item_id__product_id__name",
        "so_item_id__product_id__sku",
    )

    autocomplete_fields = (
        "so_item_id",
        "domain_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# =========================================================
# Sales Order Logs
# =========================================================

@admin.register(SalesOrderLogs)
class SalesOrderLogsAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "so_id",
        "comment",
        "created_by_user_id",
        "domain_user_id",
        "created_at",
    )

    list_display_links = ("id", "so_id")

    list_filter = (
        "created_at",
    )

    search_fields = (
        "so_id__so_code",
        "comment",
        "created_by_user_id__username",
        "created_by_user_id__email",
    )

    autocomplete_fields = (
        "so_id",
        "created_by_user_id",
        "domain_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)
from django.contrib import admin

from .models import (
    Warehouse,
    RackAndShelvesAndFloor,
    Inventory,
    InventoryLog,
)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "city",
        "state",
        "warehouse_manager",
        "phone",
        "email",
        "status",
        "size",
        "capacity",
        "warehouse_type",
        "created_at",
    )
    list_display_links = ("id", "name")

    list_filter = (
        "status",
        "size",
        "capacity",
        "warehouse_type",
        "city",
        "state",
        "created_at",
    )

    search_fields = (
        "name",
        "address",
        "city",
        "state",
        "country",
        "pincode",
        "phone",
        "email",
        "warehouse_manager__username",
        "warehouse_manager__email",
    )

    autocomplete_fields = (
        "warehouse_manager",
        "domain_user_id",
        "added_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


@admin.register(RackAndShelvesAndFloor)
class RackAndShelvesAndFloorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "warehouse_id",
        "rack",
        "shelf",
        "floor",
        "created_at",
    )

    list_display_links = ("id", "name")

    list_filter = (
        "warehouse_id",
        "created_at",
    )

    search_fields = (
        "name",
        "rack",
        "shelf",
        "floor",
        "warehouse_id__name",
        "warehouse_id__city",
    )

    autocomplete_fields = (
        "warehouse_id",
        "domain_user_id",
        "added_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_id",
        "warehouse_id",
        "rack_shelf_floor_id",
        "quantity",
        "quantity_inwarded",
        "buy_price",
        "sell_price",
        "tax_percentage",
        "stock_status",
        "inward_type",
        "batch_number",
        "expiry_date",
        "created_at",
    )

    list_display_links = ("id", "product_id")

    list_filter = (
        "stock_status",
        "inward_type",
        "discount_type",
        "uom",
        "warehouse_id",
        "created_at",
        "received_date",
        "expiry_date",
    )

    search_fields = (
        "product_id__name",
        "product_id__sku",
        "warehouse_id__name",
        "warehouse_id__city",
        "rack_shelf_floor_id__name",
        "rack_shelf_floor_id__rack",
        "rack_shelf_floor_id__shelf",
        "batch_number",
        "sr_no",
    )

    autocomplete_fields = (
        "purchase_order_id",
        "purchase_order_item_id",
        "purchase_order_item_inwarded_item_id",
        "product_id",
        "warehouse_id",
        "rack_shelf_floor_id",
        "domain_user_id",
        "added_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


@admin.register(InventoryLog)
class InventoryLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "inventory_id",
        "po_id",
        "so_id",
        "warehouse_id",
        "rack_shelf_floor_id",
        "quantity",
        "status",
        "created_at",
    )

    list_display_links = ("id", "inventory_id")

    list_filter = (
        "status",
        "warehouse_id",
        "created_at",
    )

    search_fields = (
        "inventory_id__product_id__name",
        "inventory_id__product_id__sku",
        "po_id__po_code",
        "so_id__so_code",
        "warehouse_id__name",
        "warehouse_id__city",
        "rack_shelf_floor_id__name",
    )

    autocomplete_fields = (
        "po_id",
        "so_id",
        "inventory_id",
        "warehouse_id",
        "rack_shelf_floor_id",
        "domain_user_id",
        "added_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)
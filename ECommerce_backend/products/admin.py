from django.contrib import admin

from .models import (
    Categories,
    Product,
    ProductQuestions,
    ProductReviews,
)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "parent_id",
        "domain_user_id",
        "added_by_user_id",
        "display_order",
        "created_at",
        "updated_at",
    )

    list_display_links = ("id", "name")

    list_filter = (
        "parent_id",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "description",
        "domain_user_id__username",
        "added_by_user_id__username",
    )

    autocomplete_fields = (
        "parent_id",
        "domain_user_id",
        "added_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("display_order", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "sku",
        "brand",
        "category_id",
        "initial_selling_price",
        "status",
        "domain_user_id",
        "added_by_user_id",
        "created_at",
    )

    list_display_links = ("id", "name")

    list_filter = (
        "status",
        "brand",
        "category_id",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "sku",
        "brand",
        "brand_model",
        "description",
        "seo_title",
        "category_id__name",
        "domain_user_id__username",
        "added_by_user_id__username",
    )

    autocomplete_fields = (
        "category_id",
        "domain_user_id",
        "added_by_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


@admin.register(ProductQuestions)
class ProductQuestionsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_id",
        "question",
        "answer",
        "status",
        "question_user_id",
        "answer_user_id",
        "created_at",
    )

    list_display_links = ("id", "product_id")

    list_filter = (
        "status",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "question",
        "answer",
        "product_id__name",
        "product_id__sku",
        "question_user_id__username",
        "answer_user_id__username",
    )

    autocomplete_fields = (
        "product_id",
        "domain_user_id",
        "question_user_id",
        "answer_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


@admin.register(ProductReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_id",
        "rating",
        "status",
        "review_user_id",
        "created_at",
    )

    list_display_links = ("id", "product_id")

    list_filter = (
        "status",
        "rating",
        "created_at",
    )

    search_fields = (
        "reviews",
        "product_id__name",
        "product_id__sku",
        "review_user_id__username",
    )

    autocomplete_fields = (
        "product_id",
        "domain_user_id",
        "review_user_id",
    )

    readonly_fields = (
        "id",
        "created_at",
    )

    ordering = ("-created_at",)
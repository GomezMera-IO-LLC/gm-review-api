"""Platform-wide constants, enums, and role definitions."""

from __future__ import annotations

from enum import StrEnum


class SubscriptionTier(StrEnum):
    """Organization subscription tiers."""

    STARTER = "starter"
    SMALL_BUSINESS = "small_business"
    GROWTH = "growth"
    BUSINESS = "business"
    ENTERPRISE = "enterprise"


class OrgStatus(StrEnum):
    """Organization lifecycle statuses."""

    ACTIVE = "active"
    SUSPENDED = "suspended"
    PENDING_DELETION = "pending_deletion"


class KeyType(StrEnum):
    """API key types."""

    PRIVATE = "private"
    PUBLIC = "public"


class KeyStatus(StrEnum):
    """API key statuses."""

    ACTIVE = "active"
    ROTATING = "rotating"
    REVOKED = "revoked"


class ProductStatus(StrEnum):
    """Product lifecycle statuses."""

    ACTIVE = "active"
    DELETED = "deleted"


class ReviewStatus(StrEnum):
    """Review moderation statuses."""

    PENDING = "pending"
    PENDING_MANUAL_REVIEW = "pending_manual_review"
    APPROVED = "approved"
    REJECTED = "rejected"


class ModerationMethod(StrEnum):
    """How a moderation decision was made."""

    AUTO = "auto"
    MANUAL = "manual"


class UserRole(StrEnum):
    """User roles within an organization."""

    ADMIN = "admin"
    MODERATOR = "moderator"
    VIEWER = "viewer"


class UserStatus(StrEnum):
    """User account statuses."""

    ACTIVE = "active"
    DISABLED = "disabled"
    INVITED = "invited"


# Product limits per subscription tier
PRODUCT_LIMITS: dict[SubscriptionTier, int] = {
    SubscriptionTier.STARTER: 3,
    SubscriptionTier.SMALL_BUSINESS: 10,
    SubscriptionTier.GROWTH: 50,
    SubscriptionTier.BUSINESS: 200,
    SubscriptionTier.ENTERPRISE: 1000,
}

"""Environment configuration loaded via AWS Lambda Powertools Parameters."""

from __future__ import annotations

import os
from functools import lru_cache

from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    """Application configuration sourced from environment variables."""

    stage: str = Field(default="dev", description="Deployment stage (dev, staging, prod)")
    aws_region: str = Field(default="us-east-1", description="AWS region")
    dynamodb_endpoint: str | None = Field(default=None, description="DynamoDB local endpoint override")

    # Table names
    organizations_table: str = Field(default="organizations")
    api_tokens_table: str = Field(default="api_tokens")
    products_table: str = Field(default="products")
    reviews_table: str = Field(default="reviews")
    moderation_policies_table: str = Field(default="moderation_policies")
    rating_aggregates_table: str = Field(default="rating_aggregates")
    rate_limit_counters_table: str = Field(default="rate_limit_counters")

    # S3
    analytics_bucket: str = Field(default="review-platform-analytics")

    # SES
    ses_sender_email: str = Field(default="noreply@gomezmera.io")
    ses_region: str = Field(default="us-east-1")

    # Stripe
    stripe_secret_key: str = Field(default="")
    stripe_webhook_secret: str = Field(default="")

    # EventBridge
    event_bus_name: str = Field(default="review-platform-events")

    # SQS
    webhook_queue_url: str = Field(default="")


@lru_cache(maxsize=1)
def get_config() -> AppConfig:
    """Load and cache application configuration from environment variables.

    Uses Powertools-compatible environment variable naming.
    All config is loaded from environment with sensible defaults for local development.
    """
    return AppConfig(
        stage=os.environ.get("STAGE", "dev"),
        aws_region=os.environ.get("AWS_REGION", "us-east-1"),
        dynamodb_endpoint=os.environ.get("DYNAMODB_ENDPOINT"),
        organizations_table=os.environ.get("ORGANIZATIONS_TABLE", "organizations"),
        api_tokens_table=os.environ.get("API_TOKENS_TABLE", "api_tokens"),
        products_table=os.environ.get("PRODUCTS_TABLE", "products"),
        reviews_table=os.environ.get("REVIEWS_TABLE", "reviews"),
        moderation_policies_table=os.environ.get("MODERATION_POLICIES_TABLE", "moderation_policies"),
        rating_aggregates_table=os.environ.get("RATING_AGGREGATES_TABLE", "rating_aggregates"),
        rate_limit_counters_table=os.environ.get("RATE_LIMIT_COUNTERS_TABLE", "rate_limit_counters"),
        analytics_bucket=os.environ.get("ANALYTICS_BUCKET", "review-platform-analytics"),
        ses_sender_email=os.environ.get("SES_SENDER_EMAIL", "noreply@gomezmera.io"),
        ses_region=os.environ.get("SES_REGION", "us-east-1"),
        stripe_secret_key=os.environ.get("STRIPE_SECRET_KEY", ""),
        stripe_webhook_secret=os.environ.get("STRIPE_WEBHOOK_SECRET", ""),
        event_bus_name=os.environ.get("EVENT_BUS_NAME", "review-platform-events"),
        webhook_queue_url=os.environ.get("WEBHOOK_QUEUE_URL", ""),
    )

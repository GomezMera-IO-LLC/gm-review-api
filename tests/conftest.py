"""Shared pytest fixtures with moto mocks for AWS services."""

from __future__ import annotations

import os
from typing import Generator

import boto3
import pytest
from moto import mock_aws


# Ensure AWS SDK doesn't hit real services
@pytest.fixture(autouse=True)
def _aws_credentials() -> None:
    """Set dummy AWS credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


@pytest.fixture
def dynamodb_resource(  # noqa: ANN201
    _aws_credentials: None,
) -> Generator:
    """Provide a mocked DynamoDB resource."""
    with mock_aws():
        yield boto3.resource("dynamodb", region_name="us-east-1")


@pytest.fixture
def ses_client(  # noqa: ANN201
    _aws_credentials: None,
) -> Generator:
    """Provide a mocked SES client."""
    with mock_aws():
        client = boto3.client("ses", region_name="us-east-1")
        # Verify a sender email so SES allows sending
        client.verify_email_identity(EmailAddress="noreply@gomezmera.io")
        yield client


@pytest.fixture
def s3_client(  # noqa: ANN201
    _aws_credentials: None,
) -> Generator:
    """Provide a mocked S3 client."""
    with mock_aws():
        client = boto3.client("s3", region_name="us-east-1")
        client.create_bucket(Bucket="review-platform-analytics")
        yield client


@pytest.fixture
def sqs_client(  # noqa: ANN201
    _aws_credentials: None,
) -> Generator:
    """Provide a mocked SQS client."""
    with mock_aws():
        client = boto3.client("sqs", region_name="us-east-1")
        client.create_queue(QueueName="webhook-delivery-queue")
        yield client


@pytest.fixture
def eventbridge_client(  # noqa: ANN201
    _aws_credentials: None,
) -> Generator:
    """Provide a mocked EventBridge client."""
    with mock_aws():
        client = boto3.client("events", region_name="us-east-1")
        client.create_event_bus(Name="review-platform-events")
        yield client

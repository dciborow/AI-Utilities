"""
AI-Utilities - test_validation.py

Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""

from azure_utils import directory
from azure_utils.configuration.configuration_validation import Validation, ValidationResult
from azure_utils.machine_learning.utils import load_configuration
from azure_utils.utilities import check_login

cfg = load_configuration(directory.replace("azure_utils", "workspace_conf.yml"))
v = Validation()


def test_subscription_validation_success():
    if check_login():
        r = v.validate_input("subscription_id", cfg['subscription_id'])
        Validation.dump_validation_result(r)
        assert r.status is ValidationResult.success


def test_subscription_validation_failure():
    r = v.validate_input("subscription_id", "<>>")
    Validation.dump_validation_result(r)
    assert r.status is ValidationResult.failure


def test_validation_warning():
    r = v.validate_input("foo", "asbas;klj;ijer;kasdf")
    Validation.dump_validation_result(r)
    assert r.status is ValidationResult.warning


def test_workspace_validation_failure():
    r = v.validate_input("workspace_name", "<mygroup>")
    Validation.dump_validation_result(r)
    assert r.status is ValidationResult.failure

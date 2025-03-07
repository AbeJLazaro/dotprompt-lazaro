# Copyright 2025 Google LLC
# SPDX-License-Identifier: Apache-2.0

"""Utility functions for dotpromptz."""

from typing import Any


def remove_undefined_fields(obj: Any) -> Any:
    """Remove undefined fields (None values) from an object recursively.

    This function handles dictionaries, lists, and primitive types.  For
    dictionaries, it removes keys with None values and processes nested
    structures.  For lists, it removes None elements and processes nested
    structures.  For primitive types and None, it returns the value as is.

    Args:
        obj: The object to process.

    Returns:
        The object with undefined fields removed.
    """
    if obj is None or not isinstance(obj, dict | list):
        return obj

    # Lists.
    if isinstance(obj, list):
        return [
            remove_undefined_fields(item) for item in obj if item is not None
        ]

    # Dicts.
    result = {}
    for key, value in obj.items():
        if value is not None:
            result[key] = remove_undefined_fields(value)
    return result

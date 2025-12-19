# SPDX-License-Identifier: MIT
# Copyright © 2025 Dylan Baker

from typing_extensions import TypeAlias

from . import v1_0

# This is a union of every major version 1 revision of the build-details.json
PEP739_v1: TypeAlias = v1_0.PEP739

# This is a union of every possible version of the build-details.json
PEP739: TypeAlias = PEP739_v1

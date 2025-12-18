# SPDX-License-Identifier: MIT
# Copyright © 2025 Dylan Baker

from typing import Literal, TypedDict

from typing_extensions import NotRequired


class VersionInfo(TypedDict):

    major: int
    minor: int
    micro: int
    serial: int
    releaselevel: Literal['alpha', 'beta', 'candidate', 'final']


class Language(TypedDict):

    version: str
    version_info: NotRequired[VersionInfo]


class Implementation(TypedDict):

    # TODO: this allows extra properties, which currently cannot be modeled

    name: str
    version: VersionInfo


class ABI(TypedDict):

    flags: list[str]
    extension_suffix: NotRequired[str]
    stable_abi_suffix: NotRequired[str]


class Suffixes(TypedDict):

    # TODO: this allows extra properties, which currently cannot be modeled

    source: list[str]
    bytecode: list[str]
    debug_bytecode: list[str]
    optimized_bytecode: list[str]
    extension: list[str]


class LibPython(TypedDict, total=False):

    dynamic: str
    dynamic_stableabi: str
    static: str
    link_extensions: bool


class CAPI(TypedDict):

    headers: str
    pkgconfig_path: NotRequired[str]


class PEP739(TypedDict):

    schema_version: str
    base_prefix: str
    base_interpreter: NotRequired[str]
    platform: str
    language: Language
    implementation: Implementation
    abi: NotRequired[ABI]
    suffixes: NotRequired[Suffixes]  # TODO
    libpython: NotRequired[LibPython]
    c_api: NotRequired[CAPI]
    arbitrary_data: NotRequired[dict[str, object]]

#!/usr/bin/env python3
# Copyright (C) 2023 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# generated by datamodel-codegen:
#   filename:  vue_types.json
#   timestamp: 2024-03-17T12:37:34+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class VueBase:
    title: str
    help: str


@dataclass
class VueInteger(VueBase):
    vue_type: str = "integer"
    label: str | None = None
    unit: str | None = None


@dataclass
class VueFloat(VueBase):
    vue_type: str = "float"
    label: str | None = None
    unit: str | None = None


@dataclass
class VueLegacyValuespec(VueBase):
    vue_type: str = "legacy_valuespec"


@dataclass
class VueText(VueBase):
    vue_type: str = "text"
    placeholder: str | None = None


@dataclass
class Model:
    all_schemas: list[VueSchema] | None = None


@dataclass
class VueList(VueBase):
    vue_type: str = "list"
    add_text: str | None = None
    vue_schema: VueSchema | None = None


@dataclass
class VueDictionaryElement:
    ident: str
    required: bool
    default_value: Any
    vue_schema: VueSchema


@dataclass
class VueDictionary(VueBase):
    elements: list[VueDictionaryElement]
    vue_type: str = "dictionary"


VueSchema = VueInteger | VueFloat | VueText | VueDictionary | VueList | VueLegacyValuespec

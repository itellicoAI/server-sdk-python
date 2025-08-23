# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AmbientSoundParam"]


class AmbientSoundParam(TypedDict, total=False):
    type: Optional[
        Literal[
            "open_plan_office", "customer_service_center", "internet_cafe", "urban_street", "rural_outdoors", "ac_fan"
        ]
    ]
    """Available ambient background sounds to enhance conversation realism"""

    volume: float
    """Controls the volume of the ambient sound.

    Value ranging from [-1.0, 1.0]. Lower values mean quieter ambient sound, while
    higher values mean louder ambient sound. 0.0 is normal volume.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AmbientSound"]


class AmbientSound(BaseModel):
    type: Optional[
        Literal[
            "open_plan_office", "customer_service_center", "internet_cafe", "urban_street", "rural_outdoors", "ac_fan"
        ]
    ] = None
    """Available ambient background sounds to enhance conversation realism"""

    volume: Optional[float] = None
    """Controls the volume of the ambient sound.

    Value ranging from [-1.0, 1.0]. Lower values mean quieter ambient sound, while
    higher values mean louder ambient sound. 0.0 is normal volume.
    """

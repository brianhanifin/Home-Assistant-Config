"""Centralite 4200-C Plug."""
import logging

from zigpy.profiles import zha, zll
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    Identify,
    Groups,
    Scenes,
    OnOff,
    Ota,
    PollControl,
)

#from zhaquirks.centralite import CENTRALITE
from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)


CENTRALITE_CLUSTER_ID = 0x0B05  # decimal = 2821

_LOGGER = logging.getLogger(__name__)

#Node Descriptor:
#  <Optional byte1=1 byte2=64 mac_capability_flags=142 manufacturer_code=4174
#  maximum_buffer_size=82 maximum_incoming_transfer_size=82
#  server_mask=11264 maximum_outgoing_transfer_size=82
#  descriptor_capability_field=0>
#
#Endpoint information:
#  <Optional endpoint=1 profile=260 device_type=256 device_version=0
#  input_clusters=[0, 3, 4, 5, 6, 2821]
#  output_clusters=[3, 6, 25]>


class CentralitePlug4200C(CustomDevice):
    """Centralite 4-Series Smart Outlet Mini 4200-C."""

    signature = {
        ENDPOINTS: {
            # <Optional endpoint=1 profile=260 device_type=256 device_version=0
            # input_clusters=[0, 3, 4, 5, 6, 2821]
            # output_clusters=[3, 6, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    CENTRALITE_CLUSTER_ID,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                ],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    CENTRALITE_CLUSTER_ID,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                ],
            }
        }
    }

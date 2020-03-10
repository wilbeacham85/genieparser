# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/software/volume' resources
# =============================================


class SysSoftwareVolumeSchema(MetaParser):

    schema = {}


class SysSoftwareVolume(SysSoftwareVolumeSchema):
    """ To F5 resource for /mgmt/tm/sys/software/volume
    """

    cli_command = "/mgmt/tm/sys/software/volume"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/memory' resources
# =============================================


class SysMemorySchema(MetaParser):

    schema = {}


class SysMemory(SysMemorySchema):
    """ To F5 resource for /mgmt/tm/sys/memory
    """

    cli_command = "/mgmt/tm/sys/memory"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

# ==============================
# Schema for 'show track'
# ==============================
class ShowTrackSchema(MetaParser):

    ''' Schema for "show track" '''

# These are the key-value pairs to add to the parsed dictionary
    schema = {'obj_id':
                {Any():
                     {'obj_type': str,
                      'obj_instance': str,
                      'obj_param': str,
                      'obj_timer_value': str,
                      'obj_state': str,
                      'obj_chg_cnt': str,
                      'last_chg_time': str,
                      'ipsla_rcode': str,
                      'up_delay': str,
                      'obj_down_delay': str
                      }
                },
            }

# Python (this imports the Python re module for RegEx)
import re

# ==============================
# Parser for 'show track'
# ==============================

# The parser class inherits from the schema class
class ShowTrack(ShowTrackSchema):
    """Parser for show track"""
    cli_command = ['show track']
    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initializes the Python dictionary variable
        parsed_dict = {}
        
        attrValPairsToCheck = [
            ('show.track.obj_id',               None),
            ('show.track.obj_instance',         None),
            ('show.track.obj_param',            None),
            ('show.track.obj_timer_value',      None),
            ('show.track.obj_state',            None),
            ('show.track.obj_chg_cnt',          None),
            ('show.track.last_chg_time',        None),
            ('show.track.ipsla_rcode',          None),
            ('show.track.up_delay',             None),
            ('show.track.obj_down_delay',       None),
        ]
        if output:
            res = parsergen.oper_fill(attrvalpairs=attrValPairsToCheck, 
                                      device_output=output, )

        # Defines the regex for the first line of device output, which is:
        # Sessions for VRF default, total: 3, established: 3
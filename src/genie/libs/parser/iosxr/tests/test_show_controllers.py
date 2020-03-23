
# Python
import unittest
from unittest.mock import Mock

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxr show_controllers
from genie.libs.parser.iosxr.show_controllers import (ShowControllersCoherentDSP,
                                                     ShowControllersOptics,
                                                     ShowControllersFiaDiagshellL2showLocation,
                                                     ShowControllersFiaDiagshellDiagCosqQpairEgpMap)


# =====================================================
#  Unit test for 'show controllers coherentDSP {port}'
# =====================================================
class test_show_controllers_coherentDSP(unittest.TestCase):
    '''Unit test for show controllers coherentDSP {port}'''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "0/0/1/2": {
            "port": "CoherentDSP 0/0/1/2",
            "controller_state": "Up",
            "inherited_secondary_state": "Normal",
            "configured_secondary_state": "Normal",
            "derived_state": "In Service",
            "loopback_mode": "None",
            "ber_thresholds_sf": "1.0E-5",
            "ber_thresholds_sd": "1.0E-7",
            "performance_monitoring": "Enable",
            "alarm_info": {
                "los": 1,
                "lof": 0,
                "lom": 0,
                "oof": 0,
                "oom": 0,
                "ais": 0,
                "iae": 0,
                "biae": 0,
                "sf_ber": 0,
                "sd_ber": 0,
                "bdi": 2,
                "tim": 0,
                "fecmis_match": 0,
                "fec_unc": 0
            },
            "detected_alarms": "None",
            "bit_error_rate_info": {
                "prefec_ber": "0.0E+00",
                "postfec_ber": "0.0E+00",
            },
            "otu_tti": "Received",
            "fec_mode": "STANDARD"
        },
    }

    golden_output = {'execute.return_value': '''
        #show controllers coherentDSP 0/0/1/2
        Sat Aug  3 03:10:15.685 EST

        Port                                            : CoherentDSP 0/0/1/2
        Controller State                                : Up
        Inherited Secondary State                       : Normal
        Configured Secondary State                      : Normal
        Derived State                                   : In Service
        Loopback mode                                   : None
        BER Thresholds                                  : SF = 1.0E-5  SD = 1.0E-7
        Performance Monitoring                          : Enable

        Alarm Information:
        LOS = 1 LOF = 0 LOM = 0
        OOF = 0 OOM = 0 AIS = 0
        IAE = 0 BIAE = 0        SF_BER = 0
        SD_BER = 0      BDI = 2 TIM = 0
        FECMISMATCH = 0 FEC-UNC = 0     
        Detected Alarms                                 : None

        Bit Error Rate Information
        PREFEC  BER                                     : 0.0E+00 
        POSTFEC BER                                     : 0.0E+00 

        OTU TTI Received 

        FEC mode                                        : STANDARD
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersCoherentDSP(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(port='0/0/1/2')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowControllersCoherentDSP(device=self.device)
        parsed_output = obj.parse(port='0/0/1/2')
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ==================================================
#  Unit test for 'show controllers optics {port}'
# ==================================================
class test_show_controllers_optics(unittest.TestCase):
    '''Unit test for show controllers optics {port}'''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        "0/0/0/0": {
            "name": "Optics 0/0/0/0",
            "controller_state": "Up",
            "transport_admin_state": "In Service",
            "laser_state": "On",
            "led_state": "Green",
            "optics_status": {
                "optics_type": "SFP+ 10G SR",
                "wavelength": "850.00 nm",
                "alarm_status": {
                    "detected_alarms": [],
                },
                "los_lol_fault_status": {},
                "laser_bias_current": "6.1 mA",
                "actual_tx_power": "-2.45 dBm",
                "rx_power": "-7.56 dBm",
                "performance_monitoring": "Enable",
                "threshold_values": {
                    "Rx Power Threshold(dBm)": {
                        "parameter": "Rx Power Threshold(dBm)",
                        "high_alarm": "2.0",
                        "low_alarm": "-13.9",
                        "high_warning": "-1.0",
                        "low_warning": "-9.9"
                    },
                    "Tx Power Threshold(dBm)": {
                        "parameter": "Tx Power Threshold(dBm)",
                        "high_alarm": "1.6",
                        "low_alarm": "-11.3",
                        "high_warning": "-1.3",
                        "low_warning": "-7.3"
                    },
                    "LBC Threshold(mA)": {
                        "parameter": "LBC Threshold(mA)",
                        "high_alarm": "10.00",
                        "low_alarm": "2.00",
                        "high_warning": "10.00",
                        "low_warning": "2.00"
                    },
                    "Temp. Threshold(celsius)": {
                        "parameter": "Temp. Threshold(celsius)",
                        "high_alarm": "75.00",
                        "low_alarm": "-5.00",
                        "high_warning": "70.00",
                        "low_warning": "0.00"
                    },
                    "Voltage Threshold(volt)": {
                        "parameter": "Voltage Threshold(volt)",
                        "high_alarm": "3.63",
                        "low_alarm": "2.97",
                        "high_warning": "3.46",
                        "low_warning": "3.13"
                    }
                },
                "polarization_parameters": "not supported by optics",
                "temperature": "35.00 Celsius",
                "voltage": "3.26 V"
            },
            "transceiver_vendor_details": {
                "form_factor": "SFP+",
                "optics_type": "SFP+ 10G SR",
                "name": "CISCO-AVAGO",
                "oui_number": "00.17.6a",
                "part_number": "SFBR-7702SDZ-CS5",
                "rev_number": "G2.5",
                "serial_number": "AGD162040SP",
                "pid": "SFP-10G-SR",
                "vid": "V03",
                "date_code": "12/05/20"
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
        #show controllers optics 0/0/0/0
        Sat Aug  3 03:11:08.682 EST

         Controller State: Up 
         Transport Admin State: In Service 
         Laser State: On 
         LED State: Green 
         Optics Status 
                 Optics Type:  SFP+ 10G SR
                 Wavelength = 850.00 nm 

                 Alarm Status:
                 -------------
                 Detected Alarms: None


                 LOS/LOL/Fault Status:

                 Laser Bias Current = 6.1 mA
                 Actual TX Power = -2.45 dBm 
                 RX Power = -7.56 dBm 

                 Performance Monitoring: Enable 

                 THRESHOLD VALUES
                 ----------------

                 Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
                 ------------------------  ----------  ---------  ------------  -----------
                 Rx Power Threshold(dBm)          2.0      -13.9          -1.0         -9.9
                 Tx Power Threshold(dBm)          1.6      -11.3          -1.3         -7.3
                 LBC Threshold(mA)              10.00       2.00         10.00         2.00
                 Temp. Threshold(celsius)       75.00      -5.00         70.00         0.00
                 Voltage Threshold(volt)         3.63       2.97          3.46         3.13

                 Polarization parameters not supported by optics

                 Temperature = 35.00 Celsius 
                 Voltage = 3.26 V 

         Transceiver Vendor Details

                 Form Factor            : SFP+
                 Optics type            : SFP+ 10G SR
                 Name                   : CISCO-AVAGO
                 OUI Number             : 00.17.6a
                 Part Number            : SFBR-7702SDZ-CS5
                 Rev Number             : G2.5
                 Serial Number          : AGD162040SP
                 PID                    : SFP-10G-SR
                 VID                    : V03
                 Date Code(yy/mm/dd)    : 12/05/20
    '''}

    golden_parsed_output2 = {
        "0/0/1/2": {
            "name": "Optics 0/0/1/2",
            "controller_state": "Up",
            "transport_admin_state": "In Service",
            "laser_state": "On",
            "led_state": "Green",
            "optics_status": {
                "optics_type": "CFP2 DWDM",
                "dwdm_carrier_info": "C BAND",
                "msa_itu_channel": "97",
                "frequency": "191.30THz",
                "wavelength": "1567.133nm",
                "alarm_status": {
                    "detected_alarms": [],
                },
                "los_lol_fault_status": {},
                "alarm_statistics": {
                    "high_rx_pwr": 0,
                    "low_rx_pwr": 1,
                    "high_tx_pwr": 0,
                    "low_tx_pwr": 1,
                    "high_lbc": 0,
                    "high_dgd": 0,
                    "oor_cd": 0,
                    "osnr": 0,
                    "wvl_ool": 0,
                    "mea": 0,
                    "improper_rem": 0,
                    "tc_power_prov_mismatch": 0
                },
                "laser_bias_current": "0.0 %",
                "actual_tx_power": "0.99 dBm",
                "rx_power": "-20.50 dBm",
                "performance_monitoring": "Enable",
                "threshold_values": {
                    "Rx Power Threshold(dBm)": {
                        "parameter": "Rx Power Threshold(dBm)",
                        "high_alarm": "1.5",
                        "low_alarm": "-30.0",
                        "high_warning": "0.0",
                        "low_warning": "0.0"
                    },
                    "Tx Power Threshold(dBm)": {
                        "parameter": "Tx Power Threshold(dBm)",
                        "high_alarm": "3.5",
                        "low_alarm": "-10.0",
                        "high_warning": "0.0",
                        "low_warning": "0.0"
                    },
                    "LBC Threshold(mA)": {
                        "parameter": "LBC Threshold(mA)",
                        "high_alarm": "N/A",
                        "low_alarm": "N/A",
                        "high_warning": "0.00",
                        "low_warning": "0.00"
                    }
                },
                "lbc_high_threshold": "98 %",
                "configured_tx_power": "1.00 dBm",
                "configured_osnr_lower_threshold": "0.00 dB",
                "configured_dgd_higher_threshold": "180.00 ps",
                "chromatic_dispersion": "5 ps/nm",
                "configured_cd_min": "-10000 ps/nm ",
                "configured_cd_max": "16000 ps/nm",
                "optical_snr": "27.00 dB",
                "polarization_dependent_loss": "0.00 dB",
                "differential_group_delay": "2.00 ps"
            },
            "transceiver_vendor_details": {
                "form_factor": "CFP2",
                "name": "CISCO-ACACIA",
                "part_number": "AC200-D23-190",
                "rev_number": "16672",
                "serial_number": "180653009",
                "pid": "ONS-C2-WDM-DE-1HL",
                "vid": "VES#",
                "date_code": "18/02/03"
            }
        }
    }

    golden_output2 = {'execute.return_value': '''
        #show controllers optics 0/0/1/2
        Sat Aug  3 03:11:51.141 EST

         Controller State: Up 
         Transport Admin State: In Service 
         Laser State: On 
         LED State: Green 
         Optics Status 
                 Optics Type:  CFP2 DWDM
                 DWDM carrier Info: C BAND, MSA ITU Channel=97, Frequency=191.30THz,
                 Wavelength=1567.133nm 

                 Alarm Status:
                 -------------
                 Detected Alarms: None


                 LOS/LOL/Fault Status:

                 Alarm Statistics:

                 -------------
                 HIGH-RX-PWR = 0            LOW-RX-PWR = 1          
                 HIGH-TX-PWR = 0            LOW-TX-PWR = 1          
                 HIGH-LBC = 0               HIGH-DGD = 0          
                 OOR-CD = 0                 OSNR = 0          
                 WVL-OOL = 0                MEA  = 0          
                 IMPROPER-REM = 0          
                 TX-POWER-PROV-MISMATCH = 0          
                 Laser Bias Current = 0.0 %
                 Actual TX Power = 0.99 dBm 
                 RX Power = -20.50 dBm 

                 Performance Monitoring: Enable 

                 THRESHOLD VALUES
                 ----------------

                 Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
                 ------------------------  ----------  ---------  ------------  -----------
                 Rx Power Threshold(dBm)          1.5      -30.0           0.0          0.0
                 Tx Power Threshold(dBm)          3.5      -10.0           0.0          0.0
                 LBC Threshold(mA)                N/A        N/A          0.00         0.00

                 LBC High Threshold = 98 % 
                 Configured Tx Power = 1.00 dBm 
                 Configured OSNR lower Threshold = 0.00 dB 
                 Configured DGD Higher Threshold = 180.00 ps 
                 Chromatic Dispersion 5 ps/nm 
                 Configured CD-MIN -10000 ps/nm  CD-MAX 16000 ps/nm 
                 Optical Signal to Noise Ratio = 27.00 dB 
                 Polarization Dependent Loss = 0.00 dB 
                 Differential Group Delay = 2.00 ps 
                  
         Transceiver Vendor Details
                  
                 Form Factor            : CFP2
                 Name                   : CISCO-ACACIA    
                 Part Number            : AC200-D23-190   
                 Rev Number             : 16672
                 Serial Number          : 180653009       
                 PID                    : ONS-C2-WDM-DE-1HL 
                 VID                    : VES#
                 Date Code(yy/mm/dd)    : 18/02/03
    '''}

    golden_parsed_output3 = {
        "0/0/0/20": {
            "name": "Optics 0/0/0/20",
            "controller_state": "Down",
            "transport_admin_state": "In Service",
            "laser_state": "Off",
            "optics_status": {
                "optics_type": "Unavailable",
                "dwdm_carrier_info": "Unavailable",
                "msa_itu_channel": "Unavailable",
                "frequency": "Unavailable",
                "wavelength": "Unavailable",
                "actual_tx_power": "Unavailable",
                "rx_power": "Unavailable"
            }
        }
    }

    golden_output3 = {'execute.return_value': '''
        #show controllers optics 0/0/0/20
        Sat Aug  3 03:15:25.076 EST

         Controller State: Down 
         Transport Admin State: In Service 
         Laser State: Off 
                 Optics not present
                 Optics Type: Unavailable
                 DWDM Carrier Info: Unavailable, MSA ITU Channel= Unavailable, Frequency= Unavailable , Wavelength= Unavailable 
                 TX Power = Unavailable 
                 RX Power = Unavailable 
    '''}

    golden_parsed_output4 = {
        "0/0/0/18": {
            "name": "Optics 0/0/0/18",
            "controller_state": "Up",
            "transport_admin_state": "In Service",
            "laser_state": "Off",
            "led_state": "Off",
            "optics_status": {
                "optics_type": "SFP+ 10G SR",
                "wavelength": "850.00 nm",
                "alarm_status": {
                    "detected_alarms": [
                        "LOW-RX1-PWR",
                        "LOW-TX1-PWR",
                        "LOW-TX1_LBC"
                    ]
                },
                "los_lol_fault_status": {
                    "detected_los_lol_fault": [
                        "RX-LOS"
                    ]
                },
                "laser_bias_current": "0.0 mA",
                "actual_tx_power": "-17.25 dBm",
                "rx_power": "-40.00 dBm",
                "performance_monitoring": "Enable",
                "threshold_values": {
                    "Rx Power Threshold(dBm)": {
                        "parameter": "Rx Power Threshold(dBm)",
                        "high_alarm": "2.0",
                        "low_alarm": "-13.9",
                        "high_warning": "-1.0",
                        "low_warning": "-9.9"
                    },
                    "Tx Power Threshold(dBm)": {
                        "parameter": "Tx Power Threshold(dBm)",
                        "high_alarm": "1.6",
                        "low_alarm": "-11.3",
                        "high_warning": "-1.3",
                        "low_warning": "-7.3"
                    },
                    "LBC Threshold(mA)": {
                        "parameter": "LBC Threshold(mA)",
                        "high_alarm": "11.00",
                        "low_alarm": "4.00",
                        "high_warning": "10.00",
                        "low_warning": "5.00"
                    },
                    "Temp. Threshold(celsius)": {
                        "parameter": "Temp. Threshold(celsius)",
                        "high_alarm": "75.00",
                        "low_alarm": "-5.00",
                        "high_warning": "70.00",
                        "low_warning": "0.00"
                    },
                    "Voltage Threshold(volt)": {
                        "parameter": "Voltage Threshold(volt)",
                        "high_alarm": "3.63",
                        "low_alarm": "2.97",
                        "high_warning": "3.46",
                        "low_warning": "3.13"
                    }
                },
                "polarization_parameters": "not supported by optics",
                "temperature": "31.00 Celsius",
                "voltage": "3.30 V"
            },
            "transceiver_vendor_details": {
                "form_factor": "SFP+",
                "optics_type": "SFP+ 10G SR",
                "name": "CISCO-FINISAR",
                "oui_number": "00.90.65",
                "part_number": "FTLX8571D3BCL-C2",
                "rev_number": "A",
                "serial_number": "FNS210108H7",
                "pid": "SFP-10G-SR",
                "vid": "V03",
                "date_code": "17/01/03"
            }
        }
    }

    golden_output4 = {'execute.return_value': '''
        #show controllers optics 0/0/0/18
        Sat Aug  3 03:19:06.519 EST

         Controller State: Up 
         Transport Admin State: In Service 
         Laser State: Off 
         LED State: Off 
         Optics Status 
                 Optics Type:  SFP+ 10G SR
                 Wavelength = 850.00 nm 

                 Alarm Status:
                 -------------
                 Detected Alarms: 
                         LOW-RX1-PWR   
                         LOW-TX1-PWR   
                         LOW-TX1_LBC   

                 LOS/LOL/Fault Status:
                 Detected LOS/LOL/FAULT: RX-LOS   


                 Laser Bias Current = 0.0 mA
                 Actual TX Power = -17.25 dBm 
                 RX Power = -40.00 dBm 

                 Performance Monitoring: Enable 

                 THRESHOLD VALUES
                 ----------------

                 Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
                 ------------------------  ----------  ---------  ------------  -----------
                 Rx Power Threshold(dBm)          2.0      -13.9          -1.0         -9.9
                 Tx Power Threshold(dBm)          1.6      -11.3          -1.3         -7.3
                 LBC Threshold(mA)              11.00       4.00         10.00         5.00
                 Temp. Threshold(celsius)       75.00      -5.00         70.00         0.00
                 Voltage Threshold(volt)         3.63       2.97          3.46         3.13

                 Polarization parameters not supported by optics

                 Temperature = 31.00 Celsius 
                 Voltage = 3.30 V 

         Transceiver Vendor Details

                 Form Factor            : SFP+
                 Optics type            : SFP+ 10G SR
                 Name                   : CISCO-FINISAR
                 OUI Number             : 00.90.65
                 Part Number            : FTLX8571D3BCL-C2
                 Rev Number             : A
                 Serial Number          : FNS210108H7
                 PID                    : SFP-10G-SR
                 VID                    : V03
                 Date Code(yy/mm/dd)    : 17/01/03 
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersOptics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(port='0/0/0/0')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/1/2')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/0/20')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_golden4(self):
        self.device = Mock(**self.golden_output4)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/0/18')
        self.assertEqual(parsed_output, self.golden_parsed_output4)


# ==============================================================================================
#  Unit test for 'show controllers fia diagshell {diagshell_unit} "l2 show" location {location}'
# ==============================================================================================
class test_show_controllers_fia_diagshell_location(unittest.TestCase):
    '''Unit test for:
        * 'show controllers fia diagshell {diagshell_unit} "l2 show" location {location}'
    '''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'nodes': 
            {'0/0/CPU0': 
                {'vlan': 
                    {4: 
                        {'mac': 
                            {'00:00:03:ff:01:0c': 
                                {'encap_id': '0x301d',
                                'gport': '0xc000001',
                                'trunk': 1}}},
                    2522: 
                        {'mac': 
                            {'fc:00:00:ff:01:03': 
                                {'encap_id': '0xffffffff',
                                'gport': '0x9800401d',
                                'static': True}}},
                    2524: 
                        {'mac': 
                            {'fc:00:00:ff:01:0c': 
                                {'encap_id': '0x3001',
                                'gport': '0xc000000',
                                'static': True,
                                'trunk': 0}}},
                    2544: 
                        {'mac': 
                            {'fc:00:00:ff:01:8c': 
                                {'encap_id': '0x2007',
                                'gport': '0x8000048'},
                            'fc:00:00:ff:01:9c': 
                                {'encap_id': '0x2007',
                                'gport': '0x8000048',
                                'trunk': 0}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:UUT4#show controller fia diagshell 0 'l2 show' location all

        Node ID: 0/0/CPU0
        mac=fc:00:00:ff:01:8c vlan=2544 GPORT=0x8000048 encap_id=0x2007
        mac=fc:00:00:ff:01:03 vlan=2522 GPORT=0x9800401d Static encap_id=0xffffffff
        mac=fc:00:00:ff:01:9c vlan=2544 GPORT=0x8000048 Trunk=0 encap_id=0x2007
        mac=fc:00:00:ff:01:0c vlan=2524 GPORT=0xc000000 Trunk=0 Static encap_id=0x3001
        mac=00:00:03:ff:01:0c vlan=4 GPORT=0xc000001 Trunk=1 encap_id=0x301d
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersFiaDiagshellL2showLocation(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowControllersFiaDiagshellL2showLocation(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class TestShowControllersFiaDiagshellDiagCosqQpairEgpMap(unittest.TestCase):
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'node_id': {
            '0/0/CPU0': {
                'egq_mapping': {
                    'port_number': {
                        0: {
                            'base_q_pair': 200,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 25,
                            'tm_port': 0,
                        },
                        1: {
                            'base_q_pair': 138,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 17,
                            'tm_port': 1,
                        },
                        5: {
                            'base_q_pair': 140,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 17,
                            'tm_port': 5,
                        },
                        9: {
                            'base_q_pair': 142,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 17,
                            'tm_port': 9,
                        },
                        13: {
                            'base_q_pair': 136,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 17,
                            'tm_port': 13,
                        },
                        17: {
                            'base_q_pair': 144,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 18,
                            'tm_port': 17,
                        },
                        21: {
                            'base_q_pair': 146,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 18,
                            'tm_port': 21,
                        },
                        25: {
                            'base_q_pair': 166,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 20,
                            'tm_port': 25,
                        },
                        26: {
                            'base_q_pair': 142,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 17,
                            'tm_port': 26,
                        },
                        27: {
                            'base_q_pair': 138,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 17,
                            'tm_port': 27,
                        },
                        28: {
                            'base_q_pair': 168,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 21,
                            'tm_port': 28,
                        },
                        29: {
                            'base_q_pair': 140,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 17,
                            'tm_port': 29,
                        },
                        30: {
                            'base_q_pair': 30,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 3,
                            'tm_port': 30,
                        },
                        31: {
                            'base_q_pair': 148,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 18,
                            'tm_port': 31,
                        },
                        32: {
                            'base_q_pair': 34,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 4,
                            'tm_port': 32,
                        },
                        33: {
                            'base_q_pair': 136,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 17,
                            'tm_port': 33,
                        },
                        34: {
                            'base_q_pair': 146,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 18,
                            'tm_port': 34,
                        },
                        35: {
                            'base_q_pair': 144,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 18,
                            'tm_port': 35,
                        },
                        36: {
                            'base_q_pair': 164,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 20,
                            'tm_port': 36,
                        },
                        37: {
                            'base_q_pair': 172,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 21,
                            'tm_port': 37,
                        },
                        38: {
                            'base_q_pair': 150,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 18,
                            'tm_port': 38,
                        },
                        39: {
                            'base_q_pair': 36,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 4,
                            'tm_port': 39,
                        },
                        40: {
                            'base_q_pair': 32,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 4,
                            'tm_port': 40,
                        },
                        41: {
                            'base_q_pair': 152,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 19,
                            'tm_port': 41,
                        },
                        42: {
                            'base_q_pair': 170,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 21,
                            'tm_port': 42,
                        },
                        43: {
                            'base_q_pair': 154,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 19,
                            'tm_port': 43,
                        },
                        44: {
                            'base_q_pair': 38,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 4,
                            'tm_port': 44,
                        },
                        45: {
                            'base_q_pair': 156,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 19,
                            'tm_port': 45,
                        },
                        46: {
                            'base_q_pair': 158,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 19,
                            'tm_port': 46,
                        },
                        47: {
                            'base_q_pair': 160,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 20,
                            'tm_port': 47,
                        },
                        48: {
                            'base_q_pair': 162,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 20,
                            'tm_port': 48,
                        },
                        49: {
                            'base_q_pair': 176,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 22,
                            'tm_port': 49,
                        },
                        50: {
                            'base_q_pair': 24,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 3,
                            'tm_port': 50,
                        },
                        51: {
                            'base_q_pair': 20,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 2,
                            'tm_port': 51,
                        },
                        52: {
                            'base_q_pair': 18,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 2,
                            'tm_port': 52,
                        },
                        53: {
                            'base_q_pair': 16,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 2,
                            'tm_port': 53,
                        },
                        54: {
                            'base_q_pair': 12,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 1,
                            'tm_port': 54,
                        },
                        55: {
                            'base_q_pair': 14,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 1,
                            'tm_port': 55,
                        },
                        56: {
                            'base_q_pair': 10,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 1,
                            'tm_port': 56,
                        },
                        57: {
                            'base_q_pair': 26,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 3,
                            'tm_port': 57,
                        },
                        58: {
                            'base_q_pair': 178,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 22,
                            'tm_port': 58,
                        },
                        59: {
                            'base_q_pair': 22,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 2,
                            'tm_port': 59,
                        },
                        60: {
                            'base_q_pair': 28,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 3,
                            'tm_port': 60,
                        },
                        61: {
                            'base_q_pair': 174,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 21,
                            'tm_port': 61,
                        },
                        62: {
                            'base_q_pair': 2,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 0,
                            'tm_port': 62,
                        },
                        63: {
                            'base_q_pair': 6,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 0,
                            'tm_port': 63,
                        },
                        64: {
                            'base_q_pair': 8,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 1,
                            'tm_port': 64,
                        },
                        65: {
                            'base_q_pair': 190,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 23,
                            'tm_port': 65,
                        },
                        66: {
                            'base_q_pair': 188,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 23,
                            'tm_port': 66,
                        },
                        67: {
                            'base_q_pair': 0,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 0,
                            'tm_port': 67,
                        },
                        68: {
                            'base_q_pair': 4,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 0,
                            'tm_port': 68,
                        },
                        69: {
                            'base_q_pair': 180,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 22,
                            'tm_port': 69,
                        },
                        70: {
                            'base_q_pair': 186,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 23,
                            'tm_port': 70,
                        },
                        71: {
                            'base_q_pair': 184,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 23,
                            'tm_port': 71,
                        },
                        72: {
                            'base_q_pair': 182,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 22,
                            'tm_port': 72,
                        },
                        80: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 80,
                        },
                        81: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 81,
                        },
                        82: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 82,
                        },
                        83: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 83,
                        },
                        84: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 84,
                        },
                        85: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 85,
                        },
                        86: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 86,
                        },
                        87: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 87,
                        },
                        88: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 88,
                        },
                        89: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 89,
                        },
                        90: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 90,
                        },
                        91: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 91,
                        },
                        92: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 92,
                        },
                        93: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 93,
                        },
                        94: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 94,
                        },
                        95: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 95,
                        },
                        96: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 96,
                        },
                        97: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 97,
                        },
                        98: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 98,
                        },
                        99: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 99,
                        },
                        100: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 100,
                        },
                        101: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 101,
                        },
                        102: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 102,
                        },
                        103: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 103,
                        },
                        128: {
                            'base_q_pair': 104,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 13,
                            'tm_port': 128,
                        },
                        129: {
                            'base_q_pair': 104,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 13,
                            'tm_port': 129,
                        },
                        130: {
                            'base_q_pair': 106,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 13,
                            'tm_port': 130,
                        },
                        131: {
                            'base_q_pair': 106,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 13,
                            'tm_port': 131,
                        },
                        132: {
                            'base_q_pair': 108,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 13,
                            'tm_port': 132,
                        },
                        133: {
                            'base_q_pair': 108,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 13,
                            'tm_port': 133,
                        },
                        134: {
                            'base_q_pair': 110,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 13,
                            'tm_port': 134,
                        },
                        135: {
                            'base_q_pair': 110,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 13,
                            'tm_port': 135,
                        },
                        136: {
                            'base_q_pair': 112,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 14,
                            'tm_port': 136,
                        },
                        137: {
                            'base_q_pair': 112,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 14,
                            'tm_port': 137,
                        },
                        138: {
                            'base_q_pair': 114,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 14,
                            'tm_port': 138,
                        },
                        139: {
                            'base_q_pair': 114,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 14,
                            'tm_port': 139,
                        },
                        140: {
                            'base_q_pair': 116,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 14,
                            'tm_port': 140,
                        },
                        141: {
                            'base_q_pair': 116,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 14,
                            'tm_port': 141,
                        },
                        142: {
                            'base_q_pair': 118,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 14,
                            'tm_port': 142,
                        },
                        143: {
                            'base_q_pair': 118,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 14,
                            'tm_port': 143,
                        },
                        144: {
                            'base_q_pair': 120,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 15,
                            'tm_port': 144,
                        },
                        145: {
                            'base_q_pair': 120,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 15,
                            'tm_port': 145,
                        },
                        146: {
                            'base_q_pair': 122,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 15,
                            'tm_port': 146,
                        },
                        147: {
                            'base_q_pair': 122,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 15,
                            'tm_port': 147,
                        },
                        148: {
                            'base_q_pair': 124,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 15,
                            'tm_port': 148,
                        },
                        149: {
                            'base_q_pair': 124,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 15,
                            'tm_port': 149,
                        },
                        158: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 158,
                        },
                        159: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 159,
                        },
                        160: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 160,
                        },
                        161: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 161,
                        },
                        162: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 162,
                        },
                        163: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 163,
                        },
                        164: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 164,
                        },
                        165: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 165,
                        },
                        166: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 166,
                        },
                        167: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 167,
                        },
                        168: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 168,
                        },
                        169: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 169,
                        },
                        170: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 170,
                        },
                        171: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 171,
                        },
                        172: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 172,
                        },
                        173: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 173,
                        },
                        174: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 174,
                        },
                        175: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 175,
                        },
                        176: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 176,
                        },
                        177: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 177,
                        },
                        178: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 178,
                        },
                        179: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 179,
                        },
                        180: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 180,
                        },
                        181: {
                            'base_q_pair': 255,
                            'core': 0,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 181,
                        },
                        182: {
                            'base_q_pair': 255,
                            'core': 1,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 182,
                        },
                        183: {
                            'base_q_pair': 255,
                            'core': 1,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 183,
                        },
                        184: {
                            'base_q_pair': 255,
                            'core': 1,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 184,
                        },
                        185: {
                            'base_q_pair': 255,
                            'core': 1,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 185,
                        },
                        186: {
                            'base_q_pair': 255,
                            'core': 1,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 186,
                        },
                        187: {
                            'base_q_pair': 255,
                            'core': 1,
                            'priorities': 0,
                            'ps_number': 31,
                            'tm_port': 187,
                        },
                        208: {
                            'base_q_pair': 216,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 27,
                            'tm_port': 208,
                        },
                        232: {
                            'base_q_pair': 232,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 29,
                            'tm_port': 232,
                        },
                        233: {
                            'base_q_pair': 232,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 29,
                            'tm_port': 232,
                        },
                        235: {
                            'base_q_pair': 126,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 15,
                            'tm_port': 235,
                        },
                        240: {
                            'base_q_pair': 240,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 30,
                            'tm_port': 240,
                        },
                        241: {
                            'base_q_pair': 240,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 30,
                            'tm_port': 240,
                        },
                        246: {
                            'base_q_pair': 128,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 16,
                            'tm_port': 246,
                        },
                        247: {
                            'base_q_pair': 126,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 15,
                            'tm_port': 247,
                        },
                        248: {
                            'base_q_pair': 130,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 16,
                            'tm_port': 248,
                        },
                        249: {
                            'base_q_pair': 128,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 16,
                            'tm_port': 249,
                        },
                        250: {
                            'base_q_pair': 132,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 16,
                            'tm_port': 250,
                        },
                        251: {
                            'base_q_pair': 130,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 16,
                            'tm_port': 251,
                        },
                        252: {
                            'base_q_pair': 134,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 16,
                            'tm_port': 252,
                        },
                        253: {
                            'base_q_pair': 192,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 24,
                            'tm_port': 253,
                        },
                        564: {
                            'base_q_pair': 248,
                            'core': 0,
                            'priorities': 2,
                            'ps_number': 31,
                            'tm_port': 255,
                        },
                        565: {
                            'base_q_pair': 248,
                            'core': 1,
                            'priorities': 2,
                            'ps_number': 31,
                            'tm_port': 255,
                        },
                    },
                },
            },
        },
    }
    golden_output1 = {'execute.return_value': '''
        show controllers fia diagshell 0 "diag cosq qpair egq map" location all
        Mon Mar 23 13:08:25.947 UTC
        
        Node ID: 0/0/CPU0
        
        EGQ MAPPING:
        **************
        Port #  |  Priorities  |  Base Q-Pair  |   PS #  | Core | TM Port |
        ---------|--------------|---------------|---------|------|---------|
            0    |       2      |      200      |    25   |   0  |     0   |
            1    |       2      |      138      |    17   |   1  |     1   |
            5    |       2      |      140      |    17   |   1  |     5   |
            9    |       2      |      142      |    17   |   1  |     9   |
        13    |       2      |      136      |    17   |   1  |    13   |
        17    |       2      |      144      |    18   |   1  |    17   |
        21    |       2      |      146      |    18   |   1  |    21   |
        25    |       2      |      166      |    20   |   0  |    25   |
        26    |       2      |      142      |    17   |   0  |    26   |
        27    |       2      |      138      |    17   |   0  |    27   |
        28    |       2      |      168      |    21   |   0  |    28   |
        29    |       2      |      140      |    17   |   0  |    29   |
        30    |       2      |       30      |     3   |   0  |    30   |
        31    |       2      |      148      |    18   |   0  |    31   |
        32    |       2      |       34      |     4   |   0  |    32   |
        33    |       2      |      136      |    17   |   0  |    33   |
        34    |       2      |      146      |    18   |   0  |    34   |
        35    |       2      |      144      |    18   |   0  |    35   |
        36    |       2      |      164      |    20   |   0  |    36   |
        37    |       2      |      172      |    21   |   0  |    37   |
        38    |       2      |      150      |    18   |   0  |    38   |
        39    |       2      |       36      |     4   |   0  |    39   |
        40    |       2      |       32      |     4   |   0  |    40   |
        41    |       2      |      152      |    19   |   0  |    41   |
        42    |       2      |      170      |    21   |   0  |    42   |
        43    |       2      |      154      |    19   |   0  |    43   |
        44    |       2      |       38      |     4   |   0  |    44   |
        45    |       2      |      156      |    19   |   0  |    45   |
        46    |       2      |      158      |    19   |   0  |    46   |
        47    |       2      |      160      |    20   |   0  |    47   |
        48    |       2      |      162      |    20   |   0  |    48   |
        49    |       2      |      176      |    22   |   0  |    49   |
        50    |       2      |       24      |     3   |   0  |    50   |
        51    |       2      |       20      |     2   |   0  |    51   |
        52    |       2      |       18      |     2   |   0  |    52   |
        53    |       2      |       16      |     2   |   0  |    53   |
        54    |       2      |       12      |     1   |   0  |    54   |
        55    |       2      |       14      |     1   |   0  |    55   |
        56    |       2      |       10      |     1   |   0  |    56   |
        57    |       2      |       26      |     3   |   0  |    57   |
        58    |       2      |      178      |    22   |   0  |    58   |
        59    |       2      |       22      |     2   |   0  |    59   |
        60    |       2      |       28      |     3   |   0  |    60   |
        61    |       2      |      174      |    21   |   0  |    61   |
        62    |       2      |        2      |     0   |   0  |    62   |
        63    |       2      |        6      |     0   |   0  |    63   |
        64    |       2      |        8      |     1   |   0  |    64   |
        65    |       2      |      190      |    23   |   0  |    65   |
        66    |       2      |      188      |    23   |   0  |    66   |
        67    |       2      |        0      |     0   |   0  |    67   |
        68    |       2      |        4      |     0   |   0  |    68   |
        69    |       2      |      180      |    22   |   0  |    69   |
        70    |       2      |      186      |    23   |   0  |    70   |
        71    |       2      |      184      |    23   |   0  |    71   |
        72    |       2      |      182      |    22   |   0  |    72   |
        80    |       0      |      255      |    31   |   0  |    80   |
        81    |       0      |      255      |    31   |   0  |    81   |
        82    |       0      |      255      |    31   |   0  |    82   |
        83    |       0      |      255      |    31   |   0  |    83   |
        84    |       0      |      255      |    31   |   0  |    84   |
        85    |       0      |      255      |    31   |   0  |    85   |
        86    |       0      |      255      |    31   |   0  |    86   |
        87    |       0      |      255      |    31   |   0  |    87   |
        88    |       0      |      255      |    31   |   0  |    88   |
        89    |       0      |      255      |    31   |   0  |    89   |
        90    |       0      |      255      |    31   |   0  |    90   |
        91    |       0      |      255      |    31   |   0  |    91   |
        92    |       0      |      255      |    31   |   0  |    92   |
        93    |       0      |      255      |    31   |   0  |    93   |
        94    |       0      |      255      |    31   |   0  |    94   |
        95    |       0      |      255      |    31   |   0  |    95   |
        96    |       0      |      255      |    31   |   0  |    96   |
        97    |       0      |      255      |    31   |   0  |    97   |
        98    |       0      |      255      |    31   |   0  |    98   |
        99    |       0      |      255      |    31   |   0  |    99   |
        100    |       0      |      255      |    31   |   0  |   100   |
        101    |       0      |      255      |    31   |   0  |   101   |
        102    |       0      |      255      |    31   |   0  |   102   |
        103    |       0      |      255      |    31   |   0  |   103   |
        128    |       2      |      104      |    13   |   0  |   128   |
        129    |       2      |      104      |    13   |   1  |   129   |
        130    |       2      |      106      |    13   |   0  |   130   |
        131    |       2      |      106      |    13   |   1  |   131   |
        132    |       2      |      108      |    13   |   0  |   132   |
        133    |       2      |      108      |    13   |   1  |   133   |
        134    |       2      |      110      |    13   |   0  |   134   |
        135    |       2      |      110      |    13   |   1  |   135   |
        136    |       2      |      112      |    14   |   0  |   136   |
        137    |       2      |      112      |    14   |   1  |   137   |
        138    |       2      |      114      |    14   |   0  |   138   |
        139    |       2      |      114      |    14   |   1  |   139   |
        140    |       2      |      116      |    14   |   0  |   140   |
        141    |       2      |      116      |    14   |   1  |   141   |
        142    |       2      |      118      |    14   |   0  |   142   |
        143    |       2      |      118      |    14   |   1  |   143   |
        144    |       2      |      120      |    15   |   0  |   144   |
        145    |       2      |      120      |    15   |   1  |   145   |
        146    |       2      |      122      |    15   |   0  |   146   |
        147    |       2      |      122      |    15   |   1  |   147   |
        148    |       2      |      124      |    15   |   0  |   148   |
        149    |       2      |      124      |    15   |   1  |   149   |
        158    |       0      |      255      |    31   |   0  |   158   |
        159    |       0      |      255      |    31   |   0  |   159   |
        160    |       0      |      255      |    31   |   0  |   160   |
        161    |       0      |      255      |    31   |   0  |   161   |
        162    |       0      |      255      |    31   |   0  |   162   |
        163    |       0      |      255      |    31   |   0  |   163   |
        164    |       0      |      255      |    31   |   0  |   164   |
        165    |       0      |      255      |    31   |   0  |   165   |
        166    |       0      |      255      |    31   |   0  |   166   |
        167    |       0      |      255      |    31   |   0  |   167   |
        168    |       0      |      255      |    31   |   0  |   168   |
        169    |       0      |      255      |    31   |   0  |   169   |
        170    |       0      |      255      |    31   |   0  |   170   |
        171    |       0      |      255      |    31   |   0  |   171   |
        172    |       0      |      255      |    31   |   0  |   172   |
        173    |       0      |      255      |    31   |   0  |   173   |
        174    |       0      |      255      |    31   |   0  |   174   |
        175    |       0      |      255      |    31   |   0  |   175   |
        176    |       0      |      255      |    31   |   0  |   176   |
        177    |       0      |      255      |    31   |   0  |   177   |
        178    |       0      |      255      |    31   |   0  |   178   |
        179    |       0      |      255      |    31   |   0  |   179   |
        180    |       0      |      255      |    31   |   0  |   180   |
        181    |       0      |      255      |    31   |   0  |   181   |
        182    |       0      |      255      |    31   |   1  |   182   |
        183    |       0      |      255      |    31   |   1  |   183   |
        184    |       0      |      255      |    31   |   1  |   184   |
        185    |       0      |      255      |    31   |   1  |   185   |
        186    |       0      |      255      |    31   |   1  |   186   |
        187    |       0      |      255      |    31   |   1  |   187   |
        208    |       2      |      216      |    27   |   0  |   208   |
        232    |       2      |      232      |    29   |   0  |   232   |
        233    |       2      |      232      |    29   |   1  |   232   |
        235    |       2      |      126      |    15   |   0  |   235   |
        240    |       2      |      240      |    30   |   0  |   240   |
        241    |       2      |      240      |    30   |   1  |   240   |
        246    |       2      |      128      |    16   |   0  |   246   |
        247    |       2      |      126      |    15   |   1  |   247   |
        248    |       2      |      130      |    16   |   0  |   248   |
        249    |       2      |      128      |    16   |   1  |   249   |
        250    |       2      |      132      |    16   |   0  |   250   |
        251    |       2      |      130      |    16   |   1  |   251   |
        252    |       2      |      134      |    16   |   0  |   252   |
        253    |       2      |      192      |    24   |   0  |   253   |
        564    |       2      |      248      |    31   |   0  |   255   |
        565    |       2      |      248      |    31   |   1  |   255   |
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersFiaDiagshellDiagCosqQpairEgpMap(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowControllersFiaDiagshellDiagCosqQpairEgpMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

if __name__ == '__main__':
    unittest.main()

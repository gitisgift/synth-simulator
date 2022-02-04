#!/usr/bin/env python
# (c) 2016 DevicePilot Ltd.
# Definitions from https://github.com/OpenMobileAlliance/OMA-LWM2M-DevKit/blob/master/objects/lwm2m-object-definitions.json

objects = {
  "0": {
    "id": 0,
    "name": "LWM2M Security",
    "instancetype": "multiple",
    "mandatory": True,
    "description": "This LWM2M Object provides the keying material of a LWM2M Client appropriate to access a specified LWM2M Server. One Object Instance SHOULD address a LWM2M Bootstrap Server.\n    These LWM2M Object Resources MUST only be changed by a LWM2M Bootstrap Server or Bootstrap from Smartcardand MUST NOT be accessible by any other LWM2M Server.",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "LWM2M  Server URI",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "string",
        "range": "0-255 bytes",
        "units": "",
        "description": "Uniquely identifies the LWM2M Server or LWM2M Bootstrap Server, and is in the form:\n\"coaps://host:port\", where host is an IP address or FQDN, and port is the UDP port of the Server."
      },
      "1": {
        "id": 1,
        "name": "Bootstrap Server",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "boolean",
        "range": "",
        "units": "",
        "description": "Determines if the current instance concerns a LWM2M Bootstrap Server (True) or a standard LWM2M Server (False)"
      },
      "2": {
        "id": 2,
        "name": "Security Mode",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "0-3",
        "units": "",
        "description": "Determines which UDP payload security mode is used\n0: Pre-Shared Key mode\n1: Raw Public Key mode\n2: Certificate mode\n3: NoSec mode"
      },
      "3": {
        "id": 3,
        "name": "Public Key or Identity",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "opaque",
        "range": "",
        "units": "",
        "description": "Stores the LWM2M Client's Certificate (Certificate mode), public key (RPK mode) or PSK Identity (PSK mode). The format is defined in Section E.1.1."
      },
      "4": {
        "id": 4,
        "name": "Server Public Key or Identity",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "opaque",
        "range": "",
        "units": "",
        "description": "Stores the LWM2M Server's or LWM2M Bootstrap Server's Certificate (Certificate mode), public key (RPK mode) or PSK Identity (PSK mode). The format is defined in Section E.1.1."
      },
      "5": {
        "id": 5,
        "name": "Secret Key",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "opaque",
        "range": "",
        "units": "",
        "description": "Stores the secret key or private key of the security mode. The format of the keying material is defined by the security mode in  Section E.1.1. This Resource MUST only be changed by a bootstrap server and MUST NOT be readable by any server."
      },
      "6": {
        "id": 6,
        "name": "SMS Security Mode",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "0-255",
        "units": "",
        "description": "Determines which SMS payload security mode is used (see section 7.2)\n0: Reserved for future use\n1: Secure Packet Structure mode device terminated\n2: Secure Packet Structure mode smartcard terminated\n3: NoSec mode\n255: Proprietary modes"
      },
      "7": {
        "id": 7,
        "name": "SMS Binding Key Parameters",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "opaque",
        "range": "6 bytes",
        "units": "",
        "description": "Stores the KIc, KID, SPI and TAR. The format is defined in Section D.1.2."
      },
      "8": {
        "id": 8,
        "name": "SMS Binding Secret Keys",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "opaque",
        "range": "32-48 bytes",
        "units": "",
        "description": "Stores the values of the keys for the SMS binding. \nThis resource MUST only be changed by a bootstrap server and MUST NOT be readable by any server."
      },
      "9": {
        "id": 9,
        "name": "LWM2M Server SMS Number",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "",
        "units": "",
        "description": "MSISDN used by the LWM2M Client  to send messages to the LWM2M Server via the SMS binding. \nThe LWM2M Client SHALL silently ignore any SMS not originated from unknown MSISDN"
      },
      "10": {
        "id": 10,
        "name": "Short Server ID",
        "operations": "-",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "1-65535",
        "units": "",
        "description": "This identifier uniquely identifies each LWM2M Server configured for the LWM2M Client.\nThis Resource MUST be set when the Bootstrap Server Resource has False value.\nDefault Short Server ID (i.e. 0) MUST NOT be used for identifying the LWM2M Server."
      },
      "11": {
        "id": 11,
        "name": "Client Hold Off Time",
        "operations": "-",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "",
        "units": "s",
        "description": "Relevant information for a Bootstrap Server only.\nThe number of seconds to wait before initiating a Client Initiated Bootstrap once the LWM2M Client has determined it should initiate this bootstrap mode"
      }
    }
  },
  "1": {
    "id": 1,
    "name": "LWM2M Server",
    "instancetype": "multiple",
    "mandatory": True,
    "description": "This LWM2M Objects provides the data related to a LWM2M Server. A Bootstrap Server has no such an Object Instance associated to it.",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "Short Server ID",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "1-65535",
        "units": "",
        "description": "Used as link to associate server Object Instance."
      },
      "1": {
        "id": 1,
        "name": "Lifetime",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "",
        "units": "s",
        "description": "Specify the lifetime of the registration in seconds."
      },
      "2": {
        "id": 2,
        "name": "Default Minimum Period",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "s",
        "description": "The default value the LWM2M Client should use for the Minimum Period of an Observation in the absence of this parameter being included in an Observation.\nIf this Resource doesn't exist, the default value is 1."
      },
      "3": {
        "id": 3,
        "name": "Default Maximum Period",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "s",
        "description": "The default value the LWM2M Client should use for the Maximum Period of an Observation in the absence of this parameter being included in an Observation."
      },
      "4": {
        "id": 4,
        "name": "Disable",
        "operations": "E",
        "instancetype": "single",
        "mandatory": False,
        "type": "",
        "range": "",
        "units": "",
        "description": "If this Resource is executed, this LWM2M Server Object is disabled for a certain period defined in the Disabled Timeout Resource. After receiving 'Execute' operation, LWM2M Client MUST send response of the operation and perform de-registration process, and underlying network connection between the Client and Server MUST be disconnected to disable the LWM2M Server account.\nAfter the above process, the LWM2M Client MUST NOT send any message to the Server and ignore all the messages from the LWM2M Server for the period."
      },
      "5": {
        "id": 5,
        "name": "Disable Timeout",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "s",
        "description": "A period to disable the Server. After this period, the LWM2M Client MUST perform registration process to the Server. If this Resource is not set, a default timeout value is 86400 (1 day)."
      },
      "6": {
        "id": 6,
        "name": "Notification Storing When Disabled or Offline",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": True,
        "type": "boolean",
        "range": "",
        "units": "",
        "description": "If True, the LWM2M Client stores 'Notify' operations to the LWM2M Server while the LWM2M Server account is disabled or the LWM2M Client is offline. After the LWM2M Server account is enabled or the LWM2M Client is online, the LWM2M Client reports the stored 'Notify' operations to the Server.\nIf False, the LWM2M Client discards all the 'Notify' operationsor temporally disables the Observe function while the LWM2M Server is disabled or the LWM2M Client is offline.\nThe default value is True.\nThe maximum number of storing Notification per the Server is up to the implementation."
      },
      "7": {
        "id": 7,
        "name": "Binding",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": True,
        "type": "string",
        "range": "The possible values of Resource are listed in 5.2.1.1",
        "units": "",
        "description": "This Resource defines the transport binding configured for the LWM2M Client.\nIf the LWM2M Client supports the binding specified in this Resource, the LWM2M Client MUST use that for Current Binding and Mode."
      },
      "8": {
        "id": 8,
        "name": "Registration Update Trigger",
        "operations": "E",
        "instancetype": "single",
        "mandatory": True,
        "type": "",
        "range": "",
        "units": "",
        "description": "If this Resource is executed the LWM2M Client MUST perform an 'Update' operation with this LWM2M Server using the Current Transport Binding and Mode."
      }
    }
  },
  "2": {
    "id": 2,
    "name": "LWM2M Access Control",
    "instancetype": "multiple",
    "mandatory": False,
    "description": "Access Control Object is used to check whether the LWM2M Server has access right for performing a operation.",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "Object ID",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "1-65534",
        "units": "",
        "description": "The Object ID and The Object Instance ID are applied for."
      },
      "1": {
        "id": 1,
        "name": "Object Instance ID",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "0-65535",
        "units": "",
        "description": "See Table 14: LWM2M Identifiers."
      },
      "2": {
        "id": 2,
        "name": "ACL",
        "operations": "RW",
        "instancetype": "multiple",
        "mandatory": False,
        "type": "integer",
        "range": "16-bit",
        "units": "",
        "description": "Resource Instance ID MUST be the Short Server ID of a certain LWM2M Server which has an access right.\nResource Instance ID 0 is for default Short Server ID.\nThe Value of the Resource Instance contains the access rights.\nSetting each bit means the LWM2M Server has the access right for that operation. The bit order is specified as below.\n1st lsb: R(Read, Observe, Discover, Write Attributes)\n2nd lsb: W(Write)\n3rd lsb: E(Execute)\n4th lsb: D(Delete)\n5th lsb: C(Create)\nOther bits are reserved for future use"
      },
      "3": {
        "id": 3,
        "name": "Access Control Owner",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "0-65535",
        "units": "",
        "description": "Short Server ID of a certain LWM2M Server. Only this LWM2M Server can manage these Resources of the Object Instance.\nValue MAX_ID=65535 is reserved for the Access Control Object Instances created during Bootstrap procedure."
      }
    }
  },
  "3": {
    "id": 3,
    "name": "Device",
    "instancetype": "single",
    "mandatory": True,
    "description": "This LWM2M Object provides a range of device related information which can be queried by the LWM2M Server, and a device reboot and factory reset function.",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "Manufacturer",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "",
        "description": "Human readable manufacturer name"
      },
      "1": {
        "id": 1,
        "name": "Model Number",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "",
        "description": "A model identifier (manufacturer specified string)"
      },
      "2": {
        "id": 2,
        "name": "Serial Number",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "",
        "description": "Serial Number"
      },
      "3": {
        "id": 3,
        "name": "Firmware Version",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "",
        "description": "Current firmware version"
      },
      "4": {
        "id": 4,
        "name": "Reboot",
        "operations": "E",
        "instancetype": "single",
        "mandatory": True,
        "type": "",
        "range": "",
        "units": "",
        "description": "Reboot the LWM2M Device to restore the Device from unexpected firmware failure."
      },
      "5": {
        "id": 5,
        "name": "Factory Reset",
        "operations": "E",
        "instancetype": "single",
        "mandatory": False,
        "type": "",
        "range": "",
        "units": "",
        "description": "Perform factory reset of the LWM2M Device to make the LWM2M Device have the same configuration as at the initial deployment.\nWhen this Resource is executed, 'De-register' operation  MAY be sent to the LWM2M Server(s) before factory reset of the LWM2M Device."
      },
      "6": {
        "id": 6,
        "name": "Available Power Sources",
        "operations": "R",
        "instancetype": "multiple",
        "mandatory": False,
        "type": "integer",
        "range": "0-7",
        "units": "",
        "description": "0: DC power\n1: Internal Battery\n2: External Battery\n4: Power over Ethernet\n5: USB\n6: AC (Mains) power\n7: Solar"
      },
      "7": {
        "id": 7,
        "name": "Power Source Voltage",
        "operations": "R",
        "instancetype": "multiple",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "mV",
        "description": "Present voltage for each Available Power Sources Resource Instance.\nEach Resource Instance ID MUST map to the value of Available Power Sources Resource."
      },
      "8": {
        "id": 8,
        "name": "Power Source Current",
        "operations": "R",
        "instancetype": "multiple",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "mA",
        "description": "Present current for each Available Power Source"
      },
      "9": {
        "id": 9,
        "name": "Battery Level",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-100",
        "units": "%",
        "description": "Contains the current battery level as a percentage (with a range from 0 to 100). This value is only valid when the value of Available Power Sources Resource is 1."
      },
      "10": {
        "id": 10,
        "name": "Memory Free",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "KB",
        "description": "Estimated current available amount of storage space which can store data and software in the LWM2M Device (expressed in kilobytes)."
      },
      "11": {
        "id": 11,
        "name": "Error Code",
        "operations": "R",
        "instancetype": "multiple",
        "mandatory": True,
        "type": "integer",
        "range": "",
        "units": "",
        "description": "0: No error\n1: Low battery power\n2: External power supply off\n3: GPS module failure\n4: Low received signal strength\n5: Out of memory\n6: SMS failure\n7: IP connectivity failure\n8: Peripheral malfunction\n\nWhen the single Device Object Instance is initiated, there is only one error code Resource Instance whose value is equal to 0 that means no error. When the first error happens, the LWM2M Client changes error code Resource Instance to any non-zero value to indicate the error type. When any other error happens, a new error code Resource Instance is created.\nThis error code Resource MAY be observed by the LWM2M Server. How to deal with LWM2M Client's error report depends on the policy of the LWM2M Server."
      },
      "12": {
        "id": 12,
        "name": "Reset Error Code",
        "operations": "E",
        "instancetype": "single",
        "mandatory": False,
        "type": "",
        "range": "",
        "units": "",
        "description": "Delete all error code Resource Instances and create only one zero-value error code that implies no error."
      },
      "13": {
        "id": 13,
        "name": "Current Time",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "time",
        "range": "",
        "units": "",
        "description": "Current UNIX time of the LWM2M Client.\nThe LWM2M Client should be responsible to increase this time value as every second elapses.\nThe LWM2M Server is able to write this Resource to make the LWM2M Client synchronized with the LWM2M Server."
      },
      "14": {
        "id": 14,
        "name": "UTC Offset",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "",
        "description": "Indicates the UTC offset currently in effect for this LWM2M Device. UTC+X [ISO 8601]."
      },
      "15": {
        "id": 15,
        "name": "Timezone",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "",
        "description": "Indicates in which time zone the LWM2M Device is located, in IANA Timezone (TZ) database format."
      },
      "16": {
        "id": 16,
        "name": "Supported Binding and Modes",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "string",
        "range": "",
        "units": "",
        "description": "Indicates which bindings and modes are supported in the LWM2M Client. The possible values of Resource are combination of \"U\" or \"UQ\" and \"S\" or \"SQ\"."
      }
    }
  },
  "4": {
    "id": 4,
    "name": "Connectivity Monitoring",
    "instancetype": "single",
    "mandatory": False,
    "description": "This LWM2M Object enables monitoring of parameters related to network connectivity.\nIn this general connectivity Object, the Resources are limited to the most general cases common to most network bearers. It is recommended to read the description, which refers to relevant standard development organizations (e.g. 3GPP, IEEE).\nThe goal of the Connectivity Monitoring Object is to carry information reflecting the more up to date values of the current connection for monitoring purposes. Resources such as Link Quality, Radio Signal Strenght, Cell ID are retrieved during connected mode at least for cellular networks.",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "Network Bearer",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "",
        "units": "",
        "description": "Indicates the network bearer used for the current LWM2M communication session from the below network bearer list.\n0~20 are Cellular Bearers\n0: GSM cellular network\n1: TD-SCDMA cellular network\n2: WCDMA cellular network\n3: CDMA2000 cellular network\n4: WiMAX cellular network\n5: LTE-TDD cellular network\n6: LTE-FDD cellular network\n7~20: Reserved for other type cellular network\n21~40 are Wireless Bearers\n21: WLAN network\n22: Bluetooth network\n23: IEEE 802.15.4 network\n24~40: Reserved for other type local wireless network\n41~50 are Wireline Bearers\n41: Ethernet\n42: DSL\n43: PLC\n44~50: reserved for others type wireline networks."
      },
      "1": {
        "id": 1,
        "name": "Available Network Bearer",
        "operations": "R",
        "instancetype": "multiple",
        "mandatory": True,
        "type": "integer",
        "range": "",
        "units": "",
        "description": "Indicates list of current available network bearer. Each Resource Instance has a value from the network bearer list."
      },
      "2": {
        "id": 2,
        "name": "Radio Signal Strength",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "",
        "units": "dBm",
        "description": "This node contains the average value of the received signal strength indication used in the current network bearer in case Network Bearer Resource indicates a Cellular Network (RXLEV range 0..64) 0 is < 110dBm, 64 is > -48 dBm).\nRefer to [3GPP 44.018] for more details on Network Measurement Report encoding and [3GPP 45.008] or for Wireless Networks refer to the appropriate wireless standard."
      },
      "3": {
        "id": 3,
        "name": "Link Quality",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "",
        "description": "This contains received link quality  e.g., LQI for IEEE 802.15.4, (Range (0..255)), RxQual Downlink (for GSM range is 0..7).\nRefer to [3GPP 44.018] for more details on Network Measurement Report encoding."
      },
      "4": {
        "id": 4,
        "name": "IP Addresses",
        "operations": "R",
        "instancetype": "multiple",
        "mandatory": True,
        "type": "string",
        "range": "",
        "units": "",
        "description": "The IP addresses assigned to the connectivity interface. (e.g. IPv4, IPv6, etc.)"
      },
      "5": {
        "id": 5,
        "name": "Router IP Addresse",
        "operations": "R",
        "instancetype": "multiple",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "",
        "description": "The IP address of the next-hop IP router.\nNote: This IP Address doesn't indicate the Server IP address."
      },
      "6": {
        "id": 6,
        "name": "Link Utilization",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-100",
        "units": "%",
        "description": "The average utilization of the link to the next-hop IP router in %."
      },
      "7": {
        "id": 7,
        "name": "APN",
        "operations": "R",
        "instancetype": "multiple",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "",
        "description": "Access Point Name in case Network Bearer Resource is a Cellular Network."
      },
      "8": {
        "id": 8,
        "name": "Cell ID",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "",
        "description": "Serving Cell ID in case Network Bearer Resource is a Cellular Network.\nAs specified in TS [3GPP 23.003] and in [3GPP. 24.008]. Range (0..65535) in GSM/EDGE\nUTRAN Cell ID has a length of 28 bits.\nCell Identity  in WCDMA/TD-SCDMA. Range: (0..268435455).\nLTE Cell ID has a length of 28 bits.\nParameter definitions in [3GPP 25.331]."
      },
      "9": {
        "id": 9,
        "name": "SMNC",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "%",
        "description": "Serving Mobile Network Code. In case Network Bearer Resource has 0(cellular network). Range (0..999).\nAs specified in TS [3GPP 23.003]."
      },
      "10": {
        "id": 10,
        "name": "SMCC",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "",
        "description": "Serving Mobile Country Code. In case Network Bearer Resource has 0 (cellular network). Range (0..999).\nAs specified in TS [3GPP 23.003]."
      }
    }
  },
  "5": {
    "id": 5,
    "name": "Firmware Update",
    "instancetype": "single",
    "mandatory": False,
    "description": "This LWM2M Object enables management of firmware which is to be updated. This Object includes installing firmware package, updating firmware, and performing actions after updating firmware.",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "Package",
        "operations": "W",
        "instancetype": "single",
        "mandatory": True,
        "type": "opaque",
        "range": "",
        "units": "",
        "description": "Firmware package"
      },
      "1": {
        "id": 1,
        "name": "Package URI",
        "operations": "W",
        "instancetype": "single",
        "mandatory": True,
        "type": "string",
        "range": "0-255 bytes",
        "units": "",
        "description": "URI from where the device can download the firmware package by an alternative mechanism. As soon the device has received the Package URI it performs the download at the next practical opportunity."
      },
      "2": {
        "id": 2,
        "name": "Update",
        "operations": "E",
        "instancetype": "single",
        "mandatory": True,
        "type": "",
        "range": "",
        "units": "",
        "description": "Updates firmware by using the firmware package stored in Package, or, by using the firmware downloaded from the Package URI.\nThis Resource is only executable when the value of the State Resource is Downloaded."
      },
      "3": {
        "id": 3,
        "name": "State",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "1-3",
        "units": "",
        "description": "Indicates current state with respect to this firmware update. This value is set by the LWM2M Client.\n1: Idle (before downloading or after updating)\n2: Downloading (The data sequence is on the way)\n3: Downloaded\nIf writing the firmware package to Package Resource is done, or, if the device has downloaded the firmware package from the Package URI the state changes to Downloaded.\nIf writing an empty string to Package Resource is done or writing an empty string to Package URI is done, the state changes to Idle.\nIf performing the Update Resource failed, the state remains at Downloaded.\nIf performing the Update Resource was successful, the state changes from Downloaded to Idle."
      },
      "4": {
        "id": 4,
        "name": "Update Supported Objects",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "boolean",
        "range": "",
        "units": "",
        "description": "If this value is True, the LWM2M Client MUST inform the registered LWM2M Servers of Objects and Object Instances parameter by sending an Update or Registration message after the firmware update operation at the next practical opportunity if supported Objects in the LWM2M Client have changed, in order for the LWM2M Servers to promptly manage newly installed Objects.\nIf False, Objects and Object Instances parameter MUST be reported at the next periodic Update message.\nThe default value is False."
      },
      "5": {
        "id": 5,
        "name": "Update Result",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "0-6",
        "units": "",
        "description": "Contains the result of downloading or updating the firmware\n0: Default value. Once the updating process is initiated, this Resource SHOULD be reset to default value.\n1: Firmware updated successfully,\n2: Not enough storage for the new firmware package.\n3. Out of memory during downloading process.\n4: Connection lost during downloading process.\n5: CRC check failure for new downloaded package.\n6: Unsupported package type.\n7: Invalid URI\nThis Resource MAY be reported by sending Observe operation."
      }
    }
  },
  "6": {
    "id": 6,
    "name": "Location",
    "instancetype": "single",
    "mandatory": False,
    "description": "This LWM2M Objects provide a range of device related information which can be queried by the LWM2M Server, and a device reboot and factory reset function.",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "Latitude",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "string",
        "range": "",
        "units": "Deg",
        "description": "The decimal notation of latitude, e.g. -43.5723 [World Geodetic System 1984]."
      },
      "1": {
        "id": 1,
        "name": "Longitude",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "string",
        "range": "",
        "units": "Deg",
        "description": "The decimal notation of longitude, e.g. 153.21760 [World Geodetic System 1984]."
      },
      "2": {
        "id": 2,
        "name": "Altitude",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "m",
        "description": "The decimal notation of altitude in meters above sea level."
      },
      "3": {
        "id": 3,
        "name": "Uncertainty",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "m",
        "description": "The accuracy of the position in meters."
      },
      "4": {
        "id": 4,
        "name": "Velocity",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "opaque",
        "range": "",
        "units": "Refers to 3GPP GAD specs",
        "description": "The velocity of the device as defined in 3GPP 23.032 GAD specification. This set of values may not be available if the device is static."
      },
      "5": {
        "id": 5,
        "name": "Timestamp",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "time",
        "range": "0-6",
        "units": "",
        "description": "The timestamp of when the location measurement was performed."
      }
    }
  },
  "7": {
    "id": 7,
    "name": "Connectivity Statistics",
    "instancetype": "single",
    "mandatory": False,
    "description": "This LWM2M Objects enables client to collect statistical information and enables the LWM2M Server to retrieve these information, set the collection duration and reset the statistical parameters.",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "SMS Tx Counter",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "",
        "description": "Indicate the total number of SMS successfully transmitted during the collection period."
      },
      "1": {
        "id": 1,
        "name": "SMS Rx Counter",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "",
        "description": "Indicate the total number of SMS successfully received during the collection period."
      },
      "2": {
        "id": 2,
        "name": "Tx Data",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "Kilo-Bytes",
        "description": "Indicate the total amount of data transmitted during the collection period."
      },
      "3": {
        "id": 3,
        "name": "Rx Data",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "Kilo-Bytes",
        "description": "Indicate the total amount of data received during the collection period."
      },
      "4": {
        "id": 4,
        "name": "Max Message Size",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "Byte",
        "description": "The maximum message size that is used during the collection period."
      },
      "5": {
        "id": 5,
        "name": "Average Message Size",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "",
        "units": "Byte",
        "description": "The average message size that is used during the collection period."
      },
      "6": {
        "id": 6,
        "name": "StartOrReset",
        "operations": "E",
        "instancetype": "single",
        "mandatory": True,
        "type": "",
        "range": "",
        "units": "",
        "description": "Start to collect information or reset all other Resources to zeros in this Object. For example, the first time this Resource is executed, the client starts to collect information. The second time this Resource is executed, the values of Resource 0~5 are reset to 0."
      }
    }
  },
  "8": {
    "id": 8,
    "name": "Lock and Wipe",
    "instancetype": "single",
    "mandatory": False,
    "description": "This LWM2M objects provides the resources needed to perform the lock and wipe operations.",
    "resourcedefs": {
			"0": {
        "id": 0,
        "name": "State",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "0-2",
        "units": "",
        "description": "State of the device:\n0: unlocked state\nNormal operation.\n1: partially locked state\nTo render the device inoperable the device has been partially locked. The 'lock target' resource allows specifying the target(s) for this operation.\n2: fully locked state\nTo render the device fully inoperable the device has been fully locked."
			},
			"1": {
        "id": 1,
        "name": "Lock target",
        "operations": "W",
        "instancetype": "multiple",
        "mandatory": True,
        "type": "string",
        "range": "",
        "units": "",
        "description": "To specify one or several targets for the lock operation. This allows partially locking the device by selecting specific components or interfaces to be locked."
			},
			"2": {
        "id": 2,
        "name": "Wipe item",
        "operations": "R",
        "instancetype": "multiple",
        "mandatory": False,
        "type": "string",
        "range": "",
        "units": "",
        "description": "Indicates which data can be wiped from the device. This resource could be e.g. representing a directory."
			},
			"3": {
        "id": 3,
        "name": "Wipe",
        "operations": "E",
        "instancetype": "single",
        "mandatory": True,
        "type": "",
        "range": "",
        "units": "",
        "description": "To permanently erase data from the device."
			},
			"4": {
        "id": 4,
        "name": "Wipe target",
        "operations": "W",
        "instancetype": "multiple",
        "mandatory": True,
        "type": "string",
        "range": "",
        "units": "",
        "description": "To specify one or several targets for the wipe operation. This allows selecting specific data, or, memory areas for the wipe operation."
			},
			"5": {
        "id": 5,
        "name": "Lock or Wipe Operation Result",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "0-8",
        "units": "",
        "description": "Contains the result of a lock and wipe operation\n0: Default\n1: Partially Lock operation successful\n2: Fully Lock operation successful\n3: Unlock operation successful\n4: Wipe operation successful\n5: Partially Lock operation failed\n6: Fully Lock operation failed\n7: Unlock operation failed\n8: Wipe operation failed\nThis Resource MAY be reported by sending Observe operation."
			}
		}
  },
  "9": {
    "id": 9,
    "name": "Software Update",
    "instancetype": "multiple",
    "mandatory": False,
    "description": "This LWM2M Objects provides the resources needed to perform software management on the device. Each software component is managed via a dedicated Software Management Object instance.",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "PkgName",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "string",
        "range": "0-255 bytes",
        "units": "",
        "description": "Name of the software package."
      },
      "1": {
        "id": 1,
        "name": "PkgVersion",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "string",
        "range": "0-255 bytes",
        "units": "",
        "description": "Version of the software package."
      },
      "2": {
        "id": 2,
        "name": "Package",
        "operations": "W",
        "instancetype": "single",
        "mandatory": True,
        "type": "opaque",
        "range": "",
        "units": "",
        "description": "Software package."
      },
      "3": {
        "id": 3,
        "name": "Package URI",
        "operations": "W",
        "instancetype": "single",
        "mandatory": True,
        "type": "string",
        "range": "0-255 bytes",
        "units": "",
        "description": "URI from where the device can download the software package by an alternative mechanism. As soon as the device has received the Package URI it performs the download at the next practical opportunity."
      },
      "4": {
        "id": 4,
        "name": "Install",
        "operations": "E",
        "instancetype": "single",
        "mandatory": True,
        "type": "",
        "range": "",
        "units": "",
        "description": "Installs software from the package either stored in Package resource or downloaded from the Package URI. This Resource is only executable when the value of the State Resource is DELIVERED."
      },
      "5": {
        "id": 5,
        "name": "Checkpoint",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "objlnk",
        "range": "",
        "units": "",
        "description": "Link to a 'Checkpoint' object which allows to specify conditions/dependencies for a software update. E.g. power connected, sufficient memory, target system."
      },
      "6": {
        "id": 6,
        "name": "Uninstall",
        "operations": "E",
        "instancetype": "single",
        "mandatory": True,
        "type": "",
        "range": "",
        "units": "",
        "description": "Uninstalls the software package, removes it from the Device if present and set Update State back to INITIAL state."
      },
      "7": {
        "id": 7,
        "name": "Update State",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "1-5",
        "units": "",
        "description": "Indicates current state with respect to this software update. This value is set by the LWM2M Client.\n1: INITIAL Before downloading. (see 5.1.2.1)\n2: DOWNLOAD STARTED The downloading process has started and is on-going. (see 5.1.2.2)\n3: DOWNLOADED The package has been completely downloaded (see 5.1.2.3)\n4: DELIVERED In that state, the package has been correctly downloaded and is ready to be installed. (see 5.1.2.4)\nIf executing the Install Resource failed, the state remains at DELIBERED.\nIf executing the Install Resource was successful, the state changes from DELIVERED to INSTALLED.\nAfter executing the UnInstall Resource, the state changes to INITIAL.\n5: INSTALLED In that state the software is correctly installed and can be activated or deactivated according to the Activation State Machine. (see 5.1.2.5)"
      },
      "8": {
        "id": 8,
        "name": "Update Supported Objects",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "boolean",
        "range": "",
        "units": "",
        "description": "If this value is True, the LWM2M Client MUST inform the registered LWM2M Servers of Objects and Object Instances parameter by sending an Update or Registration message after the software update operation at the next practical opportunity if supported Objects in the LWM2M Client have changed, in order for the LWM2M Servers to promptly manage newly installed Objects.\nIf False, Objects and Object Instances parameter MUST be reported at the next periodic Update message.\nThe default value is False."
      },
      "9": {
        "id": 9,
        "name": "Update Result",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "integer",
        "range": "0-10",
        "units": "",
        "description": "Contains the result of downloading or installing/uninstalling the software\n0: Initial value. Prior to download any new package in the Device, Update Result MUST be reset to this initial value. One side effect of executing the Uninstall resource is to reset Update Result to this initial value '0'.\n1: Downloading. The package downloading process is on-going.\n2: Software d successfully installed.\n3: Not enough storage for the new software package.\n4: Out of memory during downloading process.\n5: Connection lost during downloading process.\n6: Package integrity check failure.\n7: Unsupported package type.\n8: Invalid URI\n9: Device defined update error\n10: Software installation failure\nThis Resource MAY be reported by sending Observe operation."
      },
      "10": {
        "id": 10,
        "name": "Activate",
        "operations": "E",
        "instancetype": "single",
        "mandatory": True,
        "type": "",
        "range": "",
        "units": "",
        "description": "This action activates the software previously successfully installed (the Package Installation State Machine is currently in the INSTALLED state)"
      },
      "11": {
        "id": 11,
        "name": "Deactivate",
        "operations": "E",
        "instancetype": "single",
        "mandatory": True,
        "type": "",
        "range": "",
        "units": "",
        "description": "This action deactivates software if the Package Installation State Machine is currently in the INSTALLED state."
      },
      "12": {
        "id": 12,
        "name": "Activation State",
        "operations": "R",
        "instancetype": "single",
        "mandatory": True,
        "type": "boolean",
        "range": "",
        "units": "",
        "description": "Indicates the current activation state of this software:\n0: DISABLED Activation State is DISABLED if the Software Activation State Machine is in the INACTIVE state or not alive.\n1: ENABLED Activation State is ENABLED only if the Software Activation State Machine is in the ACTIVE state"
      },
      "13": {
        "id": 13,
        "name": "Package Settings",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "objlnk",
        "range": "",
        "units": "",
        "description": "Link to 'Package Settings' object which allows to modify at any time software configuration settings. This is an application specific object.\nNote: OMA might provide a template for a Package Settings object in a future release of this specification."
      }
    }
  },
  "32301": {    # !!! CONNECT2's proprietary parameter names
    "id": 32301,
    "name": "Connect2",
    "instancetype": "multiple",
    "mandatory": False,
    "description": "Connect 2 specific parameters",
    "resourcedefs": {
      "0": {
        "id": 0,
        "name": "Mote ID",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "1": {
        "id": 1,
        "name": "Mote Status",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "2": {
        "id": 2,
        "name": "Network Key",
        "operations": "W",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "3": {
        "id": 3,
        "name": "Firmware Version",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "string",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "4": {
        "id": 4,
        "name": "Publish Interval",
        "operations": "RW",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "5": {
        "id": 5,
        "name": "Input 1",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "6": {
        "id": 5,
        "name": "Input 2",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "7": {
        "id": 7,
        "name": "Input 3",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "8": {
        "id": 8,
        "name": "Input 4",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "9": {
        "id": 9,
        "name": "Transmit RSSI",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "10": {
        "id": 10,
        "name": "Receive RSSI",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      },
      "11": {
        "id": 11,
        "name": "Availability",
        "operations": "R",
        "instancetype": "single",
        "mandatory": False,
        "type": "integer",
        "range": "0-255 bytes",
        "units": "",
        "description": ""
      }
    }
  }

}


def doIndex(obj, num):
    # Looks up a numerical key in a dict
    if not obj:
        return None
    s = str(num)
    if s in obj:
        return obj[s]
    return None

def lookupName(objectID, resourceID=None):
    """LWM2M ids are triples e.g. 1/0/0, but the middle one is the instance number. So it's objectID/instanceNum/resourceID"""
    r1 = doIndex(objects, objectID)
    if not r1:
        return "UNKNOWN_LWM2M_OBJECT_ID"
    s1 = r1["name"]

    if resourceID==None:
        return s1.replace(" ","_")
    
    r2 = doIndex(r1["resourcedefs"], resourceID)
    if not r2:
        s2 = "UNKNOWN_LWM2M_RESOURCE_ID"
    else:
        s2 = r2["name"]
    s = s1 + "_" + s2
    s = s.replace(" ","_")
    return s

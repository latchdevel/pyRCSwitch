"""
   Unit tests for pyRCSwitch
   Python module to wrap the RCSwitch Common Library

   See: https://github.com/latchdevel/pyRCSwitch

   Copyright (c) 2024 Jorge Rivera. All right reserved.
   License GNU Lesser General Public License v3.0.
"""

import unittest

from pyRCSwitch import RCSwitch

testRCSwitchPiCodes = [
  {
     "picode": {'conrad_rsl_switch': {'id': 1, 'unit': 2, 'state': 'on'}},
     "command": "On", # unused
     "protocol": 2,
     "length": 650,
     "value": 2384640512,
     "bits": 32,
     "pulses": [1300, 650, 650, 1300, 650, 1300, 650, 1300, 1300, 650, 1300, 650, 1300, 650, 650, 1300, 650, 1300, 650, 1300, 1300, 650, 650, 1300, 650, 1300, 650, 1300, 1300, 650, 650, 1300, 1300, 650, 650, 1300, 1300, 650, 1300, 650, 1300, 650, 650, 1300, 1300, 650, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 6500]
  },
  {
     "picode": {'conrad_rsl_switch': {'id': 1, 'unit': 2, 'state': 'off'}},
     "command": "Off", # unused
     "protocol": 2,
     "length": 650,
     "value": 2166536704,
     "bits": 32,
     "pulses": [1300, 650, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 1300, 650, 650, 1300, 650, 1300, 1300, 650, 650, 1300, 650, 1300, 650, 1300, 1300, 650, 650, 1300, 1300, 650, 650, 1300, 1300, 650, 1300, 650, 1300, 650, 650, 1300, 1300, 650, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 1300, 650, 6500]
  },
]

testRCSwitchCodes = [
  {
     "sliding": ["11111", "00010"],
     "command": "On",
     "protocol": 1,
     "length": 350,
     "value": 5393,
     "bits": 24,
     "binary": "000000000001010100010001",
     "tri-state": "00000FFF0F0F",
     "pulses": [350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 10850]
  },
  {
     "sliding": ["11111", "00010"],
     "command": "Off",
     "protocol": 1,
     "length": 350,
     "value": 5396,
     "bits": 24,
     "binary": "000000000001010100010100",
     "tri-state": "00000FFF0FF0",
     "pulses": [350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 10850]
  },
]

testRCSwitchTypeD = [
  {
     "family-device": ['d', 2], # {'protocols': [{'arctech_screen_old': {'id': 26, 'unit': 0, 'state': 'up'}}, {'arctech_switch_old': {'id': 26, 'unit': 0, 'state': 'on'}}]}
     "command": "On",
     "protocol": 1,
     "length": 360,
     "value": 4433,
     "bits": 24,
     "pulses": [360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 1080, 360, 360, 1080, 360, 1080, 360, 1080, 1080, 360, 360, 1080, 1080, 360, 360, 1080, 1080, 360, 360, 1080, 360, 1080, 360, 1080, 1080, 360, 360, 11160]
  },
  {
     "family-device": ['d', 2], # {'protocols': [{'arctech_screen_old': {'id': 26, 'unit': 0, 'state': 'down'}}, {'arctech_switch_old': {'id': 26, 'unit': 0, 'state': 'off'}}]}
     "command": "Off",
     "protocol": 1,
     "length": 360,
     "value": 4436,
     "bits": 24,
     "pulses": [360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 360, 1080, 1080, 360, 360, 1080, 360, 1080, 360, 1080, 1080, 360, 360, 1080, 1080, 360, 360, 1080, 1080, 360, 360, 1080, 1080, 360, 360, 1080, 360, 1080, 360, 11160]
  },
]

testRCSwitchTypeCIntertechno = [
  {
     "family-group-device": ['d', 3, 2],
     "command": "On",
     "protocol": 1,
     "length": 350,
     "value": 5259541,
     "bits": 24,
     "pulses": [350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 10850]
  },
  { 
     "family-group-device": ['d', 3, 2],
     "command": "Off",
     "protocol": 1,
     "length": 350,
     "value": 5259540,
     "bits": 24,
     "pulses": [350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 10850]
  },
]

class tests_pyRCSwitch(unittest.TestCase):
   
   myRCSwitch = RCSwitch()

   def test_moduleVersion(self):
      import pyRCSwitch as _pyRCSwitch
      result = _pyRCSwitch.__version__
      self.assertIsInstance(result,str)

   def test_RCSwitchObjectInstance(self):
      result = self.myRCSwitch
      self.assertIsInstance(result, RCSwitch)

   def test_RCSwitchSendSliding(self):
      for code in testRCSwitchCodes:
         if code["command"] == "On":
            command = self.myRCSwitch.switchOn
         else:
            command = self.myRCSwitch.switchOff
         with self.subTest("test_RCSwitch.switch{}({})".format(code["command"],code["sliding"])):
            self.myRCSwitch.setProtocol(code["protocol"],code["length"])
            self.assertEqual(command(code["sliding"][0],code["sliding"][1]),code["pulses"])

   def test_RCSwitchSendTypeD(self):
      for code in testRCSwitchTypeD:
         if code["command"] == "On":
            command = self.myRCSwitch.switchOn
         else:
            command = self.myRCSwitch.switchOff
         with self.subTest("test_RCSwitch.switch{}({})".format(code["command"],code["family-device"])):
            self.myRCSwitch.setProtocol(code["protocol"],code["length"])
            self.assertEqual(command(code["family-device"][0],code["family-device"][1]),code["pulses"])

   def test_RCSwitchSendTypeCIntertechno(self):
      for code in testRCSwitchTypeCIntertechno:
         if code["command"] == "On":
            command = self.myRCSwitch.switchOn
         else:
            command = self.myRCSwitch.switchOff
         with self.subTest("test_RCSwitch.switch{}({})".format(code["command"],code["family-group-device"])):
            self.myRCSwitch.setProtocol(code["protocol"],code["length"])
            self.assertEqual(command(code["family-group-device"][0],code["family-group-device"][1],code["family-group-device"][2]),code["pulses"])

   def test_RCSwitchSendCodeValue(self):
      for code in testRCSwitchCodes:
         with self.subTest("test_RCSwitch.send({},{})".format(code["value"],code["bits"])):
            self.myRCSwitch.setProtocol(code["protocol"],code["length"])
            self.assertEqual(self.myRCSwitch.send(code["value"],code["bits"]),code["pulses"])

   def test_RCSwitchSendPiCodeValue(self):
      for code in testRCSwitchPiCodes:
         with self.subTest("test_RCSwitch.send({},{})".format(code["value"],code["bits"])):
            self.myRCSwitch.setProtocol(code["protocol"],code["length"])
            self.assertEqual(self.myRCSwitch.send(code["value"],code["bits"]),code["pulses"])

   def test_RCSwitchSendCodeBinary(self):
      for code in testRCSwitchCodes:
         with self.subTest("test_RCSwitch.send(\"{}\")".format(code["binary"])):
            self.myRCSwitch.setProtocol(code["protocol"],code["length"])
            self.assertEqual(self.myRCSwitch.send(code["binary"]),code["pulses"])

   def test_RCSwitchSendCodeTriState(self):
      for code in testRCSwitchCodes:
         with self.subTest("test_RCSwitch.sendTriState(\"{}\")".format(code["tri-state"])):
            self.myRCSwitch.setProtocol(code["protocol"],code["length"])
            self.assertEqual(self.myRCSwitch.sendTriState(code["tri-state"]),code["pulses"])

   def test_RCSwitchDecode(self):
      for code in testRCSwitchPiCodes + testRCSwitchCodes + testRCSwitchTypeCIntertechno + testRCSwitchTypeD:
         with self.subTest("test_RCSwitch.decode([pulse_list])"):
            self.assertTrue(self.myRCSwitch.decodePulseTrain(code["pulses"]))
            self.assertEqual(self.myRCSwitch.getReceivedProtocol(),code["protocol"])
            self.assertEqual(self.myRCSwitch.getReceivedDelay(),code["length"])
            self.assertEqual(self.myRCSwitch.getReceivedBitlength(),code["bits"])
            self.assertEqual(self.myRCSwitch.getReceivedValue(),code["value"])
            self.assertEqual(self.myRCSwitch.getReceivedRawdata(),code["pulses"])

if __name__ == '__main__':
   unittest.main()
# pyRCSwitch
Python C++ extension module to wrap the **RCSwitch Common Library**.

Works on any **libc++** compatible system with Python v3.7 or higher, such as macOS, FreeBSD, Linux, and even Windows.

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build tests](https://github.com/latchdevel/pyRCSwitch/actions/workflows/BuildTests.yml/badge.svg)](https://github.com/latchdevel/pyRCSwitch/actions/workflows/BuildTests.yml)

The [RCSwitch Common Library](https://github.com/latchdevel/rc-switch-lib) simulates capturing and reproducing operation codes of radio control devices like the popular low cost power outlet sockets, which works on the 315Mhz or 433MHz frequency in AM ASK/OOK modulation.
Its main use is to **encode** RC codes into pulse trains and **decode** pulse trains into RC codes, based on some supported protocols.

There are other similar projects that support a large number of protocols, including some very complex ones, with a large number of pulses, such as [PiCode](https://github.com/latchdevel/PiCode). However, RCSwitch is very popular for its simplicity and ease of use.

## Build and install
Package installation builds the C++ extension module, so some OS tools are required like these packages on Debian-based Linux systems:
- Python3 development tools: `python3-dev`
- C++ compiler suite: `build-essential`
- CMake make system: `cmake`
- Git version control system: `git`

### Install by "setuptools" on user location
Require **setuptools** Python module, which can be installed in several ways:
   - Install via OS package manager: `apt install python3-setuptools`
   - Or install via **pip** Python package manager:
     - Install pip: `apt install python3-pip` and `pip install setuptools`

```
git clone --recursive https://github.com/latchdevel/pyRCSwitch
cd pyRCSwitch
python3 setup.py develop --user
```
Note the `--recursive` option which is needed for **pybind11** and **rc-switch-lib** submodules.

### Install by "pip" on virtual environment
Require **venv** Python module, which can be installed via OS package manager: `apt install python3-venv`

```
python3 -m venv pyRCSwitch_env
source pyRCSwitch_env/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -v git+https://github.com/latchdevel/pyRCSwitch.git
```

## Tests
pyRCSwitch provides a unit tests module to verify its correct operation: `python3 -m unittest discover -v pyRCSwitch`

```
python3 -m unittest discover -v pyRCSwitch 
test_RCSwitchDecode (tests_pyRCSwitch.test_pyRCSwitch) ... ok
test_RCSwitchObjectInstance (tests_pyRCSwitch.test_pyRCSwitch) ... ok
test_RCSwitchSendCodeBinary (tests_pyRCSwitch.test_pyRCSwitch) ... ok
test_RCSwitchSendCodeTriState (tests_pyRCSwitch.test_pyRCSwitch) ... ok
test_RCSwitchSendCodeValue (tests_pyRCSwitch.test_pyRCSwitch) ... ok
test_RCSwitchSendPiCodeValue (tests_pyRCSwitch.test_pyRCSwitch) ... ok
test_RCSwitchSendSliding (tests_pyRCSwitch.test_pyRCSwitch) ... ok
test_RCSwitchSendTypeCIntertechno (tests_pyRCSwitch.test_pyRCSwitch) ... ok
test_RCSwitchSendTypeD (tests_pyRCSwitch.test_pyRCSwitch) ... ok
test_moduleVersion (tests_pyRCSwitch.test_pyRCSwitch) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
```

## Usage
Example of encode and decode RC command for **switch on** "11111", "00010" (Type B with two rotary/sliding switches):
```python
>>> from pyRCSwitch import RCSwitch
>>> mySwitch = RCSwitch()
>>> 
>>> pulse_list = mySwitch.switchOn("11111", "00010") # Generate a pulse train from an RC command
>>> pulse_list
[350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 1050, 350, 1050, 350, 1050, 1050, 350, 350, 10850]
>>> 
>>> mySwitch.decodePulseTrain(pulse_list) # Try to pulse train decode
True
>>> mySwitch.getReceivedValue() # Get RC code value
5393
>>> mySwitch.getReceivedBitlength() # Get RC code bit length
24
>>> mySwitch.getReceivedProtocol() # Get RC code protocol
1
>>> mySwitch.send(5393,24) == pulse_list # Verify that RC code value obtained is the same as generated pulse train
True
>>> 
```

It can be used together with [pyPiCode](https://github.com/latchdevel/pyPiCode) to perform cross encoding and decoding by exchanging pulse trains.

Example of RC code generation for **switch off** via decoding and re-encoding using **pyPiCode** library.
```python
>>> import pypicode as picode
>>> 
>>> from pyRCSwitch import RCSwitch
>>> mySwitch = RCSwitch()
>>> 
>>> picode.decodePulseTrain( mySwitch.switchOn("11111", "00010") ) # <---- Same RC command
{'protocols': [{'arctech_screen_old': {'id': 14, 'unit': 0, 'state': 'up'}}, {'arctech_switch_old': {'id': 14, 'unit': 0, 'state': 'on'}}, {'beamish_switch': {'id': 21, 'unit': -1}}, {'elro_800_switch': {'systemcode': 31, 'unitcode': 8, 'state': 'on'}}, {'rev1_switch': {'id': 'F2', 'unit': 62, 'state': 'off'}}]}
>>> 
>>> mySwitch.decodePulseTrain( picode.encodeToPulseTrainByName('arctech_switch_old', {'id': 14, 'unit': 0, 'state': 'off'}) ) # <---- Set 'off' here
True
>>> mySwitch.getReceivedValue() # Get RC code value for switch off
5396
>>> mySwitch.getReceivedBitlength()
24
>>> mySwitch.getReceivedProtocol()
1
>>> mySwitch.send(5396,24) == mySwitch.switchOff("11111", "00010") # Verify that RC code obtained is the same as that for switch off
True
>>> picode.pulseTrainToString( mySwitch.send(5396,24) ) # Converts RC code value to 'picode' string format
'c:01010101010101010101011001100110010101100110010102;p:350,1050,10850@'
```

# License
Copyright (c) 2024 Jorge Rivera. All right reserved.

License GNU Lesser General Public License v3.0.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

See the [LICENSE](LICENSE.txt) file for license rights and limitations (lgpl-3.0).
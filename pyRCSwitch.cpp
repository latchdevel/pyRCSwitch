/*
   pyRCSwitch
   Python module to wrap the RCSwitch Common Library
  
   See: https://github.com/latchdevel/pyRCSwitch
  
   Copyright (c) 2024 Jorge Rivera. All right reserved.
   License GNU Lesser General Public License v3.0.
*/

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "libs/rc-switch-lib/RCSwitch.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

PYBIND11_MODULE(pyRCSwitch, module) {

   module.doc() = "Python module to wrap the RCSwitch Common Library";

   py::class_<RCSwitch>(module, "RCSwitch")
      .def(py::init())

      .def("switchOn", static_cast<pulse_list_t(RCSwitch::*)(int, int)> (&RCSwitch::switchOn), "Switch a remote switch on (Type B with two rotary/sliding switches)")
      .def("switchOn", static_cast<pulse_list_t(RCSwitch::*)(const char*, int)>(&RCSwitch::switchOn), "Deprecated. Switch a remote switch on (Type A with 10 pole DIP switches)")
      .def("switchOn", static_cast<pulse_list_t(RCSwitch::*)(char, int, int)>(&RCSwitch::switchOn), "Switch a remote switch on (Type C Intertechno)")
      .def("switchOn", static_cast<pulse_list_t(RCSwitch::*)(const char*, const char*)>(&RCSwitch::switchOn), "Switch a remote switch on (Type A with 10 pole DIP switches)")
      .def("switchOn", static_cast<pulse_list_t(RCSwitch::*)(char, int)>(&RCSwitch::switchOn), "Switch a remote switch on (Type D REV)")

      .def("switchOff", static_cast<pulse_list_t(RCSwitch::*)(int, int)>(&RCSwitch::switchOff), "Switch a remote switch off (Type B with two rotary/sliding switches)")
      .def("switchOff", static_cast<pulse_list_t(RCSwitch::*)(const char*, int)>(&RCSwitch::switchOff), "Deprecated. Switch a remote switch off (Type A with 10 pole DIP switches)")
      .def("switchOff", static_cast<pulse_list_t(RCSwitch::*)(char, int, int)>(&RCSwitch::switchOff), "Switch a remote switch off (Type C Intertechno)")
      .def("switchOff", static_cast<pulse_list_t(RCSwitch::*)(const char*, const char*)>(&RCSwitch::switchOff), "Switch a remote switch off (Type A with 10 pole DIP switches)")
      .def("switchOff", static_cast<pulse_list_t(RCSwitch::*)(char, int)>(&RCSwitch::switchOff), "Switch a remote switch off (Type D REV)")

      .def("sendTriState", &RCSwitch::sendTriState, "Transmit a tristate code word consisting of the letter 0, 1, F")
      .def("send", static_cast<pulse_list_t(RCSwitch::*)(unsigned long code, unsigned int)>(&RCSwitch::send), "Transmit the first 'length' bits of the integer 'code'")
      .def("send", static_cast<pulse_list_t(RCSwitch::*)(const char*)>(&RCSwitch::send), "Transmit a binary code word consisting of the letter 0, 1")

      .def("available", &RCSwitch::available, "Returns 'True' when a pulse train is successfully decoded")
      .def("resetAvailable", &RCSwitch::resetAvailable, "Reset pulse train decoding state to 'False'")

      .def("getReceivedValue", &RCSwitch::getReceivedValue, "Returns code value when successfully decoded")
      .def("getReceivedBitlength", &RCSwitch::getReceivedBitlength, "Returns code length in bits when successfully decoded")
      .def("getReceivedDelay", &RCSwitch::getReceivedDelay, "Returns code length in bits when successfully decoded")
      .def("getReceivedProtocol", &RCSwitch::getReceivedProtocol, "Returns pulse delay in microseconds when successfully decoded")
      .def("getReceivedRawdata", &RCSwitch::getReceivedRawdataList, "Returns the raw pulse train when successfully decoded")

      .def("setPulseLength", &RCSwitch::setPulseLength, "Sets pulse length in microseconds")
      .def("setRepeatTransmit", &RCSwitch::setRepeatTransmit, "Sets repeat transmits")
      .def("setReceiveTolerance(", &RCSwitch::setReceiveTolerance, "Set receiving tolerance")

      .def("setProtocol", static_cast<void(RCSwitch::*)(int)> (&RCSwitch::setProtocol), "Sets the protocol to send, from a list of predefined protocols")
      .def("setProtocol", static_cast<void(RCSwitch::*)(int, uint16_t)> (&RCSwitch::setProtocol), "Sets the protocol to send with pulse length in microseconds")

      .def("decodePulseTrain", &RCSwitch::decodePulseTrain, "Decodes a pulse train simulating its reception by radio frequency receiver");

#ifdef VERSION_INFO
      module.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
      module.attr("__version__") = "dev";
#endif

}

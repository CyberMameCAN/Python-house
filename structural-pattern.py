"""
Structural Pattern
- Adapter (継承・移譲)

https://www.youtube.com/watch?v=tAuRQs_d9F8

既存クラスを修正せずに、継承・移譲したクラスで追加機能を持たせる。
移譲のほうが自由度が高い。
"""

class UsbCable:
    def __init__(self):
        self.in_plugged = False
        
    def plug_usb(self):
        self.is_plugged = True
        print(self.is_plugged, end="☆")


class UsbPort:
    def __init__(self):
        self.port_available = True
    
    def plug(self, usb):
        if self.port_available:
            usb.plug_usb()
            self.port_available = False


class MicroUsbCable:
    def __init__(self):
        self.is_plugged = False
        
    def plug_micro_usb(self):
        self.is_plugged = True
        print(self.is_plugged, end="★")


class MicroToUsbAdapter(UsbCable):
    def __init__(self, micro_usb_cable):
        self.micro_usb_cable = micro_usb_cable
        self.micro_usb_cable.plug_micro_usb()
        
    # can override UsbCable.plug_usb() if needed


def main():
    # UsbCables can plug directly into Usb ports
    usbCable = UsbCable()
    usbPort1 = UsbPort()
    usbPort1.plug(usbCable)

    # MicroUsbCables can plug into Usb ports via an adapter
    microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())
    usbPort2 = UsbPort()
    usbPort2.plug(microToUsbAdapter)


if __name__ == '__main__':
    main()
import pywifi
from pywifi import const
import time

def check_wifi():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()
    if not ifaces:
        print("No Wi-Fi interface found.")
        return

    iface = ifaces[0]
    print("Using Wi-Fi interface:", iface.name())

    status = iface.status()
    if status == const.IFACE_CONNECTED:
        print("Wi-Fi is connected.")
    else:
        print("Wi-Fi is not connected.")

    print("Scanning for Wi-Fi networks...")
    iface.scan()
    time.sleep(3)
    results = iface.scan_results()

    if results:
        print("Found networks:")
        for network in results:
            print(f"SSID: {network.ssid:<30} Signal: {network.signal}")
    else:
        print("No networks found.")

if __name__ == "__main__":
    check_wifi()
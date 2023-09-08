from napalm import import get_network_driver
import json

driver = get_network_driver("ios")

device = driver(
    hostname="IP",
    username="SEU_USERNAME",
    password="cisco",
    optional_args={"port":22}
)

device.open()

output = device.get_facts()
print(json.dump(output,indent=4))
output = device.get_interfaces()
print(json.dump(output,indent=4))
output = device.get_interfaces_counters()
print(json.dump(output,indent=4))
output = device.get_mac_addres_table()
print(json.dump(output,indent=4))
output = device.get_arp_table()
print(json.dump(output,indent=4))

device.load_merge_canditate(filename="r1-config.cfg")
device.commit_config()
device.close()

output = device.get_bgp_neighbors()
print(json.dump(output,indent=4))
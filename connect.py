from napalm import get_network_driver

# Use the IOS driver since the router in PNETLab is running Cisco IOS
driver = get_network_driver("ios")

# Router details
hostname = "192.168.223.200"
username = "cisco"
password = "cisco"
enable_secret = "cisco"

# The connection object
connection = driver(
    hostname=hostname,
    username=username,
    password=password,
)

# Open the SSH connection when this file runs or gets imported
connection.open()

if __name__ == "__main__":
    # Just checking that the connection actually works
    print(f"Connection to {hostname} opened successfully.")
    connection.close()

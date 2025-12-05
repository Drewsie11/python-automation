from connect import connection
import difflib

def main():
    # Get the current running config
    before_config = connection.get_config().get("running", "")

    # Two changes on Fa0/0
    config_commands = [
        "interface FastEthernet0/0",
        " description Updated via modify.py",
        " no ip redirects",
        " exit"
    ]

    # Use Netmiko device that NAPALM created for us
    device = connection._netmiko_device

    print("=== Applying Config Changes ===")
    output = device.send_config_set(config_commands)
    print(output)

    # Pull config again after changes
    after_config = connection.get_config().get("running", "")

    # Compute differences
    before_lines = before_config.splitlines(keepends=True)
    after_lines = after_config.splitlines(keepends=True)

    diff = difflib.unified_diff(
        before_lines,
        after_lines,
        fromfile="before",
        tofile="after"
    )

    diff_text = "".join(diff)

    print("=== Config Differences ===")
    print(diff_text if diff_text else "No differences found.")

    # Save diff for assignment
    with open("config_changes.txt", "w") as f:
        f.write(diff_text)

    # Save new full config for assignment
    with open("modified_config.txt", "w") as f:
        f.write(after_config)

    print("Saved config_changes.txt and modified_config.txt")

    # Close connection
    connection.close()


if __name__ == "__main__":
    main()

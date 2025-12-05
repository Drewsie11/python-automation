from connect import connection

def main():
    # Pull all the config info from the router
    configs = connection.get_config()

    # Grab the running config from the dictionary
    running_config = configs.get("running", "")

    # Print it out so we can see it in the console
    print("=== Running Config ===")
    print(running_config)

    # Save the running config to a text file
    with open("current_config.txt", "w") as f:
        f.write(running_config)

    print("\nSaved running config to current_config.txt")

    # Close the connection when we’re done
    connection.close()


if __name__ == "__main__":
    main()
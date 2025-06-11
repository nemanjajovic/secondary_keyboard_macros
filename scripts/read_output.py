import re


def read_output():
    # Read the content of the file
    with open("luaoutput.txt", "r") as f:
        content = f.read()

    # Step 1: Find the block that starts with '0:' and ends before the next number-colon pattern
    block_match = re.search(r"0:\s+(.*?)(?:\n\d+:|$)", content, re.DOTALL)

    if block_match:
        block = block_match.group(1)

        # Step 2: Extract the SystemId within that block
        sysid_match = re.search(r"SystemId\s*=\s*(\S+)", block)

        if sysid_match:
            system_id = sysid_match.group(1)

            # Step 3: Extract the part between the 3rd and 4th '&'
            parts = system_id.split("&")
            if len(parts) >= 4:
                print(parts[3])
                return f"'{parts[3]}'"
            else:
                print("SystemId does not contain enough '&' symbols.")
        else:
            print("SystemId not found in the '0:' block.")
    else:
        print("Block starting with '0:' not found.")

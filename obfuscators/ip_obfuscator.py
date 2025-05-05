# Copyright (c) 2025-present, Swadhin
# Python script to obfuscate ip

import sys
import random


def convert_to_octects(ip: str) -> list[str]:
    """
    Splits an IPv4 address into its octets.

    Args:
        ip (str): The IPv4 address as a string.

    Returns:
        list: A list of octets as strings.
    """
    if not isinstance(ip, str):
        raise ValueError("Input must be a string.")
    octets = ip.split(".")
    if len(octets) != 4 or not all(o.isdigit() and 0 <= int(o) <= 255 for o in octets):
        raise ValueError("Invalid IPv4 address.")
    return octets


def convert_to_hex(octets: list[str]) -> str:
    """
    Converts IPv4 octets to a hexadecimal representation.

    Args:
        octets (list): A list of IPv4 octets.

    Returns:
        str: A single string representing the IPv4 address in hexadecimal.
    """
    return "".join([f"{int(o):02x}" for o in octets])


def convert_to_octal(octets: list[str]) -> str:
    """
    Converts IPv4 octets to an octal representation.

    Args:
        octets (list): A list of IPv4 octets.

    Returns:
        str: A string where each octet is represented in octal, separated by dots.
    """
    return ".".join([f"{int(o):03o}" for o in octets])


def convert_to_binary(octets: list[str]) -> str:
    """
    Converts IPv4 octets to a binary representation.

    Args:
        octets (list): A list of IPv4 octets.

    Returns:
        str: A string where each octet is represented in binary, separated by dots.
    """
    return ".".join([f"{int(o):08b}" for o in octets])


def convert_to_ipv6(octets: list[str]) -> str:
    """
    Converts an IPv4 address (provided as octets) to an IPv6 mapped address.

    Args:
        octets (list): A list of IPv4 octets.

    Returns:
        str: The IPv6 mapped address.
    """
    # Convert each octet to a two-digit hex string.
    ip_hex_segments = [f"{int(o):02x}" for o in octets]
    # Combine first two and last two octets into 16-bit hexadecimal segments.
    segment1 = ip_hex_segments[0] + ip_hex_segments[1]
    segment2 = ip_hex_segments[2] + ip_hex_segments[3]
    # Return the IPv4-mapped IPv6 address.
    return f"::ffff:{segment1}:{segment2}"


def add_random_padding(octets: list[str]) -> str:
    """
    Adds random leading zero padding to each octet of the IP address.
    For each octet, a random number (0 to 3) of zeros is prepended.

    Args:
        ip (str): The IPv4 address as a string.

    Returns:
        str: The padded IPv4 address.
    """
    padded_octets = []
    for o in octets:
        zeros = "0" * random.randint(0, 3)
        padded_octets.append(f"{zeros}{o}")
    return ".".join(padded_octets)


def obfuscate_random_octet(octets: list[str]) -> str:
    """
    Obfuscates one random octet of the IP address using one of the available representations:
    hexadecimal, octal, or binary.

    Args:
        ip (str): The IPv4 address as a string.

    Returns:
        str: The IPv4 address with one octet obfuscated.
    """
    index = random.randint(0, 3)
    representation = random.choice(["hex", "octal", "binary"])
    original_oct = octets[index]
    num = int(original_oct)
    if representation == "hex":
        octets[index] = f"{num:02x}"
    elif representation == "octal":
        octets[index] = f"{num:03o}"
    elif representation == "binary":
        octets[index] = f"{num:08b}"
    return ".".join(octets)


def remove_extra_zeros(octets: list[str]) -> str:
    """
    Removes octets that are equal to zero from the IP address.
    E.g., converts "127.0.0.1" to "127.1".

    Args:
        ip (str): The IPv4 address as a string.

    Returns:
        str: The shortened IPv4 address.
    """
    # Filter out octets that represent 0
    filtered = [o for o in octets if int(o) != 0]
    # In case all octets are 0, return a single 0.
    return ".".join(filtered) if filtered else "0"


def main():
    if len(sys.argv) != 2:
        print("Usage: ip_obfuscator.py <ipv4_address>")
        sys.exit(1)

    ip = sys.argv[1]
    try:
        octets = convert_to_octects(ip)
        print("Hex:", convert_to_hex(octets))
        print("Octal:", convert_to_octal(octets))
        print("Binary:", convert_to_binary(octets))
        print("IPv6:", convert_to_ipv6(octets))
        print("Random Padding:", add_random_padding(octets))
        print("Obfuscate Random Octet:", obfuscate_random_octet(octets))
        print("Remove Extra Zeros:", remove_extra_zeros(octets))
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()

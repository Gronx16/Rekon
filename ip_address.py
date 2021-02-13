import os

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())

    marker_ipv4 = results.find("has address") + 12
    ip= "IPv4: " + results[marker_ipv4:].splitlines()[0]

    if "IPv6 address" in results:
        marker_ipv6 = results.find("IPv6 address") + 13
        ip= "IPv4: " + results[marker_ipv4:].splitlines()[0] + "\n" + "IPv6: " + results[marker_ipv6:].splitlines()[0]

    return ip

def ipv4(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())

    marker_ipv4 = results.find("has address") + 12
    ip=results[marker_ipv4:].splitlines()[0]
    return str(ip)


from domain_name import *
from general import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

root_dir = "Targets"

create_dir(root_dir)

def create_report(url,host_name,domain_name,ip_addr,nmapi,whois,robots="Nill"):
    target_dir = root_dir + "/" + domain_name
    create_dir(target_dir)
    write_file(target_dir + "/full_url.txt", url)
    write_file(target_dir + "/domain_name.txt", domain_name)
    write_file(target_dir + "/nmap.txt", nmapi)
    write_file(target_dir + "/whois.txt", whois)
    if robots!="Nill":
        write_file(target_dir + "/robots.txt", robots)
    
    


def gather_info(url):
    host_name= get_host_name(url)
    print("Extracting URL DONE")
    domain_name = get_domain_name(url)
    print("Extracting Domain Name DONE")
    ip_addr = get_ip_address(domain_name)
    nmapi = get_nmap("-F",ipv4(domain_name))
    print("Port Scan DONE")
    whois = get_whois(domain_name)
    print("Whois data extracted DONE")
    robots = get_robots_txt(url)
    if robots!=0:
        print("Robots.txt file extracted DONE")
        create_report(url,host_name,domain_name,ip_addr,nmapi,whois,robots)
    else:
        create_report(url,host_name,domain_name,ip_addr,nmapi,whois)

asd=input("Enter the url: ")
gather_info(asd)
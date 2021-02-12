from tld import get_tld

def get_domain_name(url):
    #return object from get_tld
    domain_name = get_tld(url, as_object=True)
    return domain_name.fld



def get_host_name(url):
    #return object from get_tld
    domain_name = get_tld(url, as_object=True)
    return domain_name.domain


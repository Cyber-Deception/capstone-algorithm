#!/usr/bin/env python
import nmap

    
def scanTarget(ip):

    nm = nmap.PortScanner()
    nm.scan(hosts=ip,'0-65535')
    serv_list = list()

    for proto in nm[ip].all_protocols():
        lport = nm[ip][proto].keys()

        for port in lport:

            serv_list.append({"port":port,"state":nm[ip][proto][port]['state'],"protocol":proto,"service_name":nm[ip][proto][port]['product'], "cpe":nm[ip][proto][port]['cpe']})

    return serv_list


if __name__ == "__main__":
   print(scanTarget('127.0.0.1'))
   

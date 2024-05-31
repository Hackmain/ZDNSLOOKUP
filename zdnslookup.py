import dns.resolver

target = str(input("PUT IP OR DOMAIN name >"))
types = ["A", "AAAA", "MX", "NS", "SOA", "SRV", "CNAME"]
for record in types:
    zdns = dns.resolver.query(target, record, raise_on_no_answer=False)
    if zdns.rrset is not None:
        print(zdns.rrset)

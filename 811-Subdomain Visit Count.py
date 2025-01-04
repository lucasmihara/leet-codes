class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp = {}
        for c in cpdomains:
            count, domain = c.split(" ")
            sub = ""
            for d in reversed(domain.split(".")):
                sub = d + "." + sub
                if sub not in cp:
                    cp[sub] = 0
                cp[sub] += int(count)
        
        return [f"{str(v)} {k[:-1]}" for k, v in cp.items()]


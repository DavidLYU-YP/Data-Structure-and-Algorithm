class Solution(object):
    def subdomainVisits(self, cpdomains):
        ans = {}
        for domain in cpdomains:
            num, domain = domain.split( )
            num = int(num)
            link = domain.split('.')
            for i in range(len(link)):
                if '.'.join(link[i:]) not in ans.keys():
                    ans['.'.join(link[i:])] = 0
                ans['.'.join(link[i:])] += num

        return ["{} {}".format(num, domain) for domain, num in ans.items()]
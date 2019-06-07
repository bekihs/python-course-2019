import re

print(re.search("ha" , "hadas"))

def getMatches(str):
    matchs =  re.findall("([a-z]+_[a-z]+)" , str)
    return matchs


print( getMatches("aa_aa8ss_dd&a_a_a_sss_aa789")) 
#['aa_a', 'ss_d', 'a_a', 'ss_a']
print( getMatches("jsnkjas jk jk 8 nk * aa_aa8ss_dd9a_a_a_sss_aa789"))
#['aa_a', 'ss_d', 'a_a', 'ss_a']
print( getMatches("jsnkjas_jk jk 8 nk * aa_a a8ss_dd9a_a_a_sss_aa789"))
 #['jsnkjas_jk', 'aa_a', 'ss_dd', 'a_a', 'a_sss']
print( getMatches("0502e20022"))#[]]
print( getMatches("aa@ee.ss"))#[]
print( getMatches(""))#[]

x = re.findall("\$" , "Give me 66$ now and 50$ tomorrow")
print(x) #['$', '$']

courses = ['CSE2012-Design and Analysis of Algorithm-4-ETHL', 
'CSE2001-Computer Architechture and Organization-3-ETH', 
'CSE2004-Database Managemant System-4-ETHL', 
'CSE2005-Operating System-4-ETHL', 
'STS2001-Numerical Ability-1-ETH', 
'MAT2002-Application of Derivative-4-ETHL']

result = ''

def computeLPSArray(pat, m, lps):
    len = 0
    i = 1
    lps[0] = 0
    while (i < m):
        if (pat[i] == pat[len]):
            lps[i] = len + 1
            len += 1
            i += 1
        else:
            if(len != 0):
                len = lps[len -1]
            else:
                lps[i] = 0
                i += 1

def KMPSearch(pat, txt):
    N = len(txt)
    M = len(pat)
    lps = [0]*M
    
    computeLPSArray(pat, M , lps)
    i=j=0
    while (i < N-M+1):
        if(txt[i] == pat[j]):
            i += 1
            j += 1
        else:
            if (j != 0):
                j = lps[j-1]
            else:
                i += 1
        
        if (j == M):
            print('Match Found',i-j)
            # print(txt.split("-")[0])
            # print(txt.split("-")[1])
        
            j = lps[j-1]
            
            return True

def find(courseId):
    # booln = KMPSearch('CSE2005', 'CSE2005-Operating System-4-ETHL')
    # print(booln)
    for i in courses:
        if(KMPSearch(courseId, i) == True):
            result = i
            break
        else:
            continue
    
    return result
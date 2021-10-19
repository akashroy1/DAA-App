
courses = ['CSE2012-Design and Analysis of Algorithm-4-Embedded Theory and Lab', 
'CSE2001-Computer Architechture and Organization-3-Theory Only', 
'CSE2004-Database Managemant System-4-Embedded Theory and Lab', 
'CSE2005-Operating System-4-Embedded Theory and Lab', 
'STS2001-Numerical Ability-1-Theory Only', 
'MAT2002-Application of Derivative-4-Embedded Theory and Lab',
'CSE1003-Digital Logic and Design-Embedded Theory and Lab',
'CSE1004-Network and Communication-Embedded Theory and Lab',
'CSE1007-Java Programming-Embedded Theory and Lab',
'CSE2001-Computer Architecture and Organization-Theory Only',
'CSE2004-Database Management Systems-Embedded Theory Lab and Project',
'CSE2005-Operating Systems-Embedded Theory and Lab',
'CSE2006-Microprocessor and Interfacing-Embedded Theory Lab and Project',	
'CSE2011-Data Structures and Algorithms-Embedded Theory and Lab',
'CSE2012-Design and Analysis of Algorithms-Embedded Theory and Lab',
'CSE2013-Theory of Computation-Theory Only',
'CSE3001-Software Engineering-Embedded Theory Lab and Project',
'CSE3002-Internet and Web Programming-Embedded Theory Lab and Project',
'CSE4001-Parallel and Distributed Computing-Embedded Theory Lab and Project',
'MAT1014-Discrete Mathematics and Graph Theory-Theory Only',
'CSE1006-Blockchain and Cryptocurrency Technologies-Theory Only',
'CSE2014-Compiler Design-Embedded Theory and Lab',
'CSE3006-Embedded System Design-Embedded Theory and Lab',
'MAT2002-Applications of Differential and Difference Equations-Embedded Theory and Lab',
'CSE3011-Robotics and its Applications-Embedded Theory and Lab',
'CSE3013-Artificial Intelligence-Embedded Theory and Project',
'CSE3016-Computer Graphics and Multimedia-Embedded Theory Lab and Project',
'CSE3018-Content Based Image and Video Retrieval-Embedded Theory Lab and Project',
'CSE3020-Data Visualization-Embedded Theory Lab and Project',
'CSE3021-Social and Information Networks-Embedded Theory and Project',
'CSE3024-Web Mining-Embedded Theory and Lab',
'CSE3025-Large Scale Data Processing-Embedded Theory Lab and Project',
'CSE3029-Game Programming-Embedded Theory, Lab and Project',
'CHY1701-Engineering Chemistry-Embedded Theory and Lab',
'ENG1901-Technical English - I-Lab Only',
'ESP1001-ESPANOL FUNDAMENTAL-Theory Only',	
'FRE1001-Francais quotidien-Theory Only',
'GER1001-Grundstufe Deutsch-Theory Only',
'HUM1021-Ethics and Values-Theory Only',
'JAP1001-Japanese for Beginners-Theory Only',
'MAT1011-Calculus for Engineers-Embedded Theory and Lab',
'PHY1701-Engineering Physics-Embedded Theory and Lab',
'STS1001-Introduction to Soft Skills-Soft Skill',
'STS1201-Introduction to Problem Solving-Soft Skill',
'CSE1902-Industrial Internship-Project',
'BCD3001-Bayesian Data Analysis-Embedded Theory and Project',
'BCI2002-Image Processing-Embedded Theory and Project',
'BCT3001-Wireless Ad-hoc and Sensor Networks-Embedded Theory and Project',
'BIT1002-Biostatistics-Theory Only',
'CBS1002-Object Oriented Programming-Embedded Theory and Lab',
'CBS1006-Principles of Operating Systems-Embedded Theory and Lab',
'CHE1004-Chemical Technology-Theory Only',
'EXC1001-Service to the Society-Extra Curricular Activity',
'EXC1002-Youth Red Cross-Extra Curricular Activity',		
'CHY1002-Environmental Sciences-Theory Only',
'BIT1001-Introduction to Life Sciences-Theory Only']

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
            course = []
            for i in range (0, 4):
                course.append(result.split("-")[i])
            result = course
            break
        else:
            result = 'Wrong Course Code'
            continue

    return result

# if __name__ == "__main__":
#     print(find('CSE2012')) #.split("-")[0]
#     # print(txt.split("-")[0])
#     # print(txt.split("-")[1])
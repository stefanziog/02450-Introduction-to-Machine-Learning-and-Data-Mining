import math
import numpy as np
# x = 5*16
# print(x)

k = (1/2 ) * math.log(4) # log
w1 = (1/25) * math.exp(-0.6931)
w = (1/25) * math.exp(0.6931) # e to the power

new_w = (1/25)*w / ((20/25)*w1 + (5/25)*w)

s4 =math.sqrt(212 - (11.1 **2 )-(7.2 ** 2) - (5.2 ** 2))
# GINI IMPURITY BY HAND
d = 1 - ((18/54)**2 + (18/54)**2+ (18/54)**2)
d1 = -((18/54)*(1-((6/18)**2+(9/18)**2+(3/18)**2)))
d2 = -((20/54)*(1-((4/20)**2+(6/20)**2+(10/20)**2)))
d3 = -((16/54)*(1-((8/16)**2+(3/16)**2+(5/16)**2)))
dol = d+d1+d2+d3
# print(dol)


#GMM BY HAND QUESTION 12 FALL 2017 
# p08_1 = w * (1/math.sqrt(2*math.pi*0.σ or λ **2)) * math.exp(-(((x0-μ)**2)/((2*σ or λ **2))))

p08_1 = 0.13 * (1/math.sqrt(2*math.pi*1.2193**2)) * math.exp(-(((15.38-18.347)**2)/((2*1.2193**2))))
p08_2 = 0.55 * (1/math.sqrt(2*math.pi*(0.986**2))) * math.exp(-((15.38-14.997)**2/(2*(0.986**2))))
p08_3 = 0.32 * (1/math.sqrt(2*math.pi*(1.1354**2))) * math.exp(-((15.38-18.421)**2/(2*(1.1354**2))))

p08_to_2 = p08_2 / (p08_1 + p08_2 + p08_3)

print("GMM PROBABILITY IS",p08_to_2)

# GAUSSIAN KERNELS
m = [-0.82, 0.0, 2.5]
s = 0.15


# Precompute constants
sqrt_part = 1 / (math.sqrt(2 * math.pi * s**2))


for i in range(len(m)):
    terms_p = []  # Terms for p4 calculation
    
    # Calculate terms for p4
    for j in range(len(m)):
        if i != j:
            terms_p.append(math.exp(-((m[i] - m[j])**2) / (2 * s**2)))
    
    # Calculate p2 and p4
    p = (1/0.26) * (1/math.sqrt(2*math.pi*s**2)) * sum(terms_p)
    
    print(f"For m{i+1}: p{i+1} = {p}")
    
# p2 = (1/3) * (1/math.sqrt(2*math.pi*s**2)) * (math.exp(-(((3.918+6.35)**2)/((2*s**2))))+math.exp(-(((3.918+2.677)**2)/((2*s**2))))+math.exp(-(((3.918+3.003)**2)/((2*s**2)))))
# p4 = (1/3) * (1/math.sqrt(2*math.pi*s**2)) * (math.exp(-(((-3.003-3.918)**2)/((2*s**2))))+math.exp(-(((-3.003+2.677)**2)/((2*s**2))))+math.exp(-(((-3.003+6.35)**2)/((2*s**2)))))

# print(p2)

LooErr = (-1/3)*((math.log(1.0554215910485338)+math.log(0.02862598368036777)+math.log(1.1603574453811363)+math.log(0.14628354835921967)))
print("LOOERR",LooErr)


p = 2.84+3.46*2.5156
# print(p)


# p3 = 0.85*0.32
# p1= 1.25*0.15
# p2 = 0.45*0.53
# pxto3 = p3 / (p1+p2+p3)
# print(pxto3)


#FOR CORRELATION WITH COV TABLE
cor = -7.0/(math.sqrt(415)*math.sqrt(1))  

# print(cor)


phigh = 3285/8760
pmid = 2190/8760
plow = 3285/8760

p1high = 1 - (2344/3285)
p1mid = 1- (1718/2190)
p1low = 1- (1327/3285)

phigh1 = (p1high * phigh) / ((p1high * phigh) + (p1mid * pmid) + (p1low * plow))
# print(phigh1)
# bestsup = 3637/8760
# print(bestsup)

# k = math.exp((1-0.5)/0.5)
# print(k)

#PRINCIPAL COMPONENT
s1 = 30.19
s2 = 16.08
s3 = 11.07
s4 = 5.98

Var1 = (s1**2) / (s1**2 + s2**2 + s3**2 + s4**2)    
Var2 = (s2**2) / (s1**2 + s2**2 + s3**2 + s4**2)
Var3 = (s3**2) / (s1**2 + s2**2 + s3**2 + s4**2)
Var4 = (s4**2) / (s1**2 + s2**2 + s3**2 + s4**2)
var12 = Var1 + Var2
var123 = Var1 + Var2 + Var3
print("variance 1:", Var1)  
print("variance 12", var12)
print("variance 123", var123)

#For RandIndex BY HAND Q8 2020


# S = (114*113)/2 + (32*31)/2+ (119*118)/2 + (8*7)/2+ (60*59)/2
# N = 114+32+119+8+60
# print ("total" ,N) 
# D = N*(N-1)/2 - ((146*145)/2 + (119*118)/2 + (68*67)/2) - ((122*121)/2 + (119*118)/2 + (92*91)/2) + S
# R = (S+D)/(0.5*(N*(N-1)))
# print("DA RESULT",R)


#AVERAGE LINKAGE OF TWO CLUSTERS BY HAND

# avg = (1025+925+1375+1100+1000+1450)/6
# print("average", avg)

prob1 = (0.97*0.01)/(0.97*0.01 + 0.03*0.99)

print ("probability", prob1) 
print("is it",)

#COV

s1 = 49.164
s2 = 31.401
s3 = 29.678
s4 = 12.436
s5 = 7.837

Var1 = (s1**2) / (s1**2 + s2**2 + s3**2 + s4**2 + s5**2)
print("Variance of first component:", Var1)

Var12 = (s1**2 + s2**2) / (s1**2 + s2**2 + s3**2 + s4**2 + s5**2)
print("Variance of first two components:", Var12)
var13 = (s1**2 + s2**2 + s3**2) / (s1**2 + s2**2 + s3**2 + s4**2 + s5**2)
print("Variance of first three components:", var13)
# VarLast4 = (s2**2 + s3**2 + s4**2 + s5**2) / (s1**2 + s2**2 + s3**2 + s4**2 + s5**2)
# print("Variance of last four components:", VarLast4)
varfirstthree = (s1**2 + s2**2 + s3**2) / (s1**2 + s2**2 + s3**2 + s4**2 + s5**2)
print("Variance of first three components:", varfirstthree)


#PARAMETERS NN (M+1)*nh + (nh+1)*Classes
# parametersNN = 5*(34-16)
# print("NN parameters",parametersNN)
# k = math.tanh(1.2)
# print(k)

conf = 436/1815

x = math.exp(math.log(2))
print("x",x)
print("conf ", conf, 4/27,1/6,3/16)

K = 236+4+33+27
N=(13-100)/900
print("MCNEMAR theta",N)

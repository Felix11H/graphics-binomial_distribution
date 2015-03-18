import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as sc
 
#plotting binomials
k_range = np.arange(0,41) 
col = {0: 'orange', 1: 'purple', 2: 'lightblue'}
 
def binomial_value(n,k,p):
    return sc.comb(n,k)*(p**k)*((1-p)**(n-k)) 
 
 
plt.clf()
plt.figure(figsize=(4,3.2))
Ax = plt.axes([0.17,0.13,0.79,0.8])
plt.hold(True)
 
 
p_n_pairs = [(0.6,int(20/0.6)),(0.2,int(20/0.2)),(0.01,int(20/0.01))]
 
A = []
for L,pair in enumerate(p_n_pairs):
 
    p = pair[0]
    n = pair[1]
 
    prob_values = np.array([binomial_value(n,k,p) for k in k_range])
 
    plt.plot(k_range, prob_values, '-', color='grey')
    a, = plt.plot(k_range, prob_values, 'o', color=col[L])
    A.append(a)
 
plt.xlabel("k")
plt.ylabel(r"P(X=k)")
 
bx = plt.legend(A, (r"$p=%.2f,\,n=%d$" % p_n_pairs[0], r"$p=%.2f,\,n=%d$" % p_n_pairs[1], r"$p=%.2f,\,n=%d$" % p_n_pairs[2]), numpoints=1, handletextpad=0, loc="upper right",prop={'size':9})
bx.draw_frame(False)
plt.xlim(10,30)
 
#plotting poisson for lambda=np=20
 
import scipy.special as sp
 
x_range = np.arange(0,41,0.05) 
 
L = 20
P = -L + x_range*np.log(L) - sp.gammaln(x_range+1)
P = np.exp(P)
t, = plt.plot(x_range,P, 'r', linestyle='dashed')
kx = plt.legend([t], (r"$\mathrm{Pois}(np=20)$",), "lower center", numpoints=1, prop={'size':9})
kx.draw_frame(False)
 
plt.gca().add_artist(bx)
 
 
plt.savefig("p-060-020-001_n-33-100-2000_Poisson-np-20.png", dpi=300)

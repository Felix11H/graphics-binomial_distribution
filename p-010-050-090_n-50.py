import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as sc
 
k_range = np.arange(0,50) 
col = {0: 'orange', 1: 'purple', 2: 'lightblue'}
 
def binomial_value(n,k,p):
    return sc.comb(n,k)*(p**k)*((1-p)**(n-k)) 
 
 
plt.clf()
plt.figure(figsize=(4,3.2))
Ax = plt.axes([0.17,0.13,0.79,0.8])
plt.hold(True)
 
 
p_n_pairs = [(0.1,50),(0.5,50),(0.9,50)]
 
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
 
bx = plt.legend(A, (r"$p=%.1f,\,n=%d$" % p_n_pairs[0], r"$p=%.1f,\,n=%d$" % p_n_pairs[1], r"$p=%.1f,\,n=%d$" % p_n_pairs[2]),\
                numpoints=1, handletextpad=0, loc="upper center",prop={'size':12})
bx.draw_frame(False)
plt.xlim(0,50)
 
 
plt.savefig("p-010-050-090_n-50.png", dpi=300)

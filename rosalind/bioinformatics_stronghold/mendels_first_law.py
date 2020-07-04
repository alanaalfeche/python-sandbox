"""
k organisms of homozygous dominant: AA
m organisms of heterozygous: Aa
n organisms of homozygous recessive: aa

Probability Tree Diagram: 
k -- k = k/t * k-1/t-1  * 1 // because there will always be at least 1 A         A   A
     m = k/t * m/t-1    * 1 // as shown in the following                     A  AA  AA
     n = k/t * n/t-1    * 1 // Punnett Square                                a  Aa  Aa

m -- k = m/t * k/t-1    * 1 
     m = m/t * m-1/t-1  * 0.75
     n = m/t * n/t-1    * 0.50
    
n -- k = n/t * k/t-1    * 1
     m = n/t * m/t-1    * 0.50
     n = n/t * n-1/t-1  * 0

P (AA and Aa) = (k * k - 1) + (k * m) + (k * n) + (m * k) + 0.75(m * m-1) + 0.50(m * n) + (n * k) + 0.50(n * m) + 0(n * n-1) / t(t-1)
              = (k^2 - k) + (km + mk) + (kn + nk) + 0.75(m^2-m) + (0.50mn + 0.50nm) / t(t-1)
              = (k^2 - k + 2km + 2kn + 0.75m^2 + 0.75m + 1mn) / t(t-1) 
"""
k = 2
m = 2
n = 2
t = k + m + n
prob = (k**2 - k + 2*k*m + 2*k*n + 0.75*m**2 + 0.75*m + 1**n) / (t*(t-1)) 
print(prob)
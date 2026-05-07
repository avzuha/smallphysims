import numpy as np
import matplotlib.pyplot as plt

def kronig_penney(P, a, alpha_min, alpha_max):
    alpha = np.linspace(alpha_min, alpha_max, 2000)
    
    
    lhs = np.zeros_like(alpha)
    mask = alpha != 0
    lhs[mask] = (P * np.sin(alpha[mask] * a)) / (alpha[mask] * a) + np.cos(alpha[mask] * a)
    lhs[~mask] = P + 1  
    
 
    plt.figure(figsize=(12,6))
    plt.plot(alpha, lhs, label=r'$\frac{P \sin(\alpha a)}{\alpha a} + \cos(\alpha a)$', color='blue')
    
    # RHS bounds: cos(k*a) ∈ [-1, 1]
    plt.axhline(1, color='green', linestyle='--', label=r'$\cos(ka)=+1$')
    plt.axhline(-1, color='red', linestyle='--', label=r'$\cos(ka)=-1$')
    

    plt.title("Kronig-Penney Model Dispersion Relation")
    plt.xlabel(r'$\alpha a$')
    plt.ylabel("Function Value")
    plt.xlim(alpha_min, alpha_max)
    ymin, ymax = lhs.min(), lhs.max()
    plt.ylim(ymin - 1, ymax + 1)
    plt.xticks(np.arange(alpha_min, alpha_max+1, np.pi), 
               [f"{int(x/np.pi)}π" for x in np.arange(alpha_min, alpha_max+1, np.pi)])
    plt.grid(True)
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    print("Kronig-Penney Model Graph Generator")
    P = eval(input("Enter potential strength parameter P: "))
    a = eval(input("Enter lattice constant a: "))
    alpha_min = eval(input("Enter minimum alpha value (e.g., -4*np.pi): "))
    alpha_max = eval(input("Enter maximum alpha value (e.g., 4*np.pi): "))
    
    kronig_penney(P, a, alpha_min, alpha_max)



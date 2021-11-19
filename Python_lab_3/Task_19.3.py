import numpy as np 
def roots_of_quadratic_equation(*k):
    a, b, c = k[0], k[1], k[2] 
    D = b ** 2 - 4 * a * c  
    x1 = (-b + D ** 0.5) / (2 * a) 
    x2 = (-b - D ** 0.5) / (2 * a) 
    
    if isinstance(x1, complex):
        x1 = np.round(x1, 2)
    else:
        x1 = round(x1, 2)
    if isinstance(x2, complex):
        x2 = np.round(x2, 2)
    else:
        x2 = round(x2, 2)
    if int(x1) == int(x2):
        return int(x1)
    return int(x1), int(x2)
def solve(*coeffs):
    if coeffs[0] == coeffs[1] == coeffs[2] == 0:
        return ["all"]
    if coeffs[0] == coeffs[1] == 0:
        return ["no"]
    if coeffs[0] != 0:
        return roots_of_quadratic_equation(*coeffs)
    else:
        b, c = coeffs[1], coeffs[2]
        return [str(-c / b)]
result = solve(0, 0, 0)
print(*sorted(result))

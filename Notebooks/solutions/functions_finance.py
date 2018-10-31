
# Exercise 1
def greet(name):
    """Create a greeting for a person"""
    return "Good morning " + name

print(greet("Robert"))


# Exercise 2:
def compute_compound_interest(P, r, n=12, t=10):
    """Computes compound interest
    
    Where:
        P  is the principle
        r  is the annual interest rate
        n  is the number of times the interest is compounded each year (default to monthly)
        t  is the number of years invested for (default to 10 years)
    """
    return P * (1 + (r / n)) ** (n * t)

def compute_deposit_reduction(P, r, n, t, D):
    """Computes how much you save by depositing D to reduce the principle P
    """
    amount_without_reduction = compute_compound_interest(P, r, n, t)
    amount_with_reduction = compute_compound_interest(P - D, r, n, t)
    
    return amount_without_reduction - amount_with_reduction

print(compute_deposit_reduction(5000, 0.05, 12, 10, 2000))
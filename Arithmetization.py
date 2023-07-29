

""" A (simple) Python Script that reduces a logical Boolean formula (in CNF form) into an algebraic expression. """

""" 

    Arithmetization mappings of the operations (from logical to arithmetic):
        And/~  ----->  (1-var)
        Or     ----->    +
        And    ----->    *


"""

from sympy import symbols, Or, And, Not, to_cnf

# Function that takes the formula as an argument and arithmetizes the logical formula
def arithmetiz(formula):

    # Convert logical formula to CNF
    cnf_formula = to_cnf(formula)

    # Extract individual clauses from CNF
    clauses = cnf_formula.args

    # Arithmetize each clause
    polynomial = 1
    for clause in clauses:
        clause_vars = []
        for var in clause.args:
            if isinstance(var, Not):
                # For negated variable, use (1 - var) 
                clause_vars.append(1 -var.args[0])
            else:
                clause_vars.append(var)
        # Multiply variables within each clause and add them to the polynomial
        polynomial *= sum(clause_vars)
    
    return polynomial


# ------------- in 'main' ------------------------------- #

# Define binary variables
x1, x2, x3, x4 = symbols('x1 x2 x3 x4', binary=True)

# Logical formula: (x2 v x3 v x2) and (~x2 v x4 v x1)
formula = And(Or(x1, x3, x2), Or(Not(x2), x4, x1))
print("Logical Formula:\n ", formula)

# Execute the function and get the result
reducedFormula = arithmetiz(formula)
print("Arithmetic Expression:\n ", reducedFormula)

# Expanded/factored reduced formula
print("Expanded Arithmetic Expression:\n ", reducedFormula.expand())
print("Factored Arithmetic Expression:\n ", reducedFormula.factor())

# Another example of a logical formula: (x3 v ~x5 v x7) and (x5 or x9) and (~x3 or ~x4)
# Define the binary variables for the formula above
x3, x4, x5, x7, x9 = symbols('x3 x4 x5 x7 x9', binary = True)

# Define the logical formula
logicalFormula = And(Or(x3, Not(x5), x7), Or(x5, x9), Or(Not(x3), Not(x4)))
arithmeticFormula = arithmetiz(logicalFormula)

print("Arithmetic Expression of the Second Example:\n ", arithmeticFormula)
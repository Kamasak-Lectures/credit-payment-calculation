# Get following information from user:
# P: Principal - The amount of credit
# r: monthly interest rate (as a percentage)
# n: number of months to repay the credit

# install streamlit if you haven't already using: pip install streamlit
import streamlit as st

st.title("Credit Monthly Payment Calculator")

# Input fields
P = st.number_input("Enter the principal amount (P):", min_value=0.0, format="%.2f")
r = st.number_input("Enter the monthly interest rate (r) as a percentage:", min_value=0.0, format="%.4f")
n = st.number_input("Enter the number of months to repay the credit (n):", min_value=1, format="%d")    

# Calculate monthly payment
if n > 0:
    r_decimal = r / 100  # Convert percentage to decimal
    if r_decimal == 0:
        M = P / n  # No interest case
    else:
        M = P * (r_decimal * (1 + r_decimal) ** n) / ((1 + r_decimal) ** n - 1)
    
    st.write(f"The monthly payment (M) is: ${M:.2f}")
    
    
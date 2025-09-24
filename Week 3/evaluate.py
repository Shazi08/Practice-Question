#Evaluate 10 + 5 * 2 ** 3 > 50 and not False step by step.
 
# Step 1: Solve Expontiation 2**3
step1=2**3
print(f"step1: {step1}")

#Step 2: Solve Multiplication 
step2 = 5*step1
print(f"step2: {5*step1} = {step2}")

#step 3: Solve Addition
step3 = 10 + step2
print(f"step3: {10+step2} = {step3}")

#step 4: Comparison
step4 = step3 > 50
print(f"Step 4: {step3} > 50 = {step4}")

# Step 5: not False
step5 = not False
print(f"Step 5: not False = {step5}")

# Step 6: logical AND of step4 and step5 (final result)
result = step4 and step5
print(f"Step 6: {step4} and {step5} = {result}")

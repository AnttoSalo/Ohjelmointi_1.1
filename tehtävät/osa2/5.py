import math
le = float(input("Anna leiviskät."))
n= float(input("Anna naulat."))
lu= float(input("Anna luodit."))

n=n+le*20
lu=lu+n*32
m=13.3*lu
kg=m/1000
g=m-math.floor(kg)*1000
leftover_kg = math.floor(kg)
g=round(g,2)

print(f"Massa nykymittojen mukaan: {leftover_kg}kilogrammaa ja {g} grammaa.")
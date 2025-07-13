w = "Do the {} thigh , {} no one is looking"
w = w.format("right","even")
print(w,"\n")

s = "Do the {0} thigh , {1} no one is looking"
s = s.format("right","even")
print(s,"\n")

k = "Do the {1} thigh , {0} no one is looking"
k = k.format("right","even")
print(k,"\n")

k = "Do the {b} thigh , {a} no one is looking"
k = k.format(a=10,b=30)
print(k,"\n")

k = "Do the {b:10} thigh , {a} no one is looking"
k = k.format(a=10,b=30)
print(k,"\n")

k = "Do the {b:^10} thigh , {a} no one is looking"
k = k.format(a=10,b=30)
print(k,"\n")

k = "Do the {b:<10} thigh , {a} no one is looking"
k = k.format(a=10,b=30)
print(k,"\n")
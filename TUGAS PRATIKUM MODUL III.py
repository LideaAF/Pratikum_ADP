lambda_t = float(input("masukan nilai lambda_t (nilai > 0) :"))
M= int(input("masukan nilai M :"))
e=2.71828

print("\nMaka didapatkan:")
for n in range (0,M+1):
    if n==0:
        n_faktorial= 1
    else:
        n_faktorial *=n
    print("Nilai dari P(N(t) =", n,") adalah", (e**- lambda_t)*((lambda_t**n)/n_faktorial))


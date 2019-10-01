#En este programa le pedimos al usuario que teclee los coeficientes de  un poinomio y hallamos el valor de las raices
def ecuacion():
    print "Introduzca los coeficientes del polinomio"
    print "A*x^2+B*x+C=0"
    a=input("A= ")
    b=input("B= ")
    c=input("C= ")
    raiz1=(-b+(b*b-4*a*c))/(2*a)
    raiz2=(-b-(b*b-4*a*c))/(2*a)
    print "primera solucion = "
    print raiz1
    print "segunda solucion = "
    print raiz2

ecuacion()

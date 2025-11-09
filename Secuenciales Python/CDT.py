cantidad = float(input("Ingrese la cantidad que quiere agregar: "))
porcentajeInteres = float(input("Ingrese el porcentaje de interes: "))
periodo = float(input("Ingrese el periodo en dias que lo quiere guardar: : "))

valorInteres = (cantidad*porcentajeInteres*periodo)/360

print("Su valor de interes sin descuento es:", valorInteres)
descuento=valorInteres*0.07
print("Su descuento es de:", descuento)
netoPagar=cantidad+valorInteres-descuento
print("Su valor neto a pagar es de:", netoPagar)

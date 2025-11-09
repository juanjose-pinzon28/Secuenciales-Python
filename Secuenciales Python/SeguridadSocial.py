salario = float(input("Ingrese su salario: "))

salud = salario*0.04
pension = salario*0.04
valorAporte = salud+pension

print("Su aporte para la salud y la pension es:",valorAporte)
salarioNeto=salario-valorAporte

print("Su salario neto es:", salarioNeto)
                

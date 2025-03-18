# Calcular_descuento de una compra (Un vestido)
def calcular_descuento(monto_total, porcentaje_descuento=10):

    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento
 
monto_compra = 500
porcentaje_predeterminado = 10
descuento = calcular_descuento(monto_compra)
monto_final = monto_compra - descuento

# Resultados
print(f"\nCOMPRA:")
print(f"Monto total = ${monto_compra}")
print(f"Porcentaje de descuento aplicado: {porcentaje_predeterminado}%")
print(f"Monto de descuento: ${descuento:}")
print(f"Monto final a pagar: ${monto_final}")

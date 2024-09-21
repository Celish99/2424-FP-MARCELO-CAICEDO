def calcular_descuento(monto_total, descuento=10):
  """
  Calcula el descuento sobre un monto total dado.

  Args:
    monto_total: El monto total de la compra.
    descuento: El porcentaje de descuento a aplicar (por defecto, 10%).

  Returns:
    El monto del descuento.
  """

  descuento_decimal = descuento / 100
  monto_descuento = monto_total * descuento_decimal
  return monto_descuento

# Llamadas a la función

# Con el descuento por defecto (10%)
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
print(f"El descuento para una compra de ${monto_compra1} es de ${descuento1:.2f}")
print(f"El monto final a pagar es de ${monto_compra1 - descuento1:.2f}")

# Con un descuento personalizado
monto_compra2 = 200
descuento_personalizado = 15
descuento2 = calcular_descuento(monto_compra2, descuento_personalizado)
print(f"El descuento para una compra de ${monto_compra2} con un descuento del {descuento_personalizado}% es de ${descuento2:.2f}")
print(f"El monto final a pagar es de ${monto_compra2 - descuento2:.2f}")
# Pedimos los datos básicos: salario por hora y horas trabajadas
salario_hora = float(input("Ingrese el salario por hora: "))
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en el mes: "))

# Cálculo del sueldo bruto según las reglas establecidas
if horas_trabajadas <= 160:
    sueldo_bruto = salario_hora * horas_trabajadas  # Se paga normal si no excede 160 horas
elif horas_trabajadas <= 200:
    sueldo_bruto = (160 * salario_hora) + ((horas_trabajadas - 160) * salario_hora * 1.5)  # Horas extra al 1.5x
else:
    sueldo_bruto = (160 * salario_hora) + (40 * salario_hora * 1.5) + ((horas_trabajadas - 200) * salario_hora * 2)  # Horas extra al 2x después de 200

# Cálculo del ISR según la tabla de impuestos
if sueldo_bruto <= 746.04:
    isr = 0.00 + (sueldo_bruto - 0.01) * 0.0192
elif sueldo_bruto <= 6332.05:
    isr = 14.32 + (sueldo_bruto - 746.05) * 0.0640
elif sueldo_bruto <= 11128.01:
    isr = 371.83 + (sueldo_bruto - 6332.06) * 0.1088
elif sueldo_bruto <= 12935.82:
    isr = 893.63 + (sueldo_bruto - 11128.02) * 0.16
elif sueldo_bruto <= 15487.71:
    isr = 1182.88 + (sueldo_bruto - 12935.83) * 0.1792
elif sueldo_bruto <= 31236.49:
    isr = 1640.18 + (sueldo_bruto - 15487.72) * 0.2136
elif sueldo_bruto <= 49233.00:
    isr = 5004.12 + (sueldo_bruto - 31236.50) * 0.2352
elif sueldo_bruto <= 93993.90:
    isr = 9236.89 + (sueldo_bruto - 49233.01) * 0.30
elif sueldo_bruto <= 125325.20:
    isr = 22665.17 + (sueldo_bruto - 93993.91) * 0.32
elif sueldo_bruto <= 375975.61:
    isr = 32691.18 + (sueldo_bruto - 125325.21) * 0.34
else:
    isr = 117912.32 + (sueldo_bruto - 375975.62) * 0.35  # Si el sueldo es muy alto, el impuesto aumenta

# Seguridad social: siempre es el 2.5% del sueldo bruto
seguridad_social = sueldo_bruto * 0.025

# Caja de ahorros: el usuario elige si quiere participar y cuánto desea aportar
print("Seleccione el tipo de participación en la caja de ahorros:")
print("1. No participa")
print("2. Cuota fija ($1,000)")
print("3. Cuota porcentual (3%)")
print("4. Cuota porcentual (5%)")
opcion_caja = int(input("Ingrese su elección (1-4): "))

if opcion_caja == 1:
    ahorro_caja = 0  # No participa
elif opcion_caja == 2:
    ahorro_caja = 1000  # Ahorro fijo de $1000
elif opcion_caja == 3:
    ahorro_caja = sueldo_bruto * 0.03  # Ahorro del 3% del sueldo bruto
elif opcion_caja == 4:
    ahorro_caja = sueldo_bruto * 0.05  # Ahorro del 5% del sueldo bruto
else:
    print("Opción inválida, se considera sin participación en caja de ahorros.")
    ahorro_caja = 0  # Si la opción no es válida, no se descuenta nada

# Ahorro solidario: el usuario elige si quiere aportar y cuánto
print("Seleccione su participación en el ahorro solidario:")
print("1. No participa")
print("2. 1% del sueldo bruto")
print("3. 2% del sueldo bruto")
opcion_solidario = int(input("Ingrese su elección (1-3): "))

if opcion_solidario == 1:
    ahorro_solidario = 0  # No participa
elif opcion_solidario == 2:
    ahorro_solidario = sueldo_bruto * 0.01  # 1% de ahorro
elif opcion_solidario == 3:
    ahorro_solidario = sueldo_bruto * 0.02  # 2% de ahorro
else:
    print("Opción inválida, se considera sin ahorro solidario.")
    ahorro_solidario = 0  # Si la opción no es válida, no se descuenta nada

# Cálculo del sueldo neto restando todas las deducciones
deducciones_totales = isr + seguridad_social + ahorro_caja + ahorro_solidario
sueldo_neto = sueldo_bruto - deducciones_totales

# Mostrar los resultados finales
print("\nResumen de cálculo:")
print(f"Sueldo bruto: ${sueldo_bruto:.2f}")
print(f"ISR: ${isr:.2f}")
print(f"Seguridad social: ${seguridad_social:.2f}")
print(f"Ahorro en caja: ${ahorro_caja:.2f}")
print(f"Ahorro solidario: ${ahorro_solidario:.2f}")
print(f"Deducciones totales: ${deducciones_totales:.2f}")
print(f"Sueldo neto: ${sueldo_neto:.2f}")# Usar este archivo como script

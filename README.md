[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rMafNWiN)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18657443)
# Práctica 1. Estructura de control selectiva
## Introducción

La elaboración de ésta práctica tiene como objetivo el realizar un código ejecutable en base a los conocimientos aprendidos en los talleres de Programación Estructurada.
El código a realizar se trató entonces de realizar un programa que realizar el cálculo para obtener el sueldo neto de una persona que trabaja en una empresa, considerando diferentes factores.
 
 ## Desarrollo

 Para diseñar el algoritmo, se utilizaron variables simples y fáciles de identificar dentro del código, con el objetivo de mantener una estructura clara y comprensible. Además, el orden de ejecución fue un aspecto clave en la lógica del programa. En primer lugar, se solicita al usuario que ingrese su salario por hora y la cantidad de horas trabajadas en el mes. Posteriormente, se le permite seleccionar su participación en la caja de ahorros.

Los cálculos se realizan tomando en cuenta el ISR con base en la tabla proporcionada por el SAT, así como el descuento obligatorio del 2.5% correspondiente a la seguridad social. La secuencia lógica del programa asegura que todas estas operaciones se ejecuten en el orden correcto para obtener un resultado preciso.

### Implementación del algoritmo en Python 

Para la implementación del algoritmo en Python, se utilizaron condicionales (if-elif-else), ya que constituyen la forma más adecuada de determinar si el usuario participa o no en las distintas opciones de ahorro. Además, se empleó el tipo de dato float, dado que los cálculos financieros requieren el uso de valores decimales para garantizar resultados precisos.

Se consideraron diferentes casos para manejar posibles errores en la entrada de datos, asegurando que el programa continúe funcionando correctamente incluso si el usuario introduce un valor no válido. Asimismo, se implementó una impresión estructurada de los resultados, lo que permite al usuario visualizar de manera clara el desglose de su sueldo y las deducciones aplicadas, facilitando así su interpretación.

# Conclusión

Este programa permitió comprender mejor algunos conceptos clave de Python, como el uso de variables, las estructuras condicionales if-elif-else y la conversión de datos con float(). También sirvió para reforzar la importancia de una entrada y salida de datos bien organizadas, lo que mejora la experiencia del usuario.

Además, se aplicaron buenas prácticas en la organización del código para que fuera más claro y fácil de modificar. Este ejercicio ayudó a fortalecer habilidades en la manipulación de datos numéricos, la realización de cálculos secuenciales y la validación de entradas para evitar errores.

Por lo que, más allá de su utilidad para calcular el sueldo neto, este programa representó una excelente oportunidad para poner en práctica los principios de la programación estructurada en Python y mejorar la capacidad de desarrollar soluciones eficientes y bien diseñadas.




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
print(f"Sueldo neto: ${sueldo_neto:.2f}")
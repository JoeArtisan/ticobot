# Tico Trader Bot - Python
Versión actual: **0.1.1**

## Contenido

- [Generalidades](#generalidades)
- [Configuración](#configuración)
- [Utilización](#utilización)
- [Incertidumbre](#incertidumbre)
- [Soporte](#soporte)
- [Contacto](#contacto)

## Generalidades

Este es un software comercial escrito en Python y desarrollado por un equipo de costarricenses que permite la ejecución de estrategias de trading automatizadas, exclusivamente para su operación en opciones binarias y digitales.
Mediante el analisis técnico y algoritmico, este software esta desarrollado para operar en escenarios donde encontramos periodos laterales y tendenciales, sin embargo antes de utilizarlo se deben de considerar lo siguiente:

1. Operamos bajo una lista de activos preestablecidos, con el fin de salvaguardar inversiones en mercados no deseados.
2. No consultamos si el mercado está activo para operar ni su profit esperado, debes asegurarte de esto por tu cuenta.
3. El periodo optimo es 200 periodos de 30 segundos con expiración de 5 minutos. No recomendamos otros periodos.
4. Utilizamos indicadores para analizar la tendencia, la confianza, los retrocesos, la oscilación, la velocidad, la fuerza y los patrones en las velas para poder determinar una decisión.

## Configuración

**Instalación local:**

No necesitas instalar el software, solo ejecutar. Pero es necesario tomar en cuenta que se deben modificar datos de la cuenta de iq option en el archivo .env antes de iniciar las operaciones.
No recomendamos el uso simultaneo del mismo software, ya que el servidor broker podria sobrecargarse de solicitudes y tomar medidas como el cierre de solicitud  a tu IP, entre otras.

## Utilización

Para ejecutar el robot, deberá proporcionar algunos datos de su cuenta de IQ Option.
Una vez que haya identificado esas piezas de información, puede ejecutar el robot. Aquí hay un ejemplo del archivo .env que debe contener la información para operar:

```python
user='example@gmail.com'
passwd='12345678'
mode='PRACTICE' # or REAL
bet=20 # Money
assets = ['NZDUSD','EURJPY','EURUSD']
market='binary' # or digital
expiration=5
candle=30 # candle size
period=200 
```

## Incertidumbre

**12 operaciones en una hora**
9 ganadas y 3 perdidas
75% probabilidad de acierto

**Señales exitosas**

Cantidad     Tendencia    Confianza    Retroceso    Oscilador    Velocidad    Fuerza    Patron    Resumen
-----------  -----------  -----------  -----------  -----------  -----------  --------  --------  ---------
1            put          ntr          put          put          put          ntr       put       put
1            


**Señales no exitosas**
Cantidad     Tendencia    Confianza    Retroceso    Oscilador    Velocidad    Fuerza    Patron    Resumen
-----------  -----------  -----------  -----------  -----------  -----------  --------  --------  ---------
1            put          ntr          put          call         call         ntr       ntr       put

## Machine Learning

**Etapas de un problema de machine learning**
Definir el problema: 

¿Qué se pretende predecir?
El precio de cierre de los proximos 5 minutos considerando el precio de apertura,maximo,minimo y cierre respectivamente.

10 = 50 * 0.2

50 velas de 30 segundos = 25 min
10 velas de 30 segundos = 5 min

target = 1 si el precio de cierre de la primer vela es menor al precio de cierre cierre actual, sino 0



50 para entrenamiento y 10 para probar


¿De qué datos se dispone?
Una cantidad considerable de 200 datos con posibilidad de aumentar y actualizar.

¿Qué datos es necesario conseguir?
El valor objetivo



Explorar y entender los datos que se van a emplear para crear el modelo.

Métrica de éxito: definir una forma apropiada de cuantificar cómo de buenos son los resultados obtenidos.

Preparar la estrategia para evaluar el modelo: separar las observaciones en un conjunto de entrenamiento, un conjunto de validación (o validación cruzada) y un conjunto de test. Es muy importante asegurar que ninguna información del conjunto de test participa en el proceso de entrenamiento del modelo.

Preprocesar los datos: aplicar las transformaciones necesarias para que los datos puedan ser interpretados por el algoritmo de machine learning seleccionado.

Ajustar un primer modelo capaz de superar unos resultados mínimos. Por ejemplo, en problemas de clasificación, el mínimo a superar es el porcentaje de la clase mayoritaria (la moda). En un modelo de regresión, la media de la variable respuesta.

Gradualmente, mejorar el modelo incorporando-creando nuevas variables u optimizando los hiperparámetros.

Evaluar la capacidad del modelo final con el conjunto de test para tener una estimación de la capacidad que tiene el modelo cuando predice nuevas observaciones.

Entrenar el modelo final con todos los datos disponibles.

## Contacto
Para informar problemas, errores, correcciones o proponer nuevas funciones utilice preferentemente tickets de Github. Para temas que requieran un enfoque más personal, no dude en enviar un correo electrónico a joeartisancr@gmail.com

## Comunidad
Si le gusta el software y siente que desea apoyar su desarrollo, mejoras y corrección de errores, entonces será de gran ayuda y muy apreciado si solo si: presenta errores, propuestas, solicitudes de extracción... 
Corre la voz con tu donación arbitraria.
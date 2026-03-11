from fastapi import FastAPI
import math
import json


app = FastAPI(
        title="API de Programación Agéntica - EPII Diurno",
        description="Elaborado por Steven Rey",
        version="1.0.0.",
        contact={
                "name": "Steven Rey",
                "email": "stevenalex0810@gmail.com",
        }
)

@app.get("/exercise/1")
def exercise_1():
    nombre = "Steven Rey"
    edad = 21
    activo = True

    return {
        "excercise": "1",
        "nombre": nombre,
        "edad": edad,
        "activo": activo,
        "tipo_nombre": str(type(nombre))
    }


@app.get("/exercise/2")
def exercise_2():
    a = 8
    b = 5

    return {
        "excercise": "2",
        "a": a,
        "b": b,
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
        "division": a / b,
        "modulo": a % b,
        "igual": a == b,
        "diferente": a != b,
        "mayor": a > b,
        "menor": a < b
    }

@app.get("/exercise/3")
def exercise_3():
    edad = 18

    if edad >= 18:
        resultado = "Mayor de edad"
    else:
        resultado = "Menor de edad"

    return {
        "excercise": "3",
        "edad": edad,
        "resultado": resultado
    }

@app.get("/exercise/4")
def exercise_4():
    frutas = ["manzana", "pera"]
    frutas.append("uva")

    coord = (10, 20)

    persona = {
        "nombre": "Juan",
        "edad": 25
    }

    return {
        "excercise": "4",
        "frutas": frutas,
        "coordenadas": coord,
        "persona": persona
    }


@app.get("/exercise/5")
def exercise_5():

    frutas = ["manzana", "pera", "uva"]

    recorrido = []
    for f in frutas:
        recorrido.append(f)

    numeros = []
    i = 0
    while i < 5:
        numeros.append(i)
        i += 1

    return {
        "excercise": "5",
        "frutas_recorridas": recorrido,
        "while_resultado": numeros
    }

@app.get("/exercise/6")
def exercise_6():

    def saludar(nombre):
        return "Hola " + nombre

    def sumar(a, b=0):
        return a + b

    return {
        "excercise": "6",
        "saludo": saludar("Steven"),
        "suma": sumar(5, 3)
    }


@app.get("/exercise/7")
def exercise_7():

    doble = lambda x: x * 2

    return {
        "excercise": "7",
        "numero": 4,
        "doble": doble(4)
    }

@app.get("/exercise/8")
def exercise_8():

    class Producto:
        def _init_(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio

    producto = Producto("Laptop", 2500)

    return {
        "excercise": "8",
        "producto": producto.nombre,
        "precio": producto.precio
    }

@app.get("/exercise/9")
def exercise_9():

    try:
        valor = int("abc")
    except:
        valor = "Error al convertir a entero"

    return {
        "excercise": "9",
        "resultado": valor
    }

@app.get("/exercise/10")
def exercise_10():

    numeros = list(range(1, 11))

    return {
        "excercise": "10",
        "numeros": numeros
    }

@app.get("/exercise/11")
def exercise_11():

    lista = [1, 2, 3, 4, 5]
    duplicada = [x * 2 for x in lista]

    return {
        "excercise": "11",
        "original": lista,
        "duplicada": duplicada
    }

@app.get("/exercise/12")
def exercise_12():

    a = 7
    b = 12

    mayor = a if a > b else b

    return {
        "excercise": "12",
        "numero1": a,
        "numero2": b,
        "mayor": mayor
    }

@app.get("/exercise/13")
def exercise_13():

    with open("data.txt", "w") as f:
        f.write("Hola desde FastAPI")

    with open("data.txt", "r") as f:
        contenido = f.read()

    return {
        "excercise": "13",
        "contenido_archivo": contenido
    }

@app.get("/exercise/14")
def exercise_14():

    data = {"nombre": "Pepito", "edad": 25}

    json_data = json.dumps(data)

    return {
        "excercise": "14",
        "dict": data,
        "json": json_data
    }

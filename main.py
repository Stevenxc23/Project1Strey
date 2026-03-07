from fastapi import FastAPI
import json
from pydantic import BaseModel
app = FastAPI()

@app.get("/nombre")
def taller_nombre():
    nombre = "Steven Rey"
    return {"resultado": nombre}

@app.get("/suma")
def taller_suma():
    num1, num2 = 15, 27
    return {
        "operacion": f"{num1} + {num2}",
        "resultado": num1 + num2
    }


@app.get("/validarpar")
def taller_par():
    numero = 8
    if numero % 2 == 0:
        return {"numero": numero, "mensaje": "Es par"}
    else:
        return {"numero": numero, "mensaje": "No es par"}

@app.get("/recorrer-lista")
def recorrer_lista():
    lista = [1, 2, 3, 4, 5]
    resultado = []
    for num in lista:
        resultado.append(num)
    return {"lista": resultado}

def multiplicar(a, b):
    return a * b

@app.get("/multiplicar")
def usar_multiplicar():
    return {"resultado": multiplicar(5, 3)}

@app.get("/persona")
def taller_persona():
    persona = {
        "nombre": "Steven",
        "edad": 22,
        "ciudad": "Barranquilla"
    }
    return persona

@app.get("/claves")
def mostrar_claves():
    persona = {
        "nombre": "Steven",
        "edad": 22,
        "ciudad": "Barranquilla"
    }
    return {"claves": list(persona.keys())}

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

@app.get("/producto")
def crear_producto():
    producto = Producto("Laptop", 2500)
    return {
        "nombre": producto.nombre,
        "precio": producto.precio
    }

@app.get("/try")
def usar_try():
    try:
        resultado = 10 / 2
        return {"resultado": resultado}
    except ZeroDivisionError:
        return {"error": "No se puede dividir por cero"}

@app.get("/lista-1-10")
def lista_1_10():
    return {"lista": list(range(1, 11))}

@app.get("/duplicar-lista")
def duplicar_lista():
    lista = [1, 2, 3, 4, 5]
    duplicada = [x * 2 for x in lista]
    return {"original": lista, "duplicada": duplicada}

@app.get("/mayor")
def mayor():
    a, b = 10, 20
    if a > b:
        return {"mayor": a}
    else:
        return {"mayor": b}

@app.get("/leer-archivo")
def leer_archivo():
    with open("archivo.txt", "r") as file:
        contenido = file.read()
    return {"contenido": contenido}

@app.get("/dict-json")
def dict_json():
    diccionario = {
        "nombre": "Steven",
        "curso": "Python"
    }
    return json.loads(json.dumps(diccionario))

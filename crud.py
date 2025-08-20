from flask import Flask

app = Flask(__name__)
productos = []

@app.route('/')
def inicio():
    return "Bienvenido al CRUD de productos"

@app.post('/crear')
def crear():
    productos.append({"nombre": "Producto fijo", "precio": 1000})
    return "Producto creado"

@app.get('/leer')
def leer():
    if productos:
        return f"Productos actuales: {productos}"
    return "No hay productos"


@app.put('/actualizar')
def actualizar():
    if productos:
        productos[0] = {"nombre": "Producto actualizado", "precio": 2000}
        return "Producto actualizado"
    return "No hay productos para actualizar"

@app.delete('/borrar')
def borrar():
    if productos:
        productos.pop(0)
        return "Producto eliminado"
    return "No hay productos para eliminar"

if __name__ == '__main__':
    app.run(debug=True)

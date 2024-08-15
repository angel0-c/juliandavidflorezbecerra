from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.secret_key =  'your_secret_key'

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/respuesta', methods=['POST'])
def respueta():
    if request.method =='POST':
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        suma = n1 + n2
        return render_template('formulario.html', res=suma)
    

@app.route('/formulari1', methods=['GET', 'POST'])
def formulari1():
    mayor = None
    menor = None
    error = None

    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            c = int(request.form['c'])

            if len({a, b, c}) != 3:
                error = "Los valores deben ser distintos."
            else:
                mayor = max(a, b, c)
                menor = min(a, b, c)

        except ValueError:
            error = "ingrese solo números enteros."

    return render_template('formulari1.html', mayor=mayor, menor=menor, error=error)

@app.route('/formulario2', methods=['GET', 'POST'])
def formulario2():
    mensaje = None  
    error_message = None  

    if request.method == 'POST':
        try:
            nota = int(request.form['nota'])

            if nota < 0 or nota > 20:
                error_message = "Error"
            elif nota >= 19:
                mensaje = "A"
            elif nota >= 16:
                mensaje = "B"
            elif nota >= 14:
                mensaje = "C"
            elif nota >= 11:
                mensaje = "D"
            else:
                mensaje = "E"
        except ValueError:
            error_message = "Error"
    return render_template('formulario2.html', mensaje=mensaje, error_message=error_message)


@app.route('/formulario3', methods=['GET', 'POST'])
def formulario3():
    pesos = None  
    error_message = None 
    if request.method == 'POST':
        try:
            total1 = int(request.form.get('total1', 0))
            total2 = int(request.form.get('total2', 0))
            total3 = int(request.form.get('total3', 0))
            total4 = int(request.form.get('total4', 0))
            total5 = int(request.form.get('total5', 0))

            dolar = total1 + total2 + total3 + total4 + total5
            pesos = dolar * 4000 
        except ValueError:
            error_message = "Error"
    return render_template('formulario3.html', pesos=pesos, error_message=error_message)


@app.route('/formulario4', methods=['GET', 'POST'])
def formulario4():
    resultado = None 
    if request.method == 'POST':
        try:
            numero = int(request.form['numero'])
            doble = numero * 2
            triple = numero * 3
            resultado = {'doble': doble,'triple': triple}
        except ValueError:
            resultado = "Error"
    return render_template('formulario4.html', resultado=resultado)
       
            
@app.route('/formulario5', methods=['GET', 'POST'])
def areformulario5():
    figura = None
    area_calculada = None
    error = None

    if request.method == 'POST':
        figura = request.form['figura']
        try:
            if figura == 'circulo':
                radio = float(request.form['radio'])
                area_calculada = 3.14159 * (radio ** 2)
            elif figura == 'cuadrado':
                lado = float(request.form['lado'])
                area_calculada = lado ** 2
            elif figura == 'rectangulo':
                largo = float(request.form['largo'])
                ancho = float(request.form['ancho'])
                area_calculada = largo * ancho
            elif figura == 'triangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                area_calculada = 0.5 * base * altura
            else:
                error = "Figura no válida."
        except ValueError:
            error = "ingrese valores válidos."

    return render_template('formulario5.html', figura=figura, area=area_calculada, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5020)

"""CREA UNA FUNCION IMPORTANTE QUE SOLO SEA UNO QUE SEA CAPAZ DE CALCULAR Y RETORNAR
EL AREA DE UN POLIGONO

- LA FUNCION RECIBIRA POR PARAMETRO SOLO UN POLIGONO A LA VEZ
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo."""

def area_poligono (base, altura, poligono):#creo la funcion con tres argumentos uno para la base otro para la altura y por ultimo el poligono que queremos calcular que debe introducirse como una cadena de texto
    if poligono == "triangulo":
        area = (base*altura)/2
        return f"Es un Triángulo cuaya area es {area}"
    elif poligono == "cuadrado" and base == altura: 
        area = base * altura
        return f"Es un cuadrado cuaya area es {area}"
    elif poligono == "rectangulo" and base != altura:
        area = base * altura
        return f"Es un rectangulo cuaya area es {area}"

print(area_poligono(4, 4, "cuadrado"))
    
Total_productos=int(input("Ingresa el número total de productos: "))
for i in range(Total_productos):
    Producto=(input("Ingresa el nombre del producto: ")) 
    print()
    Stock=float(input("Ingresa la cantidad de stock: "))
    print()
    Stockvendido=int(input("ingresa la cantidad de stock vendido: "))
    print()
    if Stockvendido>Stock:
     print("No puedes vender mas producto del que tienes, tendras que volver a ejecutar este programa :V")
     break
     
    else:
     Precio=float(input("Ingresa el precio de compra del producto: "))
    print()
    Ventas=float(input("Ingresa el precio de venta del producto: "))
    print()
    
    stockrestante=Stock-Stockvendido
    Gasto=Precio*Stockvendido
    Ganancia=Ventas*Stockvendido-Gasto
    print("El costo total es de: ", Gasto)
  
    print("La ganancia total es de: ", Ganancia)
  
    print("el stock que queda es: ",stockrestante,"Productos")

    p1=Ganancia*100/Gasto
    print("El porcentaje de ganancia es de: ", p1, "%")
    print()
  
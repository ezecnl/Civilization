inventario={"Madera":100,"Piedra":10}
costo={"Madera":20,"Piedra":30}
def eliminar(cantidad, material):
    inventario[material] -= cantidad

def puedo_contruir():
    construccion= True
    for tipo,costos in costo.items():
        if costos > inventario[tipo]:
            construccion=False
    return construccion

print(len(inventario))
for tipo,cantidad in costo.items():
    eliminar(cantidad,tipo)
    print(inventario)

print(puedo_contruir()) 
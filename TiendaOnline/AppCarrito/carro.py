class Carro:
    #52
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={} #Si no hay carro, este esta vacio
            
        self.carro=carro #Si ya habia carro, este se mantiene igual, si el usuario se va de la pag y regresa, se mantendra como antes

    def agregar(self, producto):
        #Hay que comprobar que el ID de producto no este en el carro, si no se encuentra, se puede agregar
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        #Si el producto YA ESTA en el carro, 53
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1 #Si se encuentra el ID dentro del carro le agrega 1 unidad
                    value["precio"]=round(float(value["precio"])+producto.precio, 2)
                    break
        #Con esto el carro se va guardando automaticamente
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro() #Despues de eliminar el producto lo guardamos en la sesion

    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1 #Mismo funcionamiento que al agregar, pero -1
                    value["precio"]=round(float(value["precio"])-producto.precio, 2)
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    def vaciar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
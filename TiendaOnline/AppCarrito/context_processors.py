def importe_total_carro(request):
    total=0
    if 'carro' in request.session:
     for key, value in request.session['carro'].items():
          total= round(total+float(value["precio"]), 2)
                   
    return {"importe_total_carro":total}
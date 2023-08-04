# SDK de Mercado Pago
import mercadopago
# Agrega credenciales
sdk = mercadopago.SDK("TEST-2071872890123355-050618-8d5329a2130183372953cd41b03606f2-155614857")


# Crea un ítem en la preferencia
preference_data = {
    "items": [
        {
            "title": "Mi producto",
            "quantity": 1,
            "unit_price": 75.76,
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]
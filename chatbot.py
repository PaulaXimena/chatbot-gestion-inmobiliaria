import json
import os


# ============================
# 1) Datos de ejemplo
# ============================
propiedades = [
    {
        "id": 1,
        "tipo": "departamento",
        "barrio": "Palermo",
        "ambientes": 2,
        "precio": 250000,
        "operacion": "venta",
        "moneda":"Dolar"
    },
    {
        "id": 2,
        "tipo": "casa",
        "barrio": "Villa Urquiza",
        "ambientes": 4,
        "precio": 350000,
        "operacion": "venta",
        "moneda":"Dolar"
    },
    {
        "id": 3,
        "tipo": "departamento",
        "barrio": "Belgrano",
        "ambientes": 3,
        "precio": 900,
        "operacion": "alquiler",
        "moneda":"Pesos"
    },


    { "id": 5, 
     "tipo": "departamento",
       "barrio": "Villa del parque", 
       "ambientes": 1,
         "precio": 250000,
         "operacion": "venta",
         "moneda":"Dolar"
    },



    { "id": 6, 
     "tipo": "departamento",
       "barrio": "Belgrano", 
       "ambientes": 3,
         "precio": 500000,
         "operacion": "alquiler",
         "moneda":"Pesos"
    },


    { "id": 7, 
     "tipo": "Casa",
       "barrio": "Belgrano", 
       "ambientes": 2,
         "precio": 350000,
         "operacion": "alquiler",
         "moneda":"Pesos"
    },



    { "id": 8, 
     "tipo": "departamento",
       "barrio": "Belgrano", 
       "ambientes": 3,
         "precio": 550000,
         "operacion": "alquiler",
         "moneda":"Pesos"
    },


    { "id": 9, 
     "tipo": "departamento",
       "barrio": "Palermo", 
       "ambientes": 1,
         "precio": 250000,
         "operacion": "alquiler",
         "moneda":"Pesos"
    },

 { "id": 10, 
     "tipo": "departamento",
       "barrio": "Palermo", 
       "ambientes": 2,
         "precio": 300000,
         "operacion": "alquiler",
         "moneda":"Pesos"
    },
 { "id": 11, 
     "tipo": "departamento",
       "barrio": "Palermo", 
       "ambientes": 3,
         "precio": 400000,
         "operacion": "alquiler",
         "moneda":"Pesos"
    },


     { "id": 12, 
     "tipo": "departamento",
       "barrio": "Palermo", 
       "ambientes": 2,
         "precio": 250000,
         "operacion": "Venta",
         "moneda":"Dolar"
    },

{ "id": 13, 
     "tipo": "departamento",
       "barrio": "Villa del parque", 
       "ambientes": 2,
         "precio": 350000,
         "operacion": "venta",
         "moneda":"Dolar"
    },


    
{ "id": 14, 
     "tipo": "casa",
       "barrio": "Villa del parque", 
       "ambientes": 2,
         "precio": 350000,
         "operacion": "venta",
         "moneda":"Dolar"
    },



{ "id": 14, 
     "tipo": "departamento",
       "barrio": "Villa del parque", 
       "ambientes": 3,
         "precio": 350000,
         "operacion": "alquiler",
         "moneda":"Pesos"
    },


{ "id": 15, 
     "tipo": "departamento",
       "barrio": "Villa del parque", 
       "ambientes": 2,
         "precio": 250000,
         "operacion": "alquiler",
         "moneda":"Pesos"
    },


]

# 🔹 Almacenamiento local
# =======================
DATA_FILE = "conversaciones.json"
usuarios = {}

def guardar_datos():
    """Guarda todas las conversaciones en un archivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

# =======================
# 🔹 Lógica del chatbot
# =======================
def chatbot_respuesta(user_id, mensaje):
    mensaje = mensaje.strip().lower()
    user = usuarios.setdefault(user_id, {
        "estado": "inicio",
        "nombre": "",
        "direccion": "",
        "telefono": "",
        "operacion": "",
        "tipo_propiedad": "",
        "ambientes": "",
        "barrio": "",
        "garantia": "",
        "tipo_venta": "",
        "conversacion": []
    })

    user["conversacion"].append({"usuario": mensaje})
    estado = user["estado"]
    respuesta = ""

    # Cambia este número al de tu asesor:
    whatsapp_numero = "541134921552"
    whatsapp_link = f"https://wa.me/{whatsapp_numero}?text=Hola!+Vengo+del+chatbot+y+quiero+más+información+sobre+una+propiedad."

    # === Flujo ===
    if estado == "inicio":
        respuesta = "¡Hola!Bienvenido  👋 Soy el asistente virtual  de Inmobiliaria Sur, estoy aqui  para ayudarte, para iniciar voy a necesitar algo de informacion. comencemos,  . ¿Podrías decirme tu *nombre y apellido*?"
        user["estado"] = "pidiendo_nombre"

    elif estado == "pidiendo_nombre":
        user["nombre"] = mensaje.title()
        respuesta = f"Encantado, {user['nombre']} ahora  podrias darme algunos datos sobre tu ubicacion y lo ue estas buscando. ¿Podrías darme tu *dirección*?"
        user["estado"] = "pidiendo_direccion"

    elif estado == "pidiendo_direccion":
        user["direccion"] = mensaje
        respuesta = "Perfecto 👍. ¿Podrías dejarme tu *teléfono de contacto*?"
        user["estado"] = "pidiendo_telefono"

    elif estado == "pidiendo_telefono":
        user["telefono"] = mensaje
        respuesta = "Gracias. ¿Por qué operación te comunicás? ¿*Venta* o *alquiler*?"
        user["estado"] = "pidiendo_operacion"

    elif estado == "pidiendo_operacion":
        if "alquiler" in mensaje:
            user["operacion"] = "alquiler"
            respuesta = f"Entendido, {user['nombre']}. ¿Buscás una *casa* o un *departamento*?"
            user["estado"] = "pidiendo_tipo"
        elif "venta" in mensaje:
            user["operacion"] = "venta"
            respuesta = "Perfecto. ¿Querés *comprar* o *vender* una propiedad?"
            user["estado"] = "pidiendo_venta_tipo"
        else:
            respuesta = "Por favor, indicá si es *venta* o *alquiler*."

    # === Flujo de ALQUILER ===
    elif estado == "pidiendo_tipo":
        user["tipo_propiedad"] = mensaje
        respuesta = "¿De cuántos ambientes la estás buscando?"
        user["estado"] = "pidiendo_ambientes"

    elif estado == "pidiendo_ambientes":
        if mensaje.isdigit():
            user["ambientes"] = int(mensaje)
            respuesta = "¿En qué barrio te gustaría buscar? Tenemos *Belgrano, Palermo, Villa del Parque* y *Villa Urquiza*."
            user["estado"] = "pidiendo_barrio"
        else:
            respuesta = "Por favor, indicá un número de ambientes (por ejemplo: 2)."

    elif estado == "pidiendo_barrio":
        user["barrio"] = mensaje.title()
        respuesta = "¿Tenés *seguro de caución* o *garantía propietaria*?"
        user["estado"] = "pidiendo_garantia"

    elif estado == "pidiendo_garantia":
        user["garantia"] = mensaje
        barrio = user["barrio"]
        ambientes = user["ambientes"]
        tipo = user["tipo_propiedad"]

        filtradas = [
            p for p in propiedades
            if p["operacion"] == "alquiler"
            and tipo in p["tipo"]
            and p["barrio"].lower() == barrio.lower()
            and p["ambientes"] == ambientes
        ]

        if filtradas:
            respuesta = "Encontré estas opciones:\n"
            for p in filtradas:
                respuesta += f"- {p['tipo'].capitalize()} en {p['barrio']} ({p['ambientes']} amb.) — ${p['precio']}\n"
        else:
            respuesta = "No encontré propiedades con esas características, pero puedo buscar algo similar."

        respuesta += f"""<br>Un asesor puede ayudarte con más detalles.<br><a href="{whatsapp_link}" target="_blank" style="background-color:#25D366;color:white;padding:8px 12px;border-radius:8px;text-decoration:none;">📲 Hablar por WhatsApp </a>"""
        user["estado"] = "fin"

    # === Flujo de VENTA ===
    elif estado == "pidiendo_venta_tipo":
        if "comprar" in mensaje:
            user["tipo_venta"] = "comprar"
            respuesta = "Perfecto. ¿De cuántos ambientes te interesa?"
            user["estado"] = "venta_ambientes"
        elif "vender" in mensaje:
            user["tipo_venta"] = "vender"
            respuesta =f"""<br>Un asesor puede ayudarte con más detalles.<br><a href="{whatsapp_link}" target="_blank" style="background-color:#25D366;color:white;padding:8px 12px;border-radius:8px;text-decoration:none;">📲 Hablar por WhatsApp </a>"""

            user["estado"] = "fin"
        else:
            respuesta = "¿Querés *comprar* o *vender*?"

    elif estado == "venta_ambientes":
        if mensaje.isdigit():
            user["ambientes"] = int(mensaje)
            respuesta = "¿En qué barrio buscás? Tenemos *Belgrano, Palermo* y *Villa del Parque*."
            user["estado"] = "venta_barrio"
        else:
            respuesta = "Por favor, indicá un número de ambientes válido."

    elif estado == "venta_barrio":
        user["barrio"] = mensaje.title()
        barrio = user["barrio"]
        ambientes = user["ambientes"]

        filtradas = [
            p for p in propiedades
            if p["operacion"] == "venta"
            and p["barrio"].lower() == barrio.lower()
            and p["ambientes"] == ambientes
        ]

        if filtradas:
            respuesta = "Estas son las propiedades disponibles:\n"
            for p in filtradas:
                respuesta += f"- {p['tipo'].capitalize()} en {p['barrio']} ({p['ambientes']} amb.) — u$s {p['precio']}\n"
        else:
            respuesta = "No tenemos propiedades con esas características exactas, pero puedo buscar algo similar."

        respuesta += f"""<br>Un asesor puede ayudarte con más detalles.<br><a href="{whatsapp_link}" target="_blank" style="background-color:#25D366;color:white;padding:8px 12px;border-radius:8px;text-decoration:none;">📲 Hablar por WhatsApp </a>"""

        user["estado"] = "fin"

    elif estado == "fin":
        respuesta = "Gracias por comunicarte con nosotros. ¿Querés iniciar otra consulta? 😊"
        user["estado"] = "inicio"

    # === Guardar y devolver ===
    user["conversacion"].append({"bot": respuesta})
    guardar_datos()
    return respuesta
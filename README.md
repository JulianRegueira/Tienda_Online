# Tienda_Online
 
Instalar las dependencias necesarias para la correcta ejecucion del proyecto:<p>
pip install -r requirements.txt<p>

En el archivo settings.py modificar las siguientes lineas:<p>

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"<p>
EMAIL_HOST = "smtp.gmail.com"<p>
EMAIL_PORT = 587<p>
EMAIL_HOST_USER = "EMAIL_HOST_USER" > por tu mail personal<p>
EMAIL_HOST_PASSWORD = "EMAIL_HOST_PASSWORD" > por la contraseña generada en el link de abajo<p>
EMAIL_USE_TLS = True<p>

Generador de contraseña: https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4PHriUOOK3aJkaolCNy2-4OVpeYM7QCPdCDa2zglwj0bMbLPMV2WD7cRacLLZbik3ti8twpVRIto1LW2Xp-yMfuLa5fHw<p>

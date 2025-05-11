from django.shortcuts import render
import requests

def buscar_clima(request):
    clima_info = None
    chiste = None
    sismos = None
    error = None

    if request.method == 'POST':
        if 'buscar_clima' in request.POST:
            ciudad = request.POST.get('ciudad')
            api_key = '45e4061aa0fb2711712736eb989e4826'  # Reemplaza con tu API key de OpenWeather
            url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'

            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                data = respuesta.json()
                clima_info = {
                    'ciudad': ciudad,
                    'temperatura': data['main']['temp'],
                    'descripcion': data['weather'][0]['description'],
                    'icono': data['weather'][0]['icon']
                }
            else:
                error = 'Ciudad no encontrada.'

        elif 'obtener_chiste' in request.POST:
            r = requests.get('https://api.chucknorris.io/jokes/random')
            if r.status_code == 200:
                chiste = r.json()['value']
            else:
                error = 'No se pudo obtener el chiste.'

        elif 'obtener_sismos' in request.POST:
            r = requests.get('https://api.gael.cloud/general/public/sismos')
            if r.status_code == 200:
                sismos = r.json()
            else:
                error = 'No se pudo obtener la información de sismos.'

    return render(request, 'clima/buscar.html', {
        'clima': clima_info,
        'chiste': chiste,
        'sismos': sismos,
        'error': error
    })

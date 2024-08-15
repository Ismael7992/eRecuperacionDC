from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Piloto

def home(request):
    return render (request, "home.html")

def listadoPilotos(request):
    pilotosBdd = Piloto.objects.all()
    return render(request, "listadoPilotos.html", {'pilotos': pilotosBdd})

def eliminarPiloto(request, id):
    pilotoEliminar = Piloto.objects.get(id=id)
    pilotoEliminar.delete()
    messages.success(request, "Piloto eliminado exitosamente.")
    return redirect('listadoPilotos')

def nuevoPiloto(request):
    return render(request, 'nuevoPiloto.html')

def guardarPiloto(request):
    dni = request.POST["dni"]
    primer_apellido = request.POST["primer_apellido"]
    segundo_apellido = request.POST["segundo_apellido"]
    nombres = request.POST["nombres"]
    email = request.POST["email"]
    numero_celular = request.POST["numero_celular"]
    foto_carnet = request.FILES.get("foto_carnet")
    hoja_vida_pdf = request.FILES.get("hoja_vida_pdf")
    nuevoPiloto = Piloto.objects.create(dni=dni,primer_apellido=primer_apellido,segundo_apellido=segundo_apellido,nombres=nombres,email=email,numero_celular=numero_celular,foto_carnet=foto_carnet,hoja_vida_pdf=hoja_vida_pdf)
    messages.success(request, "Piloto guardado exitosamente.")
    return redirect('listadoPilotos')

def editarPiloto(request, id):
    pilotoEditar = Piloto.objects.get(id=id)
    return render(request, 'editarPiloto.html', {'pilotoEditar': pilotoEditar})

def procesarActualizacionPiloto(request):
    id = request.POST["id"]
    dni = request.POST["dni"]
    primer_apellido = request.POST["primer_apellido"]
    segundo_apellido = request.POST["segundo_apellido"]
    nombres = request.POST["nombres"]
    email = request.POST["email"]
    numero_celular = request.POST["numero_celular"]

    pilotoConsultado = Piloto.objects.get(id=id)
    pilotoConsultado.dni = dni
    pilotoConsultado.primer_apellido = primer_apellido
    pilotoConsultado.segundo_apellido = segundo_apellido
    pilotoConsultado.nombres = nombres
    pilotoConsultado.email = email
    pilotoConsultado.numero_celular = numero_celular

    # Actualizar foto_carnet y hoja_vida_pdf solo si se han enviado nuevos archivos
    if 'foto_carnet' in request.FILES:
        pilotoConsultado.foto_carnet = request.FILES['foto_carnet']
    if 'hoja_vida_pdf' in request.FILES:
        pilotoConsultado.hoja_vida_pdf = request.FILES['hoja_vida_pdf']

    pilotoConsultado.save()
    messages.success(request, "Piloto actualizado correctamente.")
    return redirect('listadoPilotos')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Avion, Piloto

def home(request):
    return render(request, "home.html")

def listadoAviones(request):
    avionesBdd = Avion.objects.all()
    return render(request, "listadoAviones.html", {'aviones': avionesBdd})

def eliminarAvion(request, id):
    avionEliminar = Avion.objects.get(id=id)
    avionEliminar.delete()
    messages.success(request, "Avión eliminado exitosamente.")
    return redirect('listadoAviones')

def nuevoAvion(request):
    pilotos = Piloto.objects.all()  # Obtenemos todos los pilotos para seleccionar
    return render(request, 'nuevoAvion.html', {'pilotos': pilotos})

def guardarAvion(request):
    nombre = request.POST["nombre"]
    marca = request.POST["marca"]
    numero_matricula = request.POST["numero_matricula"]
    capacidad = request.POST["capacidad"]
    ano_creacion = request.POST["ano_creacion"]
    fotografia = request.FILES.get("fotografia")
    piloto_id = request.POST["piloto"]  # Recibimos el ID del piloto seleccionado

    piloto = Piloto.objects.get(id=piloto_id)  # Buscamos el piloto por ID

    nuevoAvion = Avion.objects.create(
        nombre=nombre, 
        marca=marca, 
        numero_matricula=numero_matricula, 
        capacidad=capacidad, 
        ano_creacion=ano_creacion, 
        fotografia=fotografia, 
        piloto=piloto
    )

    messages.success(request, "Avión guardado exitosamente.")
    return redirect('listadoAviones')

def editarAvion(request, id):
    avionEditar = Avion.objects.get(id=id)
    pilotos = Piloto.objects.all()  # Obtenemos todos los pilotos para seleccionar
    return render(request, 'editarAvion.html', {'avionEditar': avionEditar, 'pilotos': pilotos})

def procesarActualizacionAvion(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    marca = request.POST["marca"]
    numero_matricula = request.POST["numero_matricula"]
    capacidad = request.POST["capacidad"]
    ano_creacion = request.POST["ano_creacion"]
    piloto_id = request.POST["piloto"]  # Recibimos el ID del piloto seleccionado

    avionConsultado = Avion.objects.get(id=id)
    avionConsultado.nombre = nombre
    avionConsultado.marca = marca
    avionConsultado.numero_matricula = numero_matricula
    avionConsultado.capacidad = capacidad
    avionConsultado.ano_creacion = ano_creacion

    piloto = Piloto.objects.get(id=piloto_id)  # Buscamos el piloto por ID
    avionConsultado.piloto = piloto  # Asignamos el nuevo piloto

    # Actualizar la fotografía solo si se ha enviado un nuevo archivo
    if 'fotografia' in request.FILES:
        avionConsultado.fotografia = request.FILES['fotografia']

    avionConsultado.save()
    messages.success(request, "Avión actualizado correctamente.")
    return redirect('listadoAviones')

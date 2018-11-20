from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm
# Para Login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def pacientes_listar(request):
    pacientes = Paciente.objects.all();
    return render(request, 'pacientes.html', {'pacientes' : pacientes})

@login_required
def paciente_criar(request):
    form = PacienteForm(request.POST or None, request.FILES or None) #Se chamarem essa função com um POST ela vai vir com o form preenchido, caso não, virá vazio

    if form.is_valid():
        form.save()
        return redirect('pacientes_listar')
    return render(request, 'paciente_form.html', {'form': form})

@login_required
def paciente_atualizar(request, id):
    paciente = get_object_or_404(Paciente, pk=id) # vai procurar a pessoa pela primary key ID
    form = PacienteForm(request.POST or None, request.FILES or None, instance=paciente) # No paciente_criar não tem virgula, é or None também
    # A diferença agora do form é que ele já virá instanciado com a pessoa que pegamos com o ID

    if form.is_valid():
        form.save()
        return redirect('pacientes_listar')

    return render(request, 'paciente_form.html', {"form" : form})
    # renderizaremos o mesmo Template, agora populada, e mandaremos pro template o form

@login_required
def paciente_deletar(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    # Você cria o form abaixo apenas se quiser, caso queira que exiba na tela de confirmação de deleção
    form = PacienteForm(request.POST or None, request.FILES or None, instance=paciente)

    if request.method == "POST":
        paciente.delete()
        return redirect('pacientes_listar')

    #Assim podemos retornar mais de uma coisa no render. Se você quiser visualizar o form na deleção ou só o nome do paciente
    return render(request, 'paciente_confirmacao_deletar.html', {'form' : form, 'paciente' : paciente})

import json
import interface
import inferencia

with open("regras.json", "r") as f:
    regras = json.load(f)

# print(regras)

fatos = []
inputs = []
interface.Interface(inputs)

fatos.append({ 'input_sistema': inputs[1].get()})
fatos.append({ 'input_biometria':  inputs[13].get()})
fatos.append({ 'input_nfc': inputs[12].get()})
fatos.append({ 'input_armazenamento': inputs[3].get()})
fatos.append({ 'input_conexao': inputs[11].get()})





celular = inferencia.encadeamento_frente('celular', fatos, regras)

print(celular['modelo'])
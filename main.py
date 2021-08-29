import json
import interface
import inferencia
import resultado

with open("regras.json", "r") as f:
    regras = json.load(f)

fatos = []
inputs = []
interface.Interface(inputs)

fatos.append({ 'input_sistema': inputs[1].get()})
fatos.append({ 'input_preco': inputs[2].get()})
fatos.append({ 'input_armazenamento': inputs[3].get()})
fatos.append({ 'input_ram': inputs[4].get()})
fatos.append({ 'input_chip': inputs[5].get()})
fatos.append({ 'input_cam_traseira': inputs[6].get()})
fatos.append({ 'input_cam_frontal': inputs[7].get()})
fatos.append({ 'input_res_filmagem': inputs[8].get()})
fatos.append({ 'input_tela': inputs[9].get()})
fatos.append({ 'input_bateria': inputs[10].get()})
fatos.append({ 'input_conexao': inputs[11].get()})
fatos.append({ 'input_nfc': inputs[12].get()})
fatos.append({ 'input_biometria':  inputs[13].get()})
fatos.append({ 'input_agua':  inputs[14].get()})
fatos.append({ 'input_sem_fio':  inputs[15].get()})

celular = inferencia.encadeamento_frente('celular', fatos, regras)

resultado.mostrar_resultado(celular)
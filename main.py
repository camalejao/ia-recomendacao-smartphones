import json
import interface
import inferencia

with open("regras.json", "r") as f:
    regras = json.load(f)

# print(regras)

fatos = []

interface.showOS()
fatos.append({ 'input_sistema': int(input()) })

interface.showBio()
fatos.append({ 'input_biometria': int(input()) })

interface.showNFC()
fatos.append({ 'input_nfc': int(input()) })

interface.showArmazenamento()
fatos.append({ 'input_armazenamento': int(input()) })

interface.showConexao()
fatos.append({ 'input_conexao': int(input()) })

celular = inferencia.encadeamento_frente('celular', fatos, regras)

print(celular['modelo'])
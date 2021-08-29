def encadeamento_frente(goal, fatos, regras):
    while not check_goal(goal, fatos):

        add = False
        
        for r in regras:

            if check_goal(goal, fatos):
                break

            if r['aplicada']:
                continue
            
            match = True    

            for ant in r['ant']:
                if not ant in fatos:
                    match = False

            if match:
                # print('regra: ', r)
                r['aplicada'] = True
                for f in r['con']:
                    fatos.append(f)
                    add = True
        
        if not add:
            break
    
    celular = {'modelo': 'desconhecido', 'imagem': './img/desconhecido.png', 'descricao': 'Não conseguimos encontrar um modelo adequado para suas preferências.'}
    for f in fatos:
        if 'celular' in f:
            celular = f['celular']
    return celular

def check_goal(goal, fatos):
    for f in fatos:
        if goal in f:
            return True
    
    return False
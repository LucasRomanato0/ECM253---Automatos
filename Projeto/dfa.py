import sys

def simular_dfa(dfa, entrada):
    estado = dfa.initial_state


    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: dfa <nome_arquivo>")
        sys.exit
    
    with open(sys.argv[1]) as dfa_file:
        dfa_data = dfa_file.read()
    dfa = eval(dfa_data)
    # Para conferir o conteúdo
    print(dfa)
    print (dfa['initial_state'])

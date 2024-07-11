import os

class DeterministicFiniteAutomaton:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def process(self, word):
        current_state = self.q0
        for symbol in word:
            if symbol in self.Sigma:
                current_state = self.delta.get((current_state, symbol), None)
                if current_state is None:
                    return "INVÁLIDA"
            else:
                return "INVÁLIDA"
        if current_state in self.F:
            return "ACEITA"
        else:
            return "REJEITA"

def load_automata(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        Sigma = lines[0].strip().split()
        Q = lines[1].strip().split()
        F = lines[2].strip().split()
        q0 = lines[3].strip()

        delta = {}
        for line in lines[4:]:
            parts = line.strip().split()
            if len(parts) == 3:
                origin, symbol, destination = parts
                delta[(origin, symbol)] = destination

        return Q, Sigma, delta, q0, F
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
        return None, None, None, None, None

# Caminho do arquivo para a pasta Documentos do usuário
documents_path = os.path.expanduser("~/Documents")
filename = os.path.join(documents_path, 'automata_definition.txt')

# Exemplo de uso
Q, Sigma, delta, q0, F = load_automata(filename)
if Q and Sigma and delta and q0 and F:
    dfa = DeterministicFiniteAutomaton(Q, Sigma, delta, q0, F)
    result = dfa.process(['a', 'b', 'a'])
    print(result)
else:
    print("Não foi possível carregar o autômato devido a um erro no carregamento do arquivo.")

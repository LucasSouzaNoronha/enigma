# enigma
MÁQUINA ENIGMA EM PYTHON

Este é um programa em Python que simula o funcionamento da máquina Enigma. O usuário fornece uma mensagem e define as posições iniciais das três roldanas. A mensagem é então cifrada ou decifrada com base na rotação automática dos rotores e na lógica do refletor. O programa trabalha com um alfabeto estendido (a–z, ç e espaço) e retorna o resultado da cifra letra por letra.

FUNCIONALIDADES

- Roldanas configuráveis (3 roldanas com posições iniciais definidas)
- Refletor simétrico
- Alfabeto com 28 caracteres (a–z, ç e espaço)
- Rotação automática das rodanas com entalhes
- Entrada limpa (ignora caracteres inválidos)

COMO USAR

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
2. Baixe o arquivo enigma.ipynb.
3. Execute.
4. Defina as roldanas entre 0 e 27.
5. Insira a mensagem.

LÓGICA UTILIZADA

1. A letra passa pelos três rotores (ida)
2. É refletida
3. Volta pelos rotores na ordem reversa
4. A posição das roldanas avança automaticamente após cada letra processada

EXEMPLO DE USO

1. Digite a configuração da primeira roldana: 1
2. Digite a configuração da segunda roldana: 0
3. Digite a configuração da terceira roldana: 0
4. Digite a mensagem a ser codificada ou decodificada: teste
5. Mensagem cifrada/decifrada: bhmnb
6. Repita a execução do programa e insira a mensagem codificada para decodificar

FUTURAS MELHORIAS

- Implementar plugboard (tabuleiro de conexões)
- Salvar/recuperar configurações
- Interface gráfica com Tkinter ou PyQt
- Exportar mensagens cifradas para arquivo

AUTOR Lucas Noronha
Junho/2025

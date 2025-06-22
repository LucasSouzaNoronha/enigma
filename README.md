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

Certifique-se de ter o Python instalado (versão 3.6 ou superior).
Baixe o arquivo enigma.ipynb.
Execute.
Defina as roldanas entre 0 e 27.
Insira a mensagem.

LÓGICA UTILIZADA

1. A letra passa pelos três rotores (ida)
2. É refletida
3. Volta pelos rotores na ordem reversa
4. A posição das roldanas avança automaticamente após cada letra processada

EXEMPLO DE USO

Digite a configuração da primeira roldana: 1
Digite a configuração da segunda roldana: 0
Digite a configuração da terceira roldana: 0
Digite a mensagem a ser codificada ou decodificada: teste

Mensagem cifrada/decifrada: bhmnb

Repita a execução do programa e insira a mensagem codificada para decodificar

FUTURAS MELHORIAS

- Implementar plugboard (tabuleiro de conexões)
- Salvar/recuperar configurações
- Interface gráfica com Tkinter ou PyQt
- Exportar mensagens cifradas para arquivo

AUTOR Lucas Noronha
Junho/2025

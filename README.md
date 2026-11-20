# TCP — Estudos de Redes e Sockets em Python

Projeto **feito de forma totalmente educacional** para estudar, na prática, como
funcionam os protocolos de rede e a programação de *sockets* em Python. O objetivo
não é criar uma ferramenta de produção, e sim entender o que acontece "por baixo"
quando dois computadores conversam pela rede: TCP, UDP e SSH.

> ⚠️ **Aviso**
> Todo o código aqui tem **fins exclusivamente educacionais** e de estudo pessoal.
> As funcionalidades (incluindo o cliente SSH e o exemplo de *reverse shell*) devem
> ser usadas **apenas em máquinas e redes próprias ou em ambientes de laboratório
> com autorização**. Usar isso contra sistemas de terceiros sem permissão é ilegal.

## Estrutura do projeto

```
TCP/
├── server/
│   ├── server_tcp.py   # Servidor TCP que aceita uma conexão e troca mensagens
│   └── client_tcp.py   # Cliente TCP que conecta e envia uma requisição crua
├── UDP/
│   └── client_udp.py   # Cliente UDP que envia/recebe datagramas
└── SSH/
    └── ssh_client.py   # Cliente SSH (paramiko) com modo texto e reverse shell
```

## O que cada parte faz

### TCP (`server/`)
- **`server_tcp.py`** — cria um socket `SOCK_STREAM`, faz `bind` na porta `4433`,
  escuta (`listen`) e aceita (`accept`) uma conexão. Depois entra em um laço
  recebendo (`recv`) e enviando (`send`) mensagens com o cliente.
- **`client_tcp.py`** — cria um socket TCP, conecta no servidor e envia um cabeçalho
  HTTP cru só para observar a troca de bytes na conexão.

### UDP (`UDP/`)
- **`client_udp.py`** — usa um socket `SOCK_DGRAM` para enviar datagramas com
  `sendto` e recebê-los com `recvfrom`, mostrando como o UDP funciona **sem
  conexão** (diferente do TCP).

### SSH (`SSH/`)
- **`ssh_client.py`** — cliente SSH usando a biblioteca `paramiko`. Pede host,
  usuário e senha, conecta e oferece dois modos:
  1. **Free Texting** — executar comandos no servidor remoto interativamente.
  2. **Reverse Shell** — exemplo de estudo de *reverse shell* com `netcat`.

## Como executar

Requisitos: Python 3 e, para o cliente SSH, a biblioteca `paramiko`.

```bash
# criar/ativar o ambiente virtual (opcional)
python -m venv venv
# instalar a dependência do SSH
pip install paramiko
```

Exemplo com TCP (em dois terminais):

```bash
# terminal 1
python server/server_tcp.py
# terminal 2
python server/client_tcp.py
```

## O que eu aprendi com este projeto

- A diferença prática entre **TCP** (orientado a conexão, confiável, com
  `listen`/`accept`) e **UDP** (sem conexão, baseado em datagramas com
  `sendto`/`recvfrom`).
- Como criar **sockets** em Python do zero: escolher família de endereço (`AF_INET`,
  IPv4) e tipo de socket (`SOCK_STREAM` para TCP, `SOCK_DGRAM` para UDP).
- O ciclo de vida de uma conexão TCP: `bind` → `listen` → `accept` → `recv`/`send`
  → `close`.
- Como os dados trafegam como **bytes** e a necessidade de fazer `encode`/`decode`
  (UTF-8) ao enviar e receber texto.
- A estrutura de uma **requisição HTTP crua**, enviando o cabeçalho manualmente
  pelo socket.
- Como usar a biblioteca **`paramiko`** para automatizar conexões **SSH** e
  executar comandos remotos com `exec_command`, lendo `stdout` e `stderr`.
- O conceito de **reverse shell** e por que ele é relevante em segurança da
  informação — entendendo o funcionamento para poder **defender** sistemas.
- A importância de **tratar erros** (`try/except`) e de fechar conexões corretamente.

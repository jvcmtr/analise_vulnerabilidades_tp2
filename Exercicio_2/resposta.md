# Exercício 2

### Contexto

Encerrada a fase passiva, é hora do reconhecimento ativo. A Vetor Security pede o mapeamento completo da superfície de ataque do crAPI usando ferramentas de varredura de porta e descoberta de endpoints, além da identificação de tecnologias de backend usadas pela aplicação. 

Diferente da fase passiva, aqui o tráfego gerado é direto e detectável, então cada varredura precisa estar dentro do escopo já autorizado no documento de RoE produzido no TP1.

Essa etapa gera o inventário técnico que orienta toda a exploração posterior: sem saber exatamente o que existe na superfície do alvo, não é possível atacar com precisão nas etapas seguintes do engajamento.

### Tarefa
1. Execute uma varredura de portas e serviços com Nmap contra o alvo de laboratório, registrando os serviços identificados.

2. Utilize Gobuster e Kiterunner para descobrir diretórios e endpoints de API não documentados, registrando os achados relevantes.

3. Use o ZAP e o Wireshark para identificar tecnologias de backend e cabeçalhos característicos da aplicação, explicando o que cada evidência revela sobre a stack utilizada.

---

> Todos os comandos a seguir referem-se à aplicação `crAPI` executada localmente no Docker executada na porta `:8888`

### Item 2.1
O seguinte comando escaneia todas as portas do host local onde está o alvo de laboratorio, incluindo os serviços disponiveis em cada porta (por conta do argumento `-sV`).
```
sudo nmap -sS -sV -p- --min-rate 1000 127.0.0.1 -oN nmap_output.txt
```
O output deste comando pode ser encontrado em `Exercicio_2/nmap_output.txt`

**Serviços identificados com base no output:**
- `:8025/tcp` http - Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
- `:8443/tcp` ssl/http - OpenResty web app server 1.27.1.2
- `:8888/tcp` http - OpenResty web app server 1.27.1.2
- `:30080/tcp` http - OpenResty web app server 1.27.1.2
- `:30443/tcp` ssl/http - nginx

---

### Item 2.2
> A wordlist foi gerada com base em: `https://raw.githubusercontent.com/OWASP/crAPI/refs/heads/develop/openapi-spec/crapi-openapi-spec.json`

Execute o seguinte comando dentro do diretorio `Exercicio_2`para realizar a busca por subdominios de de crAPI. a porta `8888` foi identificada no item anterior como o serviço frontend do crAPI.

```sh
gobuster dir -u http://127.0.0.1:8888/workshop -w wordlist.txt -o gobuster_output.txt
```

O output do comando pode ser encontrado em `Exercicio_2/gobuster_output.txt`

**Endpoints encontrados:**
/community
/identity
/images
/workshop

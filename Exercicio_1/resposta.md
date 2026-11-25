# Exercício 1

### Contexto

A Vetor Security recebeu um novo engajamento contra uma API que simula um sistema de veículos conectados (o crAPI, usado como alvo de treinamento). 

Antes de qualquer interação direta com a aplicação, seu líder técnico exige uma fase de reconhecimento passivo, para levantar informações publicamente disponíveis sem gerar tráfego direto contra o alvo. 

Essa etapa reduz o risco de alertar defesas do lado do cliente e costuma revelar informações que a própria equipe de desenvolvimento não sabia estar expostas, como repositórios de código vazados, subdomínios esquecidos ou credenciais reaproveitadas em outros serviços. Em um engajamento black box real, esta é frequentemente a única fase em que o pentester consegue reunir contexto de negócio sobre o alvo antes de qualquer autorização formal de teste ativo ser exercida.

### Tarefa
1. Execute buscas de Google dorking direcionadas ao domínio e à tecnologia do alvo simulado, documentando ao menos três dorks utilizados e o que cada um pretende revelar.

2. Utilize o Shodan (ou registre a consulta equivalente, caso o ambiente de laboratório seja isolado) para identificar informações de infraestrutura potencialmente expostas.

3. Consolide os achados de reconhecimento passivo em uma tabela curta, indicando a fonte e a relevância de cada informação para o restante do engajamento.

---

### Item 1.1
Os dorks a seguir assumem que o dominio do alvo é `www.crapi.apisec.ai`

#### Dork 1
A consulta a seguir tem o proposito de buscar pela documentação exposta da API, afim de encontrar endpoints não documentados.
```txt
site:crapi.apisec.ai ("swagger" OR "openapi" OR "postman_collection") (inurl:swagger OR inurl:api-docs OR inurl:openapi)
``` 

#### Dork 2
O Dork a seguir tem o proposito de encontrar arquivos de configuração, variaveis de ambiente ou outros segredos do sistema que não deveriam etar expostos.  
```txt
site:crapi.apisec.ai (ext:yml OR ext:yaml OR ext:sql OR ext:bak OR inurl:.env) ("password" OR "secret" OR "database" OR "host" OR "connectionstring")
```

#### Dork 3:
O dork a seguir tem o proposito de encontrar paginas ou endpoints do sistema que usualmente estão destinadas a admins ou desenvolvedores.  
``` txt
site:crapi.apisec.ai (intitle:"dashboard" OR intitle:"admin" OR inurl:health OR inurl:debug)
```

---

### Item 1.2
Um script python utilizando a biblioteca shodan pode ser encontrado em `/Exercicio_1/shodan_inspect.py`

---

### Item 1.3
A consolidação não pode ser feita pos não existe dominio para ser analisado. Nenhumas das duas tecnicas funciona com crAPI rodando localmente.
# Revisão prática — Git, GitHub e pytest

**Objetivo:** revisar o caminho de um arquivo de testes até o repositório remoto e explicar o que muda em cada etapa.  

## Exercício: triagem de previsões

O arquivo [`confianca.py`](confianca.py) contém a função `classificar_confianca(confianca, dados_incompletos=False)`. A confiança é um número inteiro. O segundo argumento é um booleano opcional que indica se faltam dados na previsão. Se for omitido, considera-se que os dados estão completos.

| Confiança | Dados completos | Dados incompletos |
|---|---|---|
| Abaixo de 0 ou acima de 100 | `"invalida"` | `"invalida"` |
| 0 a 49 | `"nova_analise"` | `"nova_analise"` |
| 50 a 79 | `"revisao"` | `"revisao"` |
| 80 a 100 | `"automatica"` | `"revisao"` |

Crie o arquivo `test_confianca.py` na raiz do projeto e escreva os testes com pytest. Escolha entradas para cobrir os quatro resultados, as transições entre faixas e os dois extremos do intervalo válido, por dentro e por fora. Compare a mesma pontuação com dados completos e incompletos em pelo menos uma faixa em que o resultado muda e uma em que ele permanece igual. Não altere o código original.

## Roteiro de revisão

### 0 — Importar o WSL com `--import-in-place` e abrir o VS Code

- O que é o WSL e por que usamos um ambiente Linux na disciplina?
- Por que precisamos registrar a distribuição novamente depois do logoff no laboratório?
- Em qual terminal fazemos a importação? Como conferir se o terminal integrado do VS Code está no WSL?

### 1 — Clonar o repositório

- Qual é a diferença entre Git e GitHub?
- O que um clone traz além dos arquivos atuais?
- Em que situação você usaria `git init` e em que situação usaria `git clone`?

### 2 — Criar e conferir sua branch

- O que é uma branch? O que significa dizer que ela está ativa?
- Por que trabalhar em uma branch separada? Alterar uma branch muda a `main` automaticamente?
- Como descobrir a branch atual? Uma branch criada localmente já aparece no GitHub?

### 3 — Escrever os testes

- Para que serve um teste automatizado? 
- O que significam *Arrange*, *Act* e *Assert*? Onde cada etapa aparece em um dos seus testes?
- O que é TDD?
- Como a função já está pronta, em que esta atividade difere de desenvolvê-la com TDD?
- Quais entradas você escolheu para detectar erros nas mudanças de faixa? Por que escolheu esses valores?

### 4 — Executar os testes com pytest

- Qual é a diferença entre um teste que passou, um teste que falhou e uma execução que não encontrou testes?
- O que você pode concluir quando todos os testes passam? O que ficou sem verificar?

### 5 — Conferir o estado do repositório

- O que são Working Directory, Staging Area, Local Repository e Remote Repository?
- Logo depois de salvar o novo arquivo de testes, o que mudou no diretório de trabalho (*working directory*)? O que mudou na *staging area*, no histórico local e no remoto?
- Como o `git status` distingue um arquivo novo ainda não rastreado de um arquivo preparado para o commit?

### 6 — Preparar e revisar o commit

- O que o `git add` coloca na *staging area*? Quais ele altera algo em outras áreas do git?
- Se você editar o arquivo depois de usar `git add`, qual versão entrará no commit? Como preparar a edição mais recente?

### 7 — Fazer e conferir o commit dos testes

- De onde vem o conteúdo do commit? Em qual repositório ele é registrado?
- Como conferir a mensagem do commit mais recente e a branch em que você está?
- O que ainda falta para o commit aparecer no GitHub?

### 8 — Fazer o primeiro push e conferir a branch no GitHub

- O que o  `git push` faz? 
- Em que direção as atualizações viajam com `git push` e com `git pull`?


## Glossário de comandos Git

| Comando | O que faz |
|---|---|
| `git init` | Inicializa um repositório Git local em uma pasta. |
| `git clone URL` | Cria uma cópia local de um repositório existente e configura a origem remota. |
| `git switch -c NOME_DA_BRANCH` | Cria uma branch local e muda para ela. |
| `git checkout NOME_DA_BRANCH` | Muda para uma branch existente. Com um identificador de commit, permite visitar aquele commit. |
| `git branch --show-current` | Mostra o nome da branch ativa. |
| `git status` | Mostra a branch atual e o estado das alterações, inclusive arquivos ainda não rastreados. |
| `git diff` | Mostra mudanças em arquivos rastreados que ainda não foram preparadas para o commit. |
| `git diff --staged` | Mostra as mudanças preparadas em relação ao último commit. |
| `git add ARQUIVO` | Prepara o conteúdo atual do arquivo para o próximo commit. |
| `git commit -m "Mensagem"` | Registra o conteúdo preparado no histórico local. |
| `git log --oneline` | Mostra o histórico de commits em formato resumido. |
| `git pull` | Busca atualizações do remoto e as integra à branch atual. |
| `git push` | Envia commits locais ao remoto e atualiza a branch de destino. |
| `git push -u origin NOME_DA_BRANCH` | Publica a branch no remoto `origin` e associa a branch local à correspondente remota. |

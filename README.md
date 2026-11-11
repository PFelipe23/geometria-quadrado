# Geometria do quadrado: Git, GitHub e contribuição com IA

Notas de aula para aprender Git e GitHub construindo duas contribuições ao mesmo projeto: uma manual e outra com auxílio de inteligência artificial. O conteúdo segue a ordem de execução: entender o projeto, registrar uma issue, desenvolver, propor a alteração, revisar e integrar.

O programa recebe o lado de um quadrado e devolve suas medidas em um dicionário. Vamos acrescentar uma medida por vez, usando **fork, branch, commit e pull request**.

| Momento da aula | O que a função calcula | Exemplo com lado 5 |
|---|---|---|
| Início | Área | `area = 25` |
| Primeiro PR, manual | Área e perímetro | `area = 25`, `perimetro = 20` |
| Segundo PR, com IA | Área, perímetro e diagonal | `area = 25`, `perimetro = 20`, `diagonal ≈ 7,071` |

**Ponto de partida:** `quadrado_geom.py` calcula somente a área. Ao longo da aula, a primeira contribuição acrescenta o perímetro; a segunda acrescenta diagonal, validação e testes. Os exemplos deste README apresentam cada evolução no momento em que ela será implementada.

## Os papéis na colaboração

| Participante | Responsabilidade | Repositório em que trabalha |
|---|---|---|
| **Mantenedor (Ricardo)** | Organiza os pedidos, revisa as propostas e integra as contribuições | Original: [ricardocorsini/geometria-quadrado](https://github.com/ricardocorsini/geometria-quadrado) |
| **Contribuidor** | Desenvolve a alteração em seu fork e propõe sua integração por meio de um PR | Fork: `SEU-USUARIO/geometria-quadrado` |

O mantenedor e o contribuidor trabalham em cópias separadas. Execute os comandos de cada papel **na cópia correspondente e no computador de quem desempenha esse papel**. Antes de copiar um endereço, substitua `SEU-USUARIO` pelo usuário real do contribuidor.

## 1. Git, GitHub e os conceitos da colaboração

O Git registra a evolução dos arquivos no computador. O GitHub hospeda esse histórico e permite organizar pedidos e revisar propostas. É possível usar Git sem GitHub; nesta aula, usamos os dois para colaborar.

Uma contribuição atravessa três lugares: o repositório original, o fork no GitHub e a cópia local do contribuidor. A branch separa a tarefa dentro do histórico dessa cópia. Os termos abaixo descrevem cada parte desse processo.

| Termo | Significado nesta aula |
|---|---|
| **Git** | Sistema que registra versões dos arquivos e relaciona o histórico de alterações. Funciona localmente. |
| **GitHub** | Plataforma que hospeda repositórios Git e reúne issues, PRs e revisões. |
| **Repositório** | Conjunto de arquivos do projeto, histórico e referências de versões. |
| **Original** | Repositório do projeto que receberá a proposta de contribuição. |
| **Fork** | Cópia vinculada ao original no GitHub, normalmente na conta de quem contribui. |
| **Clone** | Cópia de trabalho do repositório no computador ou no ambiente da IA, com o histórico Git. |
| **Branch** | Linha de trabalho no histórico. Nesta aula, cada contribuição terá sua própria branch. |
| **Branch padrão/base** | A padrão é a principal configurada no GitHub. A base é o destino escolhido para o PR; nesta aula, ambas são `master`. |
| **Área de trabalho** | Arquivos que estão no disco e podem ser editados. Salvar o arquivo ainda não cria um commit. |
| **Staging/index** | Seleção do conteúdo que entrará no próximo commit, preparada com `git add`. |
| **Commit** | Registro de uma versão dos arquivos, com identificação, autoria e mensagem. Não envia nada ao GitHub sozinho. |
| **Remote** | Destino configurado no Git para buscar ou enviar histórico. O nome e o endereço aparecem em `git remote -v`. |
| **origin** | Nome convencional do remoto criado no clone. Para o contribuidor, apontará ao fork; para Ricardo, ao original. |
| **upstream** | Nome convencional que o contribuidor dará ao original para buscar as atualizações do projeto. |
| **fetch** | Busca histórico e atualiza referências remotas locais, sem integrar as alterações à branch atual. |
| **pull** | Busca e integra alterações na branch atual. Usaremos `--ff-only` para recusar integração com histórico divergente. |
| **push** | Envia commits e solicita a atualização da branch no remoto de destino. Não abre PR automaticamente. |
| **Diff** | Comparação entre versões, mostrando o que foi acrescentado, removido ou alterado. |
| **Issue** | Página que registra um pedido, problema ou investigação, com contexto, conversa e critérios de aceite. |
| **Pull request/PR** | Proposta para integrar alterações de uma branch em outra, com espaço para revisar e conversar. |
| **Review** | Revisão da proposta: pode gerar comentários, pedidos de ajuste ou aprovação. |
| **Merge** | Integração das alterações ao destino aceito pelo mantenedor. |
| **Checks/CI** | Verificações automáticas configuradas no projeto. Só aparecem quando existe essa configuração; rodar um teste local não cria CI. |
| **Conflito** | Situação em que a integração exige decidir como combinar alterações concorrentes. |

> **Três ações diferentes:** commit registra; push envia; PR propõe a integração. Nesta colaboração, o contribuidor propõe e o mantenedor decide o merge.

## 2. Preparar o ambiente

Cada participante precisa de uma conta no GitHub, Git 2.28+ e Python 3.10+ instalados, além de um editor de texto. O VS Code é uma opção. Este exemplo usa apenas a biblioteca padrão do Python.

**Ambos, no terminal:**

```bash
git --version
python --version
```

Nesta aula usamos `python`. Se o computador usa `python3` ou `py -3`, substitua o comando nos exemplos. Os comandos de Git podem ser usados no terminal do Linux/macOS ou no Git Bash do Windows.

### Autenticação para enviar commits

Estar conectado ao GitHub no navegador e estar autenticado no terminal são coisas diferentes. A autenticação precisa estar concluída antes de enviar alterações.

<details>
<summary>Uma opção para autenticar o terminal: GitHub CLI</summary>

Se o GitHub CLI estiver instalado, cada pessoa pode executar:

```bash
gh auth login
gh auth setup-git
gh auth status
```

No login, escolha `GitHub.com`, protocolo `HTTPS` e autenticação pelo navegador. Quem já usa outro método de autenticação Git pode mantê-lo. A identidade dos commits será configurada dentro de cada clone nas próximas etapas.

Senhas e tokens não devem ser compartilhados com a IA ou exibidos na tela. Consulte a [instalação do GitHub CLI](https://cli.github.com/) se precisar dessa ferramenta.

</details>

## 3. Conhecer e executar o programa inicial

### A cópia local do mantenedor

Em uma pasta de trabalho fora de outro repositório:

```bash
git clone https://github.com/ricardocorsini/geometria-quadrado.git
cd geometria-quadrado
git remote -v
git branch --show-current
python quadrado_geom.py
```

Saída inicial esperada:

```text
Lado: 5.0
{'area': 25.0}
```

Neste repositório, a branch padrão é **`master`**. Em outros projetos, confira o nome; ele pode ser `main` ou outro. Na cópia de Ricardo, `origin` aponta para o original.

O arquivo `quadrado_geom.py` começa assim:

```python
def quadrado_geom(lado):
    """Retorna a área de um quadrado em um dicionário."""
    return {"area": lado ** 2}


if __name__ == "__main__":
    lado = 5.0
    resultado = quadrado_geom(lado)
    print(f"Lado: {lado}")
    print(resultado)
```

- `lado` é a entrada da função; a área é `lado²`.
- O retorno já é um dicionário: acrescentaremos novas chaves sem trocar o tipo de retorno.
- O bloco `if __name__ == "__main__":` executa o exemplo quando o arquivo é iniciado diretamente. Importar a função nos testes não executará esse exemplo.
- A área usa unidades ao quadrado; perímetro e diagonal usam a mesma unidade do lado.

## 4. Registrar a primeira issue: o pedido de contribuição

Antes de alterar o código, registre o que precisa ser feito. Uma **issue** concentra o objetivo, o contexto e os **critérios de aceite**: condições observáveis que permitem decidir se o pedido foi atendido.

A issue descreve o trabalho; o pull request apresenta a implementação. Separar essas duas coisas permite discutir a necessidade antes de escrever código e relacionar o resultado ao pedido original.

**Mantenedor, no GitHub:** abra [Issues do repositório original](https://github.com/ricardocorsini/geometria-quadrado/issues), clique em **New issue** e copie o título e a descrição abaixo. Se aparecer uma seleção de modelos, escolha a opção de issue em branco. Reutilize uma issue equivalente se ela já existir.

**Título da issue:**

```text
Adicionar o cálculo do perímetro do quadrado
```

**Descrição da issue:**

~~~markdown
## Contexto

A função quadrado_geom, no arquivo quadrado_geom.py, recebe o lado de
um quadrado e atualmente retorna um dicionário contendo somente a área.

## Objetivo

Acrescentar o perímetro ao resultado da função, preservando o cálculo
da área e o bloco de execução de exemplo.

## Comportamento esperado

Usar a relação: perimetro = 4 * lado.

Para lado = 5.0, o resultado deve ser:
{"area": 25.0, "perimetro": 20.0}

## Critérios de aceite

- [ ] A função continua retornando um dicionário.
- [ ] A chave area mantém o cálculo lado ** 2.
- [ ] A chave perimetro retorna 4 * lado.
- [ ] Para lado 5.0, área e perímetro são 25.0 e 20.0.
- [ ] A execução de python quadrado_geom.py continua funcionando.
- [ ] A contribuição altera somente quadrado_geom.py.

## Escopo

A diagonal, a validação do lado e os testes automatizados serão tratados
em uma segunda issue, depois da integração desta contribuição.
~~~

Clique em **Create / Submit new issue** para publicar. Guarde o **link e o número efetivamente criado**. Issues e PRs compartilham a mesma sequência numérica no GitHub; por isso, os exemplos usam marcadores em vez de supor que esta será a issue #1.

O contribuidor lê o pedido e pode comentar que começará a tarefa, evitando trabalho duplicado. Labels classificam o pedido, e assignees identificam responsáveis quando usados pelo projeto; esses recursos não são necessários para completar o exemplo.

## 5. Primeira contribuição: implementar o perímetro sem IA

**Papel ativo: contribuidor.** A issue define a alteração que será feita. O fork permite publicar essa alteração na sua conta, e a branch mantém a tarefa identificada até a revisão.

### 5.1. Criar o fork no navegador

1. Abra o [repositório original](https://github.com/ricardocorsini/geometria-quadrado).
2. Clique em **Fork** e confira o **Owner**: deve ser sua conta.
3. Clique em **Create fork**. Se a cópia já existir, abra seu fork.
4. Confira que o endereço agora é `github.com/SEU-USUARIO/geometria-quadrado` e que a página informa o vínculo com o original.

### 5.2. Clonar o fork e identificar os destinos

**Contribuidor, no terminal, em uma pasta nova:**

```bash
git clone https://github.com/SEU-USUARIO/geometria-quadrado.git
cd geometria-quadrado
git remote add upstream https://github.com/ricardocorsini/geometria-quadrado.git
git remote -v
git remote show upstream
```

Confira: **`origin` aponta ao seu fork e `upstream` ao original de Ricardo**. O comando `remote add` é feito uma vez nesse clone.

Configure sua própria autoria, substituindo os dois campos abaixo. Use um e-mail associado à sua conta ou o endereço `noreply` fornecido pelo GitHub:

```bash
git config user.name "SEU_NOME"
git config user.email "SEU_EMAIL_DO_GITHUB"
```

Essas configurações são locais a este repositório e não substituem o login necessário para o push.

### 5.3. Atualizar a base e criar a branch da tarefa

Comece com os arquivos salvos e `git status --short` sem alterações. Se houver trabalho pendente de outra tarefa, organize-o antes de continuar.

```bash
git status --short
git fetch upstream
git switch master
git merge --ff-only upstream/master
git switch -c feat/perimetro
git branch --show-current
python quadrado_geom.py
```

A branch atual deve ser `feat/perimetro`. A execução ainda mostra somente a área. Uma branch organiza o histórico; ela não guarda automaticamente edições ainda não commitadas.

### 5.4. Acrescentar o perímetro no editor

Altere **somente a função** em `quadrado_geom.py`, preservando o bloco de execução:

```python
def quadrado_geom(lado):
    """Retorna a área e o perímetro de um quadrado."""
    return {
        "area": lado ** 2,
        "perimetro": 4 * lado,
    }
```

Salve e confira:

```bash
python quadrado_geom.py
git status --short
git diff -- quadrado_geom.py
git diff --check
```

Resultado esperado:

```text
Lado: 5.0
{'area': 25.0, 'perimetro': 20.0}
```

### 5.5. Registrar e enviar ao fork

Salvar o arquivo muda a área de trabalho. `git add` seleciona o conteúdo para o próximo commit, e `git diff --cached` permite revisar essa seleção. Depois, `git commit` registra a versão e `git push` a envia ao fork. Execute os comandos nessa ordem:

```bash
git add quadrado_geom.py
git diff --cached
git diff --cached --check
git commit -m "feat: adicionar perimetro do quadrado"
git push -u origin feat/perimetro
```

Antes do commit, o diff staged deve conter apenas a alteração intencional. O `-u` configura o rastreamento dessa branch. Abra seu fork no GitHub e selecione `feat/perimetro` para conferir o commit publicado.

### 5.6. Abrir o primeiro PR manualmente

No original, abra **Pull requests > New pull request > compare across forks**. O aviso **Compare & pull request** no fork também pode iniciar a comparação.

| Campo | Escolha |
|---|---|
| **base repository** | `ricardocorsini/geometria-quadrado` |
| **base** | `master` |
| **head repository** | `SEU-USUARIO/geometria-quadrado` |
| **compare** | `feat/perimetro` |

Título sugerido: **feat: adicionar perímetro do quadrado**.

Na descrição, informe a issue real, a mudança e o resultado observado ao executar o programa. Confira **Files changed** antes de clicar em **Create pull request**.

Se toda a issue estiver resolvida, pode usar `Closes #NUMERO_REAL` na descrição, substituindo o marcador. O fechamento automático ocorre quando o PR é integrado à branch padrão. Para uma relação parcial, apenas referencie a issue.

## 6. Revisar e integrar o primeiro pull request

**Mantenedor, no navegador:** abra o PR, leia a descrição e **Files changed**. Confira se a área foi preservada, se o perímetro está correto e se o contribuidor demonstrou a execução.

Se houver ajuste necessário, comente no PR. O contribuidor corrige na mesma branch, executa o programa novamente e registra o ajuste com os comandos abaixo, somente se houver uma correção a enviar:

```bash
git diff
git add quadrado_geom.py
git diff --cached
git commit -m "fix: atender ajuste solicitado na revisao"
git push origin feat/perimetro
```

Os novos commits entram no mesmo PR. Não é necessário abrir outro para cada ajuste.

**Mantenedor, no navegador:** quando estiver correto, use **Merge pull request** e confirme a integração. Para esta aula, se disponível, escolha **Create a merge commit**, facilitando observar o histórico. Use apenas o método permitido pelo repositório.

**Mantenedor, no terminal, na cópia do original:** comece com estado limpo.

```bash
git status --short
git switch master
git pull --ff-only origin master
python quadrado_geom.py
git log --oneline --graph --all -8
```

Agora o original também deve devolver área e perímetro. Enquanto o PR estava aberto, a mudança era uma proposta. Depois do merge, ela passa a fazer parte da branch padrão do original.

## 7. Sincronizar o fork depois do merge

**Contribuidor, no terminal da cópia do fork.** O merge aconteceu no original. Antes da segunda tarefa, atualize sua base local e envie essa base ao seu fork. Comece com estado limpo:

```bash
git status --short
git fetch upstream
git switch master
git merge --ff-only upstream/master
git push origin master
python quadrado_geom.py
```

Confirme área e perímetro também na `master` do fork. A contribuição com IA partirá dessa versão e usará **uma nova branch**, `feat/diagonal`.

## 8. Registrar a segunda issue: diagonal, validação e testes

Com o perímetro integrado, o próximo pedido pode partir da versão atualizada do projeto. **Mantenedor:** abra uma nova issue no original usando o texto abaixo.

**Título da issue:**

```text
Adicionar diagonal, validação do lado e testes automatizados
```

**Descrição da issue:**

~~~markdown
## Contexto

A função quadrado_geom já retorna a área e o perímetro do quadrado.

## Objetivo

Adicionar a diagonal, definir que o lado deve ser positivo e verificar
o comportamento da função com testes automatizados.

## Comportamento esperado

- Calcular diagonal = lado * sqrt(2), usando a biblioteca padrão.
- Preservar as chaves area e perimetro e o retorno como dicionário.
- Lançar ValueError para lado igual a zero ou negativo.
- Preservar o bloco de execução de exemplo.

Para lado = 5.0:
area = 25.0, perimetro = 20.0, diagonal aproximadamente 7.0710678.

## Critérios de aceite

- [ ] As três medidas estão corretas para lados 5.0 e 2.0.
- [ ] A comparação da diagonal nos testes usa tolerância numérica.
- [ ] Zero e valores negativos geram ValueError.
- [ ] test_quadrado_geom.py usa unittest, sem dependências externas.
- [ ] python quadrado_geom.py executa o exemplo.
- [ ] python -m unittest -v encontra testes e todos passam.
- [ ] Apenas quadrado_geom.py e test_quadrado_geom.py são alterados/criados.

## Forma de contribuição

A implementação pode usar IA. O contribuidor deve revisar o código,
conferir os resultados e descrever no PR o que foi realmente validado.
~~~

Publique a issue e copie seu número e link reais. Este será o pedido informado à IA na próxima seção. O objetivo da tarefa e seus critérios de aceite permanecem explícitos, mesmo quando a implementação é assistida por IA.

## 9. Segunda contribuição: desenvolver com IA

### 9.1. Conectar o ambiente

Abra uma sessão capaz de ler o projeto, editar arquivos e executar Python. No ChatGPT Work, conecte o plugin GitHub e indique `@GitHub`; no Codex, selecione ou informe seu fork no ambiente de desenvolvimento. Confira o acesso ao fork, especialmente se ele foi criado depois da conexão.

Conseguir ler o GitHub não garante que a sessão consiga executar testes ou enviar commits. Peça que a IA confirme cada capacidade. Autorize a conta pelas telas oficiais, sem colar credenciais no prompt.

O [guia do OpenStruct](https://www.openstruct.com.br/development/contribuir-com-ia) mostra o percurso de configuração. Nesta aula, use os endereços de **geometria-quadrado**, e não os aplicativos selecionáveis no formulário desse guia.

### 9.2. Prompt para a segunda tarefa

Substitua `SEU-USUARIO` e `NUMERO_REAL_DA_ISSUE` antes de enviar. O fork precisa estar atualizado com o primeiro PR.

```text
Quero preparar a segunda contribuição da nossa aula de Git e GitHub.

Original: https://github.com/ricardocorsini/geometria-quadrado
Meu fork: https://github.com/SEU-USUARIO/geometria-quadrado
Issue: https://github.com/ricardocorsini/geometria-quadrado/issues/NUMERO_REAL_DA_ISSUE

Leia a issue e o código atual. Confirme que o fork está atualizado com
o original e que quadrado_geom já devolve área e perímetro. Confira se
há um PR equivalente em andamento. Preserve meu trabalho existente.
Confirme seus acessos para ler, editar, executar Python e enviar ao fork.

Explique um plano breve e crie a branch feat/diagonal a partir da base
atualizada. Acrescente a chave diagonal, usando lado * sqrt(2), sem
alterar o tipo de retorno nem remover área e perímetro.

Defina que o lado deve ser positivo: zero e valores negativos devem
gerar ValueError. Preserve o bloco de execução de exemplo.

Crie test_quadrado_geom.py usando unittest, da biblioteca padrão.
Confira as três medidas para lados 5.0 e 2.0, usando tolerância na
diagonal, e teste a rejeição de zero e valores negativos.

Não instale dependências. Altere apenas quadrado_geom.py e crie
test_quadrado_geom.py. README.md contém as notas da aula: mantenha-o preservado.
Execute python quadrado_geom.py e python -m unittest -v. Confira se
testes foram realmente encontrados e relate resultados e limitações.

Revise o diff e selecione apenas os arquivos da tarefa. Use a identidade
Git configurada para minha contribuição e faça commit e push somente
na branch feat/diagonal do meu fork. Não force histórico nem envie ao
original. Não abra nem mescle o PR: faremos isso manualmente na aula.

Entregue branch, links dos commits, resumo das alterações, evidências
reais de validação e um título e descrição sugeridos para o PR.
Se faltar alguma capacidade ou acesso, diga o que depende de mim.
Não afirme ter executado ações que não realizou.
```

A IA participa da implementação, mas o contribuidor continua responsável pela proposta. O plano, o diff e as saídas dos testes permitem conferir se a ferramenta realizou o pedido e respeitou seus limites. As etapas de issue, branch, commit, PR e revisão continuam valendo.

## 10. Conferir a entrega da IA e abrir o segundo PR

### 10.1. Obter e verificar a branch da contribuição

**Papel ativo: contribuidor.** Se a IA trabalhou na nuvem e enviou a branch ao fork, na sua cópia local e com estado limpo:

```bash
git status --short
git fetch origin
git switch feat/diagonal
git pull --ff-only origin feat/diagonal
python quadrado_geom.py
python -m unittest -v
git diff master...feat/diagonal
```

Nesse clone, `git switch feat/diagonal` pode criar a branch local a partir da branch de mesmo nome em `origin`. Se a IA trabalhou no próprio clone, a branch pode já existir. Confira sempre a branch informada na entrega.

Para lado `5.0`, confira área `25.0`, perímetro `20.0` e diagonal aproximadamente `7.0710678`. A saída dos testes deve mostrar os casos executados e `OK` quando todos passarem. **`Ran 0 tests` não valida a função.** Esses testes só existirão depois desta contribuição.

Abra o segundo PR como na etapa manual, usando `feat/diagonal` no campo **compare** e o original/`master` como base. Confira que o diff contém somente a evolução desta tarefa.

Título sugerido: **feat: adicionar diagonal, validação e testes**.

Inclua a issue real, os dois arquivos alterados, os comandos realmente executados e suas saídas. Informe o apoio de IA e o que você conferiu.

### 10.2. Revisar e integrar a segunda contribuição

**Papel ativo: mantenedor.** Confira a preservação de área/perímetro, a diagonal, o tratamento de entradas e os testes. Peça explicações ou ajustes quando necessário. O contribuidor continua na mesma branch para corrigir e enviar novos commits.

<details>
<summary>Opcional: o mantenedor executar a branch do PR antes do merge</summary>

Se estiver usando GitHub CLI, na cópia do original, com estado limpo, substitua `NUMERO_REAL_DO_PR`:

```bash
gh pr checkout NUMERO_REAL_DO_PR
python quadrado_geom.py
python -m unittest -v
git switch master
```

Isso obtém a branch do PR para conferência local. A decisão de merge continua no GitHub. O contribuidor permanece responsável pelos ajustes na contribuição.

</details>

Depois da revisão e do merge, **o mantenedor**, na cópia do original:

```bash
git status --short
git switch master
git pull --ff-only origin master
python quadrado_geom.py
python -m unittest -v
git log --oneline --graph --all -10
```

**Contribuidor:** repita a sincronização da seção 7 e rode também os testes. Agora as duas contas devem acompanhar a versão integrada.

## 11. Consolidar o processo e resolver dúvidas

| Situação | O que conferir |
|---|---|
| O commit foi criado, mas não aparece no GitHub | Confira se fez push para a branch do fork. |
| O push foi negado | Confira a conta autenticada, `git remote -v` e se `origin` aponta ao seu fork. |
| O PR mostra mudanças inesperadas | Confira repositórios, branch base e branch de origem. |
| A sincronização foi recusada | Pare, preserve o trabalho e examine a divergência. Não use force push ou descarte como solução padrão. |
| O diff não mostra um arquivo novo | `git diff` comum não mostra arquivos ainda não rastreados. Veja `git status`, abra o arquivo e depois confira o diff staged. |
| A IA disse que os testes passaram | Confira os comandos, a saída, a quantidade de testes e os arquivos produzidos. |

Depois de confirmar a integração, as branches das tarefas podem ser removidas se não forem mais necessárias. Essa limpeza é posterior ao merge e não é necessária para entender a aula.

O fluxo completo começa com uma issue e termina com a mudança revisada e integrada. O **commit** registra a alteração localmente, o **push** envia o histórico ao fork e o **PR** propõe sua integração no original. Atualizar o fork entre tarefas evita começar a próxima contribuição sobre uma versão desatualizada.

### Aplicação nos projetos OpenStruct

O mesmo processo pode ser usado para contribuir com os projetos do [OpenStruct](https://www.openstruct.com.br): escolher uma issue, entender o pedido, preparar uma alteração pequena e enviar um PR com evidências de validação. O código do quadrado torna o fluxo fácil de acompanhar; nos aplicativos de engenharia, a revisão também precisa considerar os critérios técnicos e os testes próprios de cada projeto.

Uma issue pode registrar um defeito, uma melhoria, uma dúvida técnica ou uma investigação. Os critérios de aceite relacionam esse pedido ao resultado que será revisado. A IA pode ajudar a compreender o código e implementar a solução; a análise técnica e a decisão de integração continuam com as pessoas responsáveis pelo projeto.

O uso de fork é comum para contribuições externas. Em equipes com permissão de escrita, também é possível trabalhar com branches no próprio repositório. Em ambos os casos, tarefas delimitadas, revisão e validação dão sustentação ao desenvolvimento com ou sem IA.

## Referências

- [GitHub flow](https://docs.github.com/pt/get-started/using-github/github-flow)
- [Criar fork](https://docs.github.com/pt/pull-requests/how-tos/work-with-forks/fork-a-repo)
- [Sincronizar fork](https://docs.github.com/pt/pull-requests/how-tos/work-with-forks/syncing-a-fork)
- [Criar PR a partir de fork](https://docs.github.com/pt/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork)
- [Autenticação com GitHub CLI](https://cli.github.com/manual/gh_auth_login)
- [Autenticação Git pelo GitHub CLI](https://cli.github.com/manual/gh_auth_setup-git)
- [Testes com unittest](https://docs.python.org/3/library/unittest.html)
- [Contribuição com IA no OpenStruct](https://www.openstruct.com.br/development/contribuir-com-ia)

Notas de aula de Ricardo Corsini. Menus e disponibilidade das ferramentas podem variar conforme a versão e as permissões de cada ambiente..

# Geometria do quadrado: Git, GitHub e contribuição com IA

Uma aula básica, conduzida por este README, para acompanhar duas contribuições ao mesmo projeto: uma manual e outra com auxílio de IA.

O programa recebe o lado de um quadrado e devolve suas medidas em um dicionário. Vamos acrescentar uma medida por vez, usando **fork, branch, commit e pull request**.

| Momento da aula | O que a função calcula | Exemplo com lado 5 |
|---|---|---|
| Início | Área | `area = 25` |
| Primeiro PR, manual | Área e perímetro | `area = 25`, `perimetro = 20` |
| Segundo PR, com IA | Área, perímetro e diagonal | `area = 25`, `perimetro = 20`, `diagonal ≈ 7,071` |

**Estado inicial entregue:** `quadrado_geom.py` calcula somente a área. O código do perímetro neste README é uma instrução para a primeira contribuição. A diagonal e os testes serão preparados na etapa com IA.

## Quem faz o quê

| Pessoa | Papel | Repositório em que trabalha |
|---|---|---|
| **Ricardo** | Apresenta o projeto, explica o pedido, revisa e integra as contribuições | Original: [ricardocorsini/geometria-quadrado](https://github.com/ricardocorsini/geometria-quadrado) |
| **Amigo** | Faz o fork, prepara as alterações e abre os PRs | Fork: `SEU-USUARIO/geometria-quadrado` |

Os comandos de cada pessoa devem ser executados **na cópia dela e no computador dela**. Antes de copiar um endereço, substitua `SEU-USUARIO` pelo usuário real do amigo.

## 1. Preparação antes da aula

Tenham uma conta no GitHub, Git 2.28+ e Python 3.10+ instalados, além de um editor de texto. O VS Code é uma opção. Este exemplo usa apenas a biblioteca padrão do Python.

**Ambos, no terminal:**

```bash
git --version
python --version
```

Neste roteiro usamos `python`. Se o computador usa `python3` ou `py -3`, substitua o comando nos exemplos. Os comandos de Git podem ser usados no terminal do Linux/macOS ou no Git Bash do Windows.

### Autenticação para enviar commits

Estar conectado ao GitHub no navegador e estar autenticado no terminal são coisas diferentes. Confiram o acesso antes da transmissão.

<details>
<summary>Uma opção para autenticar o terminal: GitHub CLI</summary>

Se o GitHub CLI estiver instalado, cada pessoa pode executar:

```bash
gh auth login
gh auth setup-git
gh auth status
```

No login, escolha `GitHub.com`, protocolo `HTTPS` e autenticação pelo navegador. Quem já usa outro método de autenticação Git pode mantê-lo. A identidade dos commits será configurada dentro de cada clone nas próximas etapas.

Não compartilhe senha ou token na conversa com a IA nem durante a transmissão. Consulte a [instalação do GitHub CLI](https://cli.github.com/) se precisar dessa ferramenta.

</details>

### Ricardo: abrir a cópia do original

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

### Ricardo: apresentar as duas tarefas

Na aba **Issues** do original, use **New issue** para registrar os pedidos. Se já existirem issues equivalentes, reutilize-as. Copie os números/links realmente criados; os números de issues e PRs compartilham a mesma sequência no GitHub.

**Pedido 1 — Adicionar o perímetro do quadrado**

- Preservar o cálculo da área.
- Acrescentar a chave `perimetro` ao dicionário retornado.
- Usar a relação `perimetro = 4 * lado`.
- Para lado `5.0`, obter área `25.0` e perímetro `20.0`.
- Manter a execução de exemplo funcionando.

**Pedido 2 — Adicionar diagonal, validação e testes**

- Partir da versão que já contém área e perímetro.
- Acrescentar `diagonal = lado * sqrt(2)` usando a biblioteca padrão.
- Definir o lado como positivo e lançar `ValueError` para zero e valores negativos.
- Criar testes com `unittest` para as três medidas e para entradas inválidas.
- Manter o tipo de retorno como dicionário e preservar a execução de exemplo.

## 2. Conceitos principais

Esta tabela serve de consulta durante a explicação. Não é necessário decorar os termos antes da prática.

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
| **origin** | Nome convencional do remoto criado no clone. Para o amigo, apontará ao fork; para Ricardo, ao original. |
| **upstream** | Nome convencional que o amigo dará ao original para buscar as atualizações do projeto. |
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

> **Três ações diferentes:** commit registra; push envia; PR propõe a integração. Na nossa demonstração, o amigo propõe e Ricardo decide o merge.

## 3. Entender o programa inicial

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

## 4. Amigo: primeira contribuição, sem IA

### 4.1. Criar o fork no navegador

1. Abra o [repositório original](https://github.com/ricardocorsini/geometria-quadrado).
2. Clique em **Fork** e confira o **Owner**: deve ser sua conta.
3. Clique em **Create fork**. Se a cópia já existir, abra seu fork.
4. Confira que o endereço agora é `github.com/SEU-USUARIO/geometria-quadrado` e que a página informa o vínculo com o original.

### 4.2. Clonar o fork e identificar os destinos

**Amigo, no terminal, em uma pasta nova:**

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

### 4.3. Atualizar a base e criar a branch da tarefa

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

### 4.4. Acrescentar o perímetro no editor

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

### 4.5. Registrar e enviar ao fork

```bash
git add quadrado_geom.py
git diff --cached
git diff --cached --check
git commit -m "feat: adicionar perimetro do quadrado"
git push -u origin feat/perimetro
```

Antes do commit, o diff staged deve conter apenas a alteração intencional. O `-u` configura o rastreamento dessa branch. Abra seu fork no GitHub e selecione `feat/perimetro` para conferir o commit publicado.

### 4.6. Abrir o primeiro PR manualmente

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

## 5. Ricardo: revisar e integrar o primeiro PR

**No navegador:** abra o PR, leia a descrição e **Files changed**. Confira se a área foi preservada, se o perímetro está correto e se o amigo demonstrou a execução.

Se houver ajuste necessário, comente no PR. O amigo corrige na mesma branch, executa o programa novamente e repete:

```bash
git diff
git add quadrado_geom.py
git diff --cached
git commit -m "fix: atender ajuste solicitado na revisao"
git push origin feat/perimetro
```

Os novos commits entram no mesmo PR. Não é necessário abrir outro para cada ajuste.

**Ricardo, no navegador:** quando estiver correto, use **Merge pull request** e confirme a integração. Para esta aula, se disponível, escolha **Create a merge commit**, facilitando observar o histórico. Use apenas o método permitido pelo repositório.

**Ricardo, no terminal, na cópia do original:** comece com estado limpo.

```bash
git status --short
git switch master
git pull --ff-only origin master
python quadrado_geom.py
git log --oneline --graph --all -8
```

Agora o original também deve devolver área e perímetro. Mostre a diferença entre a proposta aberta e a alteração efetivamente integrada.

## 6. Amigo: sincronizar o fork depois do merge

O merge aconteceu no original. Antes da segunda tarefa, atualize sua base local e envie essa base ao seu fork. Comece com estado limpo:

```bash
git status --short
git fetch upstream
git switch master
git merge --ff-only upstream/master
git push origin master
python quadrado_geom.py
```

Confirme área e perímetro também na `master` do fork. A contribuição com IA partirá dessa versão e usará **uma nova branch**, `feat/diagonal`.

## 7. Amigo: segunda contribuição, com IA

### 7.1. Conectar o ambiente

Abra uma sessão capaz de ler o projeto, editar arquivos e executar Python. No ChatGPT Work, conecte o plugin GitHub e indique `@GitHub`; no Codex, selecione ou informe seu fork no ambiente de desenvolvimento. Confira o acesso ao fork, especialmente se ele foi criado depois da conexão.

Conseguir ler o GitHub não garante que a sessão consiga executar testes ou enviar commits. Peça que a IA confirme cada capacidade. Autorize a conta pelas telas oficiais, sem colar credenciais no prompt.

O [guia do OpenStruct](https://www.openstruct.com.br/development/contribuir-com-ia) mostra o percurso de configuração. Nesta aula, use os endereços de **geometria-quadrado**, e não os aplicativos selecionáveis no formulário desse guia.

### 7.2. Prompt para a segunda tarefa

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
test_quadrado_geom.py. README.md é nosso roteiro: mantenha-o preservado.
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

Durante a execução, observe o plano, os arquivos alterados e as verificações. O ganho demonstrado é a IA trabalhar com o projeto e apresentar evidências que podemos conferir.

## 8. Conferir a entrega da IA e abrir o segundo PR

### Amigo: trazer a branch do fork para seu computador

Se a IA trabalhou na nuvem e enviou a branch ao fork, na sua cópia local e com estado limpo:

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

### Ricardo: revisar o segundo PR

Confira a preservação de área/perímetro, a diagonal, o tratamento de entradas e os testes. Peça explicações ou ajustes quando necessário. O amigo continua na mesma branch para corrigir e enviar novos commits.

<details>
<summary>Opcional: Ricardo executar a branch do PR antes do merge</summary>

Se estiver usando GitHub CLI, na cópia do original, com estado limpo, substitua `NUMERO_REAL_DO_PR`:

```bash
gh pr checkout NUMERO_REAL_DO_PR
python quadrado_geom.py
python -m unittest -v
git switch master
```

Isso obtém a branch do PR para conferência local. A decisão de merge continua no GitHub. O amigo permanece responsável pelos ajustes na contribuição.

</details>

Depois da revisão e do merge, **Ricardo**, na cópia do original:

```bash
git status --short
git switch master
git pull --ff-only origin master
python quadrado_geom.py
python -m unittest -v
git log --oneline --graph --all -10
```

**Amigo:** repita a sincronização da seção 6 e rode também os testes. Agora as duas contas devem acompanhar a versão integrada.

## 9. Fechamento e dúvidas rápidas

| Situação | O que conferir |
|---|---|
| O commit foi criado, mas não aparece no GitHub | Confira se fez push para a branch do fork. |
| O push foi negado | Confira a conta autenticada, `git remote -v` e se `origin` aponta ao seu fork. |
| O PR mostra mudanças inesperadas | Confira repositórios, branch base e branch de origem. |
| A sincronização foi recusada | Pare, preserve o trabalho e examine a divergência. Não use force push ou descarte como solução padrão. |
| O diff não mostra um arquivo novo | `git diff` comum não mostra arquivos ainda não rastreados. Veja `git status`, abra o arquivo e depois confira o diff staged. |
| A IA disse que os testes passaram | Confira os comandos, a saída, a quantidade de testes e os arquivos produzidos. |

Depois de confirmar a integração, as branches das tarefas podem ser removidas se não forem mais necessárias. Essa limpeza é posterior ao merge e não é necessária para entender a aula.

**Perguntas para concluir:** qual a diferença entre commit, push e PR? Por que atualizar o fork antes da próxima tarefa? O que mudou no processo quando usamos IA?

## Referências

- [GitHub flow](https://docs.github.com/pt/get-started/using-github/github-flow)
- [Criar fork](https://docs.github.com/pt/pull-requests/how-tos/work-with-forks/fork-a-repo)
- [Sincronizar fork](https://docs.github.com/pt/pull-requests/how-tos/work-with-forks/syncing-a-fork)
- [Criar PR a partir de fork](https://docs.github.com/pt/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork)
- [Autenticação com GitHub CLI](https://cli.github.com/manual/gh_auth_login)
- [Autenticação Git pelo GitHub CLI](https://cli.github.com/manual/gh_auth_setup-git)
- [Testes com unittest](https://docs.python.org/3/library/unittest.html)
- [Contribuição com IA no OpenStruct](https://www.openstruct.com.br/development/contribuir-com-ia)

Material didático preparado para a aula de Ricardo Corsini. Referências conferidas em 11/11/2026. Menus e disponibilidade das ferramentas podem variar.

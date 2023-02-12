
<!--<div align="center">
    <div>
        <img src="https://media.discordapp.net/attachments/810690029847969833/1053831385963561043/ayumudestacada.png?width=760&height=480">
    </div>
    <h1>Haru (Rework) - Overview</h1>
    <h2>Configuration, Utilities, Minigames and more...</h2>
    <div>
        <a href="https://discord.com/invite/ZZHRtsJTCS", target="_blank">
            <img src="https://img.shields.io/discord/788518735752724480?color=light%20green&label=support%20server&logo=discord&logoColor=discord" alt="Support Server">
        </a>
        <a href="https://konata.site/haru/", target="_blank">
            <img src="https://img.shields.io/website?color=light%20green&down_color=red&down_message=offline&label=site&logo=github&up_color=blue&up_message=online&url=https%3A%2F%2Fkonata.site%2Fharu%2F" alt="Support Server">
        </a>
        <a href="https://www.python.org/downloads/release/python-3913/", target="_blank">
            <img src="https://img.shields.io/badge/python-3.9.13-blue" alt="Support Server">
        </a>
        <a href="https://discordpy.readthedocs.io/en/stable/", target="_blank">
            <img src="https://img.shields.io/badge/discord-py-blue" alt="Support Server">
        </a>
        <a href="https://konata.site/haru/en/commands", target="_blank">
            <img src="https://img.shields.io/badge/help-95%20slash%20commands-blue" alt="Support Server">
        </a>
        <p>
            <img src="https://img.shields.io/badge/-supports%20hybrid%20commands-gray">
            <img src="https://img.shields.io/badge/-security%20module-gray">
            <img src="https://img.shields.io/badge/-some%20AI%20implementation-gray">
        </p>
        <p>
            <a href="#descrição">Description</a>
            •
            <a href="#clonando-o-repositório">Fork</a>
            •
            <a href="#níveis-de-permissão">Perms System</a>
            •
            <a href="#idiomas">Languages</a>
            •
            <a href="#módulos">Modules</a>
        </p>
    </div>
</div>
-->

# Documentação
## Descrição
Este é um Rework da Haru (Haru v3). Um simples bot para o discord, com algumas funcionalidades básicas.<br/>

* Funciona apenas em servidores, bloqueia o uso em dms.
* Modo de Desenvolvimento: funciona apenas nos servidores pré-definidos

> Atualmente na versão alpha 3.0.0.5

---

## Clonando o Repositório
Algumas coisas precisam ser feitas para instalar o projeto e colocá-lo para funcionar

1. Clone o repositório
2. Abra um terminal e navegue até a pasta principal do projeto
3. Instale as depêndencias usando `pip install -r requirements.txt`
4. Vá no [developer portal](https://discord.com/developers/applications) do discord, crie uma aplicação e copie o token
5. Na pasta principal do projeto, crie um arquivo .env e salve o token do bot como uma variável de ambiente
4. Inicie o programa usando `python main.py`
5. No terminal, insira o ID do seu servidor de testes
6. No terminal, Insira o ID do seu usuário no discord

Caso queira desativar o Modo de Desenvolvimento ou o Modo de Debug de Erros, apenas entre no seu servidor de testes e execute o comando equivalente: `h!oc_devmode off` e/ou `h!oc_errorsmode off`

## Níveis de permissão

* Developer
> Lista fechada

* Manager
> Lista fechada

* Owner
> Posse do servidor

* Administrator
> Permissão de administrador

* Moderator
> Permissão para banir membros

* Member
> Nenhum Requisito

## Idiomas

name | code | satage
:--- | :--- | :-----
Português | pt-br | ✔️
Inglês | en | ❌

## Módulos

> Limite de 100 Comandos (com 25 subcomandos cada)
>
> Usado: 44/100 

### Dev Module

> Modulo oculto

name | permission | explanation | stage
:--- | :--------- | :---------- | :----
oc_status | manager | Envia um hello world, e os status do bot | ✔️
oc_quit | developer | Força a parar o bot | ✔️
oc_setsv | manager | Libera o uso do bot no servidor atual| ✔️
oc_unsetsv | manager | Bloqueia o uso do bot no servidor atual | ✔️
oc_listsv | manager | Lista todos os servidores liberados | ✔️
oc_pmtmanager | developer | Adiciona um usuário na lista de managers | ✔️
oc_dmtmanager | developer | Remove um usuário da lista de managers | ✔️
oc_listmanager | manager | Lista todos os usuários com permissão de manager | ✔️
oc_pmtdeveloper | developer | Adiciona um usuário na lista de developers | ✔️
oc_dmtdeveloper | developer | Remove um usuário da lista de developers | ✔️
oc_listdeveloper | manager | Lista todos os usuários com permissão de developer | ✔️
oc_disablecommand | developer | Desabilita o uso de algum comando em todos os servidores | ✔️
oc_enablecommand | developer | Habilita o uso de algum comando em todos os servidores | ✔️
oc_disablemodule | developer | Desabilita o uso de algum módulo em todos os servidores | ✔️
oc_enablemodule | developer | Habilita o uso de algum módulo em todos os servidores | ✔️
oc_disabledcommands | manager | Informa todos os comandos desabilitados globalmente | ✔️
oc_devmode | developer | Ativa ou desativa o modo de desenvolvimento | ✔️
oc_errorsmode | developer | Ativa ou desativa o modo de debug de erros desconhecidos | ✔️
oc_botsettings | manager | lista todas as configurações do bot | ✔️

### Bot Module

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
help | member | A list of all modules and commands | ✔️
help view | member | A list of all modules and commands | ✔️
help module | member | Get explanation about a specific module | ✔️
help command | member | Get explanation about a specific command | ✔️
haru | member | Basic informations about Haru | ✔️
invite | member | Send the bot invite link | ✔️
site | member | Send the bot's official website link | ✔️
server | member | Send the bot's official server invite link | ✔️
github | member | Send Haru's repository link on github | ✔️
dev | member | Informations about the bot development team | ✔️
ping | member | Used to know if haru is alive | ✔️
vote | member | link para votar na haru no top.gg | ❌

### Configuration Module

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
prefix | admin | Allows you to change the guild prefix | ✔️
language | admin | Allows you to change Haru's language | ✔️
lockcommand | admin | Blocks the use of a command for everyone | ✔️
unlockcommand | admin | Unlocks the use of a command for everyone | ✔️
lockmodule | admin | Blocks the use of a module for everyone | ✔️
unlockmodule | admin | Unlocks the use of a module for everyone | ✔️
lockedcommands | mod | Sends a list of all locked commands on this guild | ✔️
settings | mod | Send all guild settings | ✔️

### Utility Module

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
avatar | member | Download someone's profile picture | ✔️
banner | member | Download someone's banner | ✔️
servericon | member | Downloads a guild's icon | ✔️
permissions | member | Get someone's permissions | ✔️
userinfo | member | Get someone's basic informations | ✔️
channelinfo | member | Get informations about a channel | ✔️
roleinfo | member | Get informations about a role | ✔️
serverinfo | member | Get informations about a guild | ✔️
currency | member | Convert a value to another quote | ✔️
random | member | Get a random number | ✔️
mal user | member | Serach for someone's profile on MyAnimeList | ✔️
mal anime | member | . . . | ❌
mal manga | member | . . . | ❌
mal animelist | member | Search for someone's anime list on MyAnimeList | ✔️
mal mangalist | member | Search for someone's manga list on MyAnimeList | ✔️

### Fun Module

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
morse | member | traduz um texto ou frase para código morse | ❌
flipmsg | member | inverte a ordem das letras de um texto ou frase | ❌
choose | member | escolhe algo de uma lista de coisas | ❌
coinflip | member | gira uma moeda (cara ou coroa) | ❌
dice | member | joga um dado de 6 lados | ❌
ship | member | shipa dois usuários, em até 100% | ❌
mugistrong | member | envia um gif da Mugi-Strong | ❌
say | member | faça a haru dizer alguma coisa | ❌
dm | member | faça a haru enviar uma dm para alguém | ❌
profile | member | mostra o perfil do usuário
marry | member | peça alguém em casamento | ❌
divorce | member | se divorcia de alguém | ❌
store | member | mostra toda a loja | ❌
store color | member | compra/seleciona uma cor | ❌
store icon | member | compra/seleciona um icon | ❌
store banner | member | compra/seleciona um banner | ❌
store badge | member | compra/seleciona um badge | ❌
store ring | member | compra/seleciona um anel | ❌

### Minigame Module

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
guess | member | o usuário tenta adivinhar um número de 1 a 10 | ❌
jankenpon | member | joga jokenpô com o usuário | ❌
hangman | member | jogo da forca | ❌
roulette | member | jogo da roleta russa | ❌
script | member | jogo para adivinhar a linguagem | ❌
tictactoe | member | jogo da velha | ❌
checkers | member | jogo da dama | ❌
chat start | member | inicia uma conversa com a haru | ❌
chat stop | member | encerra uma conversa com a haru | ❌
chat channel | admin | limita o uso dos comandos chat para apenas um canal | ❌
coins | member | ensina sobra os sistema de coins da haru | ❌
coins wallet | member | mostra a carteira do usuário | ❌
coins give | member | dá coins à outro usuário | ❌
coins bet | member | aposta coins com outro usuário | ❌
coins daily | member | pega a recompensa de coins diária | ❌
coins rank_local | member | envia o rank local de coins | ❌
coins rank_global | member | envia o rank global de coins | ❌


### Interaction Module

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
kiss | member | beija algum outro usuário | ❌
bite | member | morder algum outro usuário | ❌
lick | member | lambe algum outro usuário | ❌
slap | member | da um tapa em algum outro usuário | ❌
hug | member | abraça algum outro usuário | ❌
shoot | member | ataca algum outro usuário | ❌
 
## Ideias: 

- [ ] Implementar os comandos via dm
- [x] Sistema de Enocomia nos minigames
- [x] Sistema de Loja (personalização do perfil e comandos)
- [x] IA chat-bot (biblioteca chatterbot)
- [x] Jogo-da-velha contra usuário e contra IA
- [x] Jogo da forca
- [x] Jogo de roleta russa
- [x] Jogo de adivinhar a linguagem de programação
- [ ] Jogo de labirinto
## Site

### Estrutura
~~~
konata.site
    haru
        en
            home
            commands
            contact
            support
            privacy-policy
            terms-of-service
        pt-br
            home
            comandos
            contato
            suporte
            politica-de-privacidade
            termos-de-servico
~~~
<div align="center">
    <div>
        <img src="https://media.discordapp.net/attachments/810690029847969833/1053831385963561043/ayumudestacada.png?width=760&height=480">
    </div>
    <h1>Haru (Rework) - Overview</h1>
    <h2>Minigames, utilities, fun and more...</h2>
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


# Documentação
## Descrição
This is a rework of Haru (Haru v3). A simple bot for discord, with minigames and some utilities.<br/>

* Only works in guilds. all commands except help cannot be used in dms.
* Modo de Desenvolvimento: funciona apenas nos servidores pré-definidos

> Actual version: alpha 3.0.0

---

## Cloning the Repository
Before copying the repository and starting the bot, a few things need to be done.<br/>
1. Clone the repository
2. Install the dependences using `pip install -r requirements.txt`
3. Install MAL-Easy-Client by following these steps: [Mal-easy-client README](https://github.com/Ka-Konata/MAL-easy-client#mal-easy-client)
4. Create your bot in the [developer portal](https://discord.com/developers/applications) and paste your token at `.env` file (included in the repository).
5. Start the bot with `python main.py`

If you want to disable **Developer Mode** or **Debug Mode**, just log into your developer server and use the following commands: `h!oc_devmode off` and `h!oc_errorsmode off`.

## Permission Levels

* **Developer**
> Selected people

* **Manager**
> Selected people

* **Owner**
> Server owner

* **Administrator**
> Admin permission

* **Moderator**
> Permission to ban members

* **Member**
> None (default level)

## Languages

name | code | satage
:--- | :--- | :-----
Portuguese | pt-br | ✔️
Inglês | en | ❌

## Modules

> Total Commands: 44/100 

### Dev Module

> Hidden module

name | permission | explanation | stage
:--- | :--------- | :---------- | :----
oc_status | manager | Sends a hello world, and the status of the bot | ✔️
oc_quit | developer | Force stop the bot | ✔️
oc_setsv | manager | Allows use of the bot on the current server| ✔️
oc_unsetsv | manager | Blocks the use of the bot on the current server | ✔️
oc_listsv | manager | List all allowed servers | ✔️
oc_pmtmanager | developer | Adds a user to the manager list | ✔️
oc_dmtmanager | developer | Removes a user to the manager list
oc_listmanager | manager | Lists all users with manager permission | ✔️
oc_pmtdeveloper | developer | Adds a user to the developer list | ✔️
oc_dmtdeveloper | developer | Removes a user to the developer list | ✔️
oc_listdeveloper | manager | Lists all users with developer permission | ✔️
oc_disablecommand | developer | Disables the use of any command on all servers | ✔️
oc_enablecommand | developer | Enables the use of any command on all servers | ✔️
oc_disablemodule | developer | Disables the use of any module on all servers | ✔️
oc_enablemodule | developer | Enables the use of any module on all servers | ✔️
oc_disabledcommands | manager | Says which are all globally disabled commands | ✔️
oc_devmode | developer | Enable or disable development mode | ✔️
oc_errorsmode | developer | Enable or disable debug mode for unknown errors| ✔️
oc_botsettings | manager | Says what all the bot settings are | ✔️

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
mal anime | member | Serach for any anime on MyAnimeList | ✔️
mal manga | member | Serach for any manga on MyAnimeList | ✔️
mal animelist | member | Search for someone's anime list on MyAnimeList | ✔️
mal mangalist | member | Search for someone's manga list on MyAnimeList | ✔️

### Fun Module

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
morse | member | Convert a text to morse code or translate from morse code | ✔️
flipmsg | member | Reverses the position of letters in a text | ✔️
choose | member | Make me pick something for you | ✔️
coinflip | member | I toss a coin and tell you the result | ✔️
dice | member | Roll a D6 die | ❌
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
 
## Ideas: 

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

### Structure
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
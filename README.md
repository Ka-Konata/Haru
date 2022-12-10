# Documentação - Haru (Rework)
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
help | member | A list of all commands or an explanation of a specific module/command. | ✔️
haru | member | Basic information about Haru | ✔️
invite | member | Send the bot invite link | ✔️
site | member | Send the bot's official website link | ✔️
server | member | Send the bot's official server invite link | ✔️
github | member | Send Haru's repository link on github | ✔️
dev | member | Information about the bot development team | ✔️
ping | member | Used to know if haru is alive | ✔️

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
servericon | member | Downloads a guild's icon | ❌
permissions | member | informa as permissões de um usuário | ❌
userinfo | member | informações sobre um usuário | ❌
channelinfo | member | informações sobre um canal | ❌
roleinfo | member | informações sobre um cargo | ❌
serverinfo | member | informações sobre um servidor | ❌
currency | member | converte um valor de para outra cotação | ❌
random | member | gera um número aleatório | ❌
anime | member | informações sobre um anime no my anime list | ❌

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

### Minigames Module

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
guess | member | o usuário tenta adivinhar um número de 1 a 10 | ❌
jankenpon | member | joga jokenpô com o usuário | ❌

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
- [ ] IA chat-bot (biblioteca chatterbot)
- [ ] Jogo-da-velha contra usuário e contra IA
- [ ] Jogo da forca
- [ ] Jogo de roleta russa
- [ ] Jogo de adivinhar a linguagem de programação
- [ ] Jogo de labirinto
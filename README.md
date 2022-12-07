# Descrição
Este é um Rework da Haru (Haru v3)<br/><br/>
Um simples bot para o discord, com algumas funcionalidades básicas.<br/>
Funciona apenas em servidores, bloqueia o uso em dms.<br/><br/>
Enquanto em estágio de desenvolvimento, por segurança o bot só responde à comandos executados em servidores que estiverem na lista de servidores de teste.

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

## Módulos

~~~py
Dev Module
~~~
> Modulo oculto

name | permission | explanation | stage
:--- | :--------- | :---------- | :----
oc_status | manager | envia um hello world, e os status do bot | ✔️
oc_quit | developer | força a parar o bot | ✔️
oc_setsv | manager | libera o uso do bot no servidor atual| ✔️
oc_unsetsv | manager | bloqueia o uso do bot no servidor atual | ✔️
oc_listsv | manager | lista todos os servidores liberados | ✔️
oc_pmtmanager | developer | adiciona um usuário na lista de managers | ✔️
oc_dmtmanager | developer | remove um usuário da lista de managers | ✔️
oc_listmanager | manager | lista todos os usuários com permissão de manager | ✔️
oc_pmtdeveloper | developer | adiciona um usuário na lista de developers | ✔️
oc_dmtdeveloper | developer | remove um usuário da lista de developers | ✔️
oc_listdeveloper | manager | lista todos os usuários com permissão de developer | ✔️
oc_devmode | developer | ativa ou desativa o modo de desenvolvimento | ✔️


~~~py
Bot Module
~~~

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
help | member | uma lista de todos os comandos ou uma explicação de um módulo ou comando específico caso requerido | ✔️
haru | member | informações básicas sobre o bot | ❌
invite | member | link de invite do bot | ❌
site | member | link do site do bot | ❌
server | member | link de invite do servidor oficial do bot | ❌
github | member | link repositório do bot no github | ❌
dev | member | informações sobre o criador do bot | ❌
ping | member | saiba se o bot está ativo | ❌

~~~py
Configuration Module
~~~

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
prefix | admin | altera o prefixo do bot | ❌
language | admin | altera o idioma do bot | ❌
settings | mod | lista as configurações do bot no servidor | ❌
lockcommand | admin | bloqueia o uso de um comando | ❌
unlockcommand | admin | desbloqueia o uso de um comando | ❌
lockmodule | admin | bloqueia o uso de um módulo | ❌
unlockmodule | admin | desbloqueia o uso de um módulo | ❌
lockedcommands | admin | lista de comandos e/ou módulos bloqueados | ❌

~~~py
Utility Module
~~~

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
avatar | member | envia o avatar de um usuário | ❌
banner | member | envia o banner de um usuário | ❌
servericon | member | envia o ícone do servidor | ❌
permissions | member | informa as permissões de um usuário | ❌
userinfo | member | informações sobre um usuário | ❌
channelinfo | member | informações sobre um canal | ❌
roleinfo | member | informações sobre um cargo | ❌
serverinfo | member | informações sobre um servidor | ❌
currency | member | converte um valor de para outra cotação | ❌
random | member | gera um número aleatório | ❌
anime | member | informações sobre um anime no my anime list | ❌

~~~py
Fun Module
~~~

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
morse | member | traduz um texto ou frase para código morse | ❌
flipmsg | member | inverte a ordem das letras de um texto ou frase | ❌
choose | member | escolhe algo de uma lista de coisas | ❌
coinflip | member | gira uma moeda (cara ou coroa) | ❌
jankenpon | member | joga jokenpô com o usuário | ❌
dice | member | joga um dado de 6 lados | ❌
ship | member | shipa dois usuários, em até 100% | ❌
guess | member | o usuário tenta adivinhar um número de 1 a 10 | ❌


~~~py
Interaction Module
~~~

name | permission | explanation | stage
:--- | :--------- | :---------- | :---:
kiss | member | beija algum outro usuário | ❌
bite | member | morder algum outro usuário | ❌
lick | member | lambe algum outro usuário | ❌
slap | member | da um tapa em algum outro usuário | ❌
hug | member | abraça algum outro usuário | ❌
shoot | member | ataca algum outro usuário | ❌
 

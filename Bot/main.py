#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	Programador: lu1tr0n
#   Canal de Telegram: @programacion
#	Version: 1.0
#	Python 3

import time
import random
import datetime
import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import pave_event_space, per_chat_id, create_open

"""
Despues de **insertar token** en el codigo fuente, ejecutelo:
```
$ python3 main.py
```
[Documetacion del Modulo Telepot](http://telepot.readthedocs.io/en/latest/)

Descripcion del Bot: ...

Comandos Soportados: 
- `/aleatorio` - Responder con un número entero aleatorio entre 1 y 6, como rodar un dado.
- `/hora` - Contesta con la hora actual, como un reloj.

"""


class MessageWelcome(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageWelcome, self).__init__(*args, **kwargs)
	# Contador         
	# self._count = 0

    def on_chat_message(self, msg):
	    # Contador        
	    # self._count += 1
        # ID de Chat
        chat_id = msg['chat']['id']
        # Texto o Comando enviado por el usuario
        command = msg['text']

        # Estas en un SuperGrupo
        if msg['chat']['type'] == 'supergroup':
            
            if command == '/aleatorio':
                bot.sendMessage(chat_id, random.randint(1,6))
            elif command == '/hora':
                bot.sendMessage(chat_id, str(datetime.datetime.now()))

        # Estas en un Grupo
        elif msg['chat']['type'] == 'group':
            
            if command == '/aleatorio':
                bot.sendMessage(chat_id, random.randint(1,6))
            elif command == '/hora':
                bot.sendMessage(chat_id, str(datetime.datetime.now()))

        # Estas en un Chat Privado
        elif msg['chat']['type'] == 'private':
            
            if command == '/aleatorio':
                bot.sendMessage(chat_id, random.randint(1,6))
            elif command == '/hora':
                bot.sendMessage(chat_id, str(datetime.datetime.now()))

        # No reconozco el tipo de Chat que haces
        else:
            pass
        
        # Informacion completa en formato json
        # self.sender.sendMessage(msg)


TOKEN = '** TOKEN **'   # TOKEN generado por botFather

# Instanciacion de telepot
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageWelcome, timeout=10),
])
# Bucle a la espera de mensajes
MessageLoop(bot).run_as_thread()
print("Esperando Mensajes")

# Bucle Infinito  
while 1:
    time.sleep(10)

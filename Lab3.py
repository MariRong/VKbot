import vk
import time
import datetime

print('VKBot')
session = vk.Session('fdbe659a630703d7e17a2b789e2275f772c9cc5d2bf0410bbbd7a4c7d09e39798d3a3c8a7653020db56df')

api = vk.API(session)
while(True):
    messages = api.messages.get()
    commands = ['help','погода','привет','как дела?']
    messages = [(m['uid'],m['mid'],m['body'])
                for m in messages[1:] if m['body']in commands and m['read_state'] == 0]
    for m in messages:
        user_id = m[0]
        message_id = [1]
        comand = m[2]
        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        if comand == 'help':
            api.messages.send(user_id=user_id,
                              message=date_time_string +'\n>'+commands)
        if comand == 'погода':
            api.messages.send(user_id=user_id,
                              message=date_time_string +'\n>Идеальная для прогулки')
        if comand == 'привет':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>HOLA')
        if comand == 'как дела?':
            api.messages.send(user_id=user_id,
                             message=date_time_string + '\n>Отлично:3')
    ids = ', '.join([str(m[1]) for m in messages])
    if ids:
        api.messages.markAsRead(message_ids=ids)
    time.sleep(3)


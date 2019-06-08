import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot
from vk_api.utils import get_random_id

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message['text'], 'keyboard': message['keyboard'], 'random_id': get_random_id()})

token = "afed17089f3ab7dfc88d3c263bc1edeaed4770b9312d73b7838b78e71646bd8c37f57764d1612ca737f46"

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

print("Server started")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}')

            bot = VkBot(event.user_id)

            write_msg(event.user_id, bot.new_message(event))

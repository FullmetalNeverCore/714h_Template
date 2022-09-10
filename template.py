from dataclasses import dataclass
from wakeonlan import send_magic_packet
import random
import exect
import dataclasses
import random
from aiogram import Dispatcher, Bot, executor,types
from aiogram.types import Message,CallbackQuery
import asyncio
from time import strftime, gmtime
from threading import Thread
import os,time
from datetime import datetime 
import logging 
import asyncio
from apscheduler.executors.base import BaseExecutor, run_job
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time

API_TOKEN = "????"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dataclass
class LastMsg():
    year : int
    month : int
    day : int
    hour : int
    minute : int
    second : int

@dataclass
class DevMode():
    dev_mode : bool

@dataclass
class SleepMode():
    sleep_mode : bool

slp_mode = SleepMode(False)
dev_mode = DevMode(False)



class Selph:
    character_name = "???"
    char_name_sec = character_name
    randomness = 1.1
    topp = 1.0
    version = "131"
    run = False
    scheduler = AsyncIOScheduler()
    lenn = 260
    chatid = 0000000
    ignore = f'----'
    mac= ['69-2X-65-E7-C2-43','25-1B-2D-6D-3C-04']
    slp_mode = SleepMode(False)
    dev_mode = DevMode(False)
    lmg = LastMsg(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour,datetime.now().minute,datetime.now().second)

    @dp.message_handler(commands=['err'])
    async def raiseerr(messages:types.Message,self):
        raise AttributeError

    async def on_startup(x):
        print('714h PRODUCTION MODULE CUSTOM TYPE')
        print(f'714h - Version : {selph.version}')
        print('Created by NeverCore')
        await Selph.memory_reset()

    async def remind_init():
            print("NOW RUN")
            now = datetime.now()
            then = datetime(selph.lmg.year, selph.lmg.month, selph.lmg.day, selph.lmg.hour, selph.lmg.minute, selph.lmg.second)
            print(f"last_msg_event_checker - {then}")
            print("remind_event_init")
            duration = now - then
            duration_in_s = duration.total_seconds()
            print("Duration: {0}".format(duration_in_s))
            print("Duration_in_hrs: {0}".format(int(divmod(duration_in_s, 3600)[0])))
            print("Dev_mode :: {0}".format(dev_mode.dev_mode))
            if int(divmod(duration_in_s, 3600)[0]) > 1:
                print(f"{selph.character_name}_break_the_silence_event_trigger")
                await bot.send_message(selph.chatid,str(exect.PARALLAX_CORE.Mind(selph.character_name).dialgen(f"--",2,float(selph.randomness),float(selph.topp),int(selph.lenn),selph.char_name_sec,"sscu")))
            else:
                if dev_mode.dev_mode:
                    print(f"Dev logs :: last_msg_event {then} :: Duration: {duration_in_s} :: Duration_is_hrs :: {divmod(duration_in_s, 3600)[0]} ")
                else:
                    print("dev_mode inactive.")



    @dp.message_handler(commands=['dev_mode'])
    async def devmode(messages:types.Message):
            selph.dev_mode.dev_mode = not selph.dev_mode.dev_mode
            print(f"Dev_Mode :: {selph.dev_mode.dev_mode}")

    @dp.message_handler(commands=['lenn'])
    async def len_change(message:types.Message):
        selph.lenn = message.text.split()[1]
        print(selph.lenn)

    @dp.message_handler(commands=['rnd'])
    async def rnd_change(message:types.Message):
        selph.randomness = message.text.split()[1]
        print(f'Current Top_P - {selph.randomness}')

    @dp.message_handler(commands=['topp'])
    async def topp_change(message:types.Message):
        selph.topp = message.text.split()[1]
        print(f'Current Top_P - {selph.topp}')

    @dp.message_handler(commands=['checkstats'])
    async def topp_change(message:types.Message):
                        await bot.send_message(selph.chatid,f'''
                            Random = {selph.randomness}
                            Leng = {selph.lenn}
                            Topp = {selph.topp}
                        ''')

    @dp.message_handler(text_contains='turn on pc')
    async def wakey_wakey(message: types.Message):
        for x in range(len(selph.mac)):
            send_magic_packet(selph.mac[x])
            print(f'{selph.mac[x]} woked up!')
            asyncio.sleep(2)
            await bot.send_message(selph.chatid,str(exect.PARALLAX_CORE.Mind(selph.character_name).dialgen(str(message.text),0,float(selph.randomness),float(selph.topp),int(selph.lenn),selph.char_name_sec,"sscu")))

    async def memory_reset():
            print("RESETING_MEMORY")
            exect.PARALLAX_CORE.Mind(selph.character_name).mem_reset()
            print("ACTIVITY_GENERATION")
            exect.PARALLAX_CORE.Mind(selph.character_name).activity_generation()
            print("INIT_D")
            await bot.send_message(selph.chatid,str(exect.PARALLAX_CORE.Mind(selph.character_name).dialgen("msg",2,float(selph.randomness),float(selph.topp),int(selph.lenn),selph.char_name_sec,"sscu")))


    @dp.message_handler()
    async def sustain__soul(message: types.Message):
        ipa = ['192.168.8.130','192.168.8.131','192.168.8.132','192.168.8.133']
        print(str(message.from_user.id))
        if str(message.from_user.id) == str(selph.chatid):
            print(f"{selph.char_name_sec}")
            try:await bot.send_message(selph.chatid,str(exect.PARALLAX_CORE.Mind(selph.character_name).dialgen(str(message.text),0,float(selph.randomness),float(selph.topp),int(selph.lenn),selph.char_name_sec,"sscu")))
            except Exception as e:await bot.send_message(selph.chatid,str(e))
            selph.lmg = LastMsg(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour,datetime.now().minute,datetime.now().second)
            try:
                            if selph.run == False: 
                                selph.run = not selph.run
                                job = selph.scheduler.add_job(Selph.remind_init, 'interval', minutes=2,id='ignore_sensor')
                                selph.scheduler.start()
            except Exception as e:
                            print(f'Expection : {e} closing the process....')
                            selph.scheduler.remove_job('ignore_sensor')
            
        else:
            print('SECURITY_MISMATCH')

if __name__ == '__main__':
    global selph
    selph = Selph()
    executor.start_polling(dp, skip_updates=True,on_startup=Selph.on_startup)
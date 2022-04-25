# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the server. """

from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which

from git import Repo
from telethon import version
from telethon.errors.rpcerrorlist import MediaEmptyError

from userbot import ALIVE_LOGO, ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
repo = Repo()
# ============================================


@register(outgoing=True, pattern=r"^\.sysd$")
async def sysdetails(sysd):
    """For .sysd command, get system info using neofetch."""
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch",
                "--stdout",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())

            await sysd.edit("`" + result + "`")
        except FileNotFoundError:
            await sysd.edit("`Install neofetch first !!`")


@register(outgoing=True, pattern=r"^\.botver$")
async def bot_ver(event):
    """For .botver command, get the bot version."""
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        if which("git") is not None:
            ver = await asyncrunapp(
                "git",
                "describe",
                "--all",
                "--long",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )
            stdout, stderr = await ver.communicate()
            verout = str(stdout.decode().strip()) + str(stderr.decode().strip())

            rev = await asyncrunapp(
                "git",
                "rev-list",
                "--all",
                "--count",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )
            stdout, stderr = await rev.communicate()
            revout = str(stdout.decode().strip()) + str(stderr.decode().strip())

            await event.edit(
                "`Userbot Version: " f"{verout}" "` \n" "`Revision: " f"{revout}" "`"
            )
        else:
            await event.edit(
                "Shame that you don't have git, you're running - 'v1.beta.4' anyway!"
            )


@register(outgoing=True, pattern=r"^\.(alive|on)$")
async def amireallyalive(alive):
    """For .alive command, check if the bot is running."""
    output = (
        f"TEMPEST USERBOT IS ALIVE🔥\n" 
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n" 
        f"⚔️ 𝗠𝗬 𝗕𝗢𝗧 𝗜𝗦 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 ⚔️\n" 
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n" 
        f"⚡️𝗠𝗬 𝗢𝗪𝗡𝗘𝗥⚡️➪{DEFAULTUSER}** \n" 
        f"**⚡️𝗥𝗘𝗣𝗢⚡️➪ [TEMPEST](https://github.com/kirito-1240/TempestUB)** \n" 
        f"**⚡️𝗖𝗛𝗔𝗡𝗡𝗘𝗟⚡️➪ [𝗝𝗢𝗜𝗡](https://t.me/TEMPEST_UB_UPDATES)** \n" 
        f"**⚡️𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️➪ [𝗝𝗢𝗜𝗡](https://t.me/TempestUBSupport)** \n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
   )
    if ALIVE_LOGO:
        try:
            await alive.respond(output, file=ALIVE_LOGO)
            await alive.delete()
        except MediaEmptyError:
            await alive.edit(
                output + "\n\n *`The provided logo is invalid."
                "\nMake sure the link is directed to the logo picture`"
            )
    else:
        await alive.edit(output)


@register(outgoing=True, pattern=r"^\.aliveu (.+)")
async def amireallyaliveuser(username):
    """For .aliveu command, change the username in the .alive command."""
    newuser = username.pattern_match.group(1)
    global DEFAULTUSER
    DEFAULTUSER = newuser
    await username.edit(f"Successfully changed user to `{newuser}`")


@register(outgoing=True, pattern=r"^\.resetalive$")
async def amireallyalivereset(ureset):
    """For .resetalive command, reset the username in the .alive command."""
    global DEFAULTUSER
    DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
    await ureset.edit("`" "Successfully reset user for alive!" "`")


CMD_HELP.update(
    {
        "sysd": ">`.sysd`" "\nUsage: Shows system information using neofetch.",
        "botver": ">`.botver`" "\nUsage: Shows the userbot version.",
        "alive": ">`.alive`"
        "\nUsage: Type .alive to see wether your bot is working or not."
        "\n\n>`.aliveu <text>`"
        "\nUsage: Changes the 'user' in alive to the text you want."
        "\n\n>`.resetalive`"
        "\nUsage: Resets the user to default.",
    }
)

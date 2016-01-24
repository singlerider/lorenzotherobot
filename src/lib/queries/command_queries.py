from datetime import datetime

import globals
from src.lib.queries.connection import get_connection


def get_custom_command(channel, command):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT channel, command FROM custom_commands
                WHERE command = %s AND channel = %s
            """, [command, channel])
        commands = cur.fetchall()
        cur.close()
        return commands


def get_custom_command_elements(channel, command):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT user_level, response, times_used FROM custom_commands
                WHERE command = %s AND channel = %s
            """, [command, channel])
        elements = cur.fetchone()
        cur.close()
        return elements


def increment_command_counter(channel, command):
    con = get_connection()
    with con:
        cur = con.cursor()
        cur.execute("""
            UPDATE custom_commands SET times_used = times_used + 1
                WHERE command = %s AND channel = %s
            """, [command, channel])
        elements = cur.fetchone()
        cur.close()
        return elements


def save_command(command, creator, user_level, response):
    con = get_connection()
    command_fetch = get_custom_command(globals.CURRENT_CHANNEL, command)
    if len(command_fetch) > 0:
        if command_fetch[0][0] == globals.CURRENT_CHANNEL and command_fetch[
                0][1] == command:
            return "{0} already exists in {1}'s channel!".format(
                command, globals.CURRENT_CHANNEL)
    else:
        with con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO custom_commands (
                    channel, command, creator, user_level, time, response, times_used
                    ) VALUES (%s, %s, %s, %s, %s, %s, 0)
                    """, [globals.CURRENT_CHANNEL, command, creator, user_level,
                          str(datetime.now()), response])
            cur.close()
            return "{0} successfully added".format(command)


def edit_command(command, creator, user_level, response):
    con = get_connection()
    command_fetch = get_custom_command(globals.CURRENT_CHANNEL, command)
    if len(command_fetch) > 0:
        if command_fetch[0][0] == globals.CURRENT_CHANNEL and command_fetch[
                0][1] == command:
            with con:
                cur = con.cursor()
                cur.execute("""
                    UPDATE custom_commands
                        SET response = %s, user_level = %s
                        WHERE command = %s AND channel = %s
                    """, [
                    response, user_level, command, globals.CURRENT_CHANNEL])
                cur.close()
                return "{0} successfully changed".format(command)
    else:
        return "{0} already exists in {1}'s channel!".format(
            command, globals.CURRENT_CHANNEL)


def delete_command(command):
    con = get_connection()
    command_fetch = get_custom_command(globals.CURRENT_CHANNEL, command)
    if len(command_fetch) > 0:
        if command_fetch[0][0] != globals.CURRENT_CHANNEL and command_fetch[
                0][1] != command:
            return "{0} not found as a unique command in {1}'s channel!".format(
                command, globals.CURRENT_CHANNEL)
        else:
            with con:
                cur = con.cursor()
                cur.execute(
                    """DELETE FROM custom_commands
                        WHERE command = %s AND channel = %s""", [
                        command, globals.CURRENT_CHANNEL])
                cur.close()
                return "{0} successfully removed".format(command)
    else:
        return "{0} not found as a command in {1}'s channel!".format(
            command, globals.CURRENT_CHANNEL)

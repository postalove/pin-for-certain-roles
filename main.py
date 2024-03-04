'''
Discord-Bot-Module template. For detailed usages,
 check https://interactions-py.github.io/interactions.py/

Copyright (C) 2024  __retr0.init__

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import interactions
# Use the following method to import the internal module in the current same directory


'''
Replace the ModuleName with any name you'd like
'''
class PinMessage(interactions.Extension):
    module_base: interactions.SlashCommand = interactions.SlashCommand(
        name="pin",
        description="标注"
    )
    

    @module_base.subcommand("message", sub_cmd_description="标注信息")
    @interactions.slash_option(
        name = "message_url",
        description = "消息链接",
        required = True,
        opt_type = interactions.OptionType.STRING
    )
    async def pin_mess(self, ctx: interactions.SlashContext, message_url: str):
        pin_role=ctx.guild.get_role(1214173923206234142)
        if ctx.author.has_role(pin_role):
            message_id=message_url.rsplit('/', 1)[-1]
            message=ctx.channel.get_message(message_id=message_id)
            if message is not None:
                await message.pin()
                await ctx.send(content="Message Pinned!",ephemeral=True)
            else:
                await ctx.send(content='不存在的消息!',ephemeral=True)
        else:
            await ctx.send(content='你没有相应的身份组!')
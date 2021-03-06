import discord
from discord.ext import commands
import random

class General(object):
  """General commands."""

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def roll(self, dice : str):
    """Rolls a dice in NdN format."""
    try:
      rolls, limit = map(int, dice.split('d'))
    except Exception:
      await self.bot.say('Format has to be in NdN!')
      return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await self.bot.say(result)

  @commands.command()
  async def choose(self, *choices : str):
    """Chooses between multiple choices."""
    await self.bot.say(random.choice(choices))

import discord
import random

class Bot(discord.Client):

	def __init__(self):
		super().__init__()


	def random_color(self):
		hexa = "0123456789abcdef"
		random_hex = "0x"
		for i in range(6):
			random_hex += random.choice(hexa)
		return discord.Colour(int(random_hex, 16))

	def create_embed(self, title, description, color, img=""):
		embed = discord.Embed()
		embed.title = title
		embed.description = description
		embed.colour = color
		if(img != ""):
			embed.set_image(url=img)
		return embed


	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

	async def on_message(self, message):

		if(message.author == self.user):
			return

		# if(message.channel.id == 668926588938879022):
		# 	return

		if(message.content.startswith("!ping")):
			await message.channel.send("pong")

		if(message.content.startswith("!dm")):

			name = message.content.split(" ")[1]

			if(name == "all"):
				for member in message.guild.members:
					if not member == self.user:
						try:
							await member.send("Hello!")
						except discord.Forbidden:
							await message.channel.send("Erreur l'utilisateur " + str(member) + " n'a pas ouvert ses DMs")
			else:
				member = discord.utils.get(message.guild.members, name=name)

				try:
					await member.send("Hello!")
				except discord.Forbidden:
					await message.channel.send("Erreur l'utilisateur " + name + " n'a pas ouvert ses DMs")
				except AttributeError:
					await message.channel.send("Erreur l'utilisateur " + name + " n'existe pas")


		if(message.content.startswith("!embed")):
			color = self.random_color()
			description = "Salut je suis un d4rk H4x0r"
			embed = self.create_embed("HACKER", description, color, message.author.avatar_url)

			await message.channel.send(embed=embed)
		

		if(message.content.startswith("!invite")):
			#Invitation unique, n'expire jamais
			#invite = await message.channel.create_invite(unique = False)

			#Invitation expire dans 1 heure
			#invite = await message.channel.create_invite(max_age = 3600, unique = False)

			#Invitation expire dans une invitation
			invite = await message.channel.create_invite(max_uses = 1, unique = False)

			await message.channel.send(invite.url)

		if(message.content.startswith("!del_invites")):

			invites = await message.guild.invites()
			for i in invites:
				await i.delete()


if(__name__ == "__main__"):

	bot = Bot()
	bot.run("token")	#Remplacer ici par votre token

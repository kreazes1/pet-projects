const { 
    Client, 
    GatewayIntentBits, 
    ChannelType 
  } = require('discord.js');

  const CHANNEL_ID = '1274686003927584781';

  const client = new Client({ 
    intents: [
      GatewayIntentBits.Guilds,
      GatewayIntentBits.GuildWebhooks,
    ] 
  });

  client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
  });

  client.on('webhookUpdate', async (channel) => {
    try {
      if (channel.type !== ChannelType.GuildText) return;

      const webhooks = await channel.fetchWebhooks();
      const webhook = webhooks.first();

      if (webhook) {
        const owner = webhook.owner ? webhook.owner : null;

        await webhook.delete('Webhook deleted by bot.');

        const notificationChannel = await client.channels.fetch(CHANNEL_ID);
        if (notificationChannel && notificationChannel.isTextBased()) {
          const ownerMention = owner ? `<@${owner.id}>` : 'Unknown user';
          await notificationChannel.send(
            `${ownerMention} создай новый вебхук!`
          );
        } else {
          console.error(`Notification channel with id ${CHANNEL_ID} not found.`);
        }
      }
    } catch (error) {
      console.error('Error handling the webhook update:', error.message || error);
    }
  });

client.login("token")
const { App } = require("@slack/bolt");

const { registerListeners } = require("./listeners");
const fs = require("fs");
const fileName = "./utilities/constants.json";
const file = require(fileName);

// Initializes your app with your bot token and signing secret
const app = new App({
  token: process.env.BOT_TOKEN,
  socketMode: true,
  appToken: process.env.APP_TOKEN,
});

app.message("help", async ({ message, say }) => {
  await say({
    blocks: [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: "Hi there! \n Enter the following commands to perform a set of actions we’ve explained below. Only Admins can perform these actions.\n \n`#channel - topic` => This allows a channel, to be linked to a particular “Topic”. Topics can be searched across by users when they are looking to join microcommunities at Setu. Eg #football - EPL OR #seeking-satoshi - DAOs \n `culture-buddies` => Matches a potential culture buddies based on interests that a user has selected when searching for groups",
        },
      },
    ],
    text: "Welcome admin",
  });
});

app.message(/<#[A-Z0-9]|[a-z]> - [a-z]/, async ({ message, say }) => {
  if (message.user === process.env.ADMIN_ID) {
    // file["topics"].push(message.text.split(" - ")[1]);
    // fs.writeFile(fileName, JSON.stringify(file), function writeJSON(err) {
    //   if (err) return console.log(err);
    // });

    await say({
      blocks: [
        {
          type: "section",
          text: {
            type: "plain_text",
            text: "Channel linked with topic. Please make sure you add the app to this channel.",
            emoji: true,
          },
        },
      ],
      text: "Welcome admin",
    });
  } else {
    await say({
      blocks: [
        {
          type: "section",
          text: {
            type: "plain_text",
            text: "Oops! Only admins can access the command.",
            emoji: true,
          },
        },
      ],
      text: "Oops! Only admins can access the command.",
    });
  }
});

app.message("culture-buddies", async ({ message, say }) => {
  if (message.user === process.env.ADMIN_ID) {
    await say({
      blocks: [
        {
          type: "section",
          text: {
            type: "plain_text",
            text: "Culture buddy suggestions",
            emoji: true,
          },
        },
        {
          type: "divider",
        },
        {
          type: "section",
          text: {
            type: "mrkdwn",
            text: `<@${message.user}> - <@${message.user}>`,
          },
        },
      ],
    });
  } else {
    await say({
      blocks: [
        {
          type: "section",
          text: {
            type: "plain_text",
            text: "Oops! Only admins can access the command.",
            emoji: true,
          },
        },
      ],
      text: "Oops! Only admins can access the command.",
    });
  }
});

registerListeners(app);

(async () => {
  try {
    // Start your app
    await app.start(process.env.PORT || 3000);

    // eslint-disable-next-line no-console
    console.log("⚡️ Bob is running!");
  } catch (error) {
    // eslint-disable-next-line no-console
    console.error("Unable to start App", error);
    process.exit(1);
  }
})();

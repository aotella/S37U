const {
  HomeTab,
  Header,
  Divider,
  Section,
  Elements,
  Input,
  Bits,
} = require("slack-block-builder");

const topics = require("../../utilities/constants.json");

module.exports = (interests, keywords, rankings, user) => {
  const homeTab = HomeTab({
    callbackId: "tasks-home",
    privateMetaData: "open",
  }).blocks(
    Header({ text: `Introducing Bob :robot_face:` }),
    Divider(),
    Section({
      text: `Hey <@${user}>, I'm Bob! :wave: \n I'm here to hook you up with some fun engagement! :partying_face: \nDid you know that we have channels around food, travel, crypto, and more! Go ahead and try me! :exploding_head: `,
    }),
    Header({ text: "Get added to channels :handshake: " }),
    Divider(),
    Section({
      text:
        interests.data.length > 0
          ? `You have selected the following interests:${interests.data.map(
              (element) =>
                " *`" +
                element.charAt(0).toUpperCase() +
                element.slice(1) +
                "`*"
            )}`
          : `You are not currently added to any channels.`,
    }),
    Section({
      text: "There are a few more awesome channels you might have missed out on, check them out by adding your interests!",
    }).accessory(
      Elements.StaticMultiSelect({
        placeholder: "Select your interests",
      })
        .initialOptions(
          interests.data.map((element) => {
            const option = {
              value: `${element}`,
              text: `${element.charAt(0).toUpperCase() + element.slice(1)}`,
            };
            return Bits.Option(option);
          })
        )
        .options(
          topics["topics"].map((element) => {
            const option = {
              value: `${element}`,
              text: `${element.charAt(0).toUpperCase() + element.slice(1)}`,
            };
            return Bits.Option(option);
          })
        )
        .actionId("multiSelectAction")
    ),
    Header({ text: "Top performing channels :loudspeaker: " }),
    Divider(),
    Section({
      text: "These are the top three performing channels of the week! Take a bow :trophy: :sunglasses: ",
    }),
    rankings.data.map((element) => {
      return Section({
        text: `<#${element.channel_id}> - ${element.count} points`,
      });
    }),
    Header({ text: "Add keywords to get trending news :newspaper: " }),
    Divider(),
    Section({
      text: "I suggest you add some relevant keywords to the channel, so that I can dig the internet and give you :fire: updates and news! :computer: \n Multiple keywords can be by comma seperated values",
    }),
    keywords.data.map((key) => {
      return Input({
        label: `Keywords for #${key["channel_name"]} channel`,
        blockId: `${key["channel_id"]}`,
      })
        .dispatchAction()
        .element(
          Elements.TextInput({
            placeholder: "Enter keywords for channel",
          })
            .actionId("payments")
            .initialValue(key["keywords"].join(", "))
            .dispatchActionOnEnterPressed(true)
        );
    })
  );

  return homeTab.buildToJSON();
};

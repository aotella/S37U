const { reloadAppHome, completeTasks } = require("../../utilities");
const { modals } = require("../../user-interface");
var axios = require("axios");

const multiSelectActionCallback = async ({ ack, action, client, body }) => {
  await ack();
  let interests = body["actions"][0]["selected_options"].map(
    (element) => element.value
  );

  var data = JSON.stringify({
    interests: interests,
    user_id: body.user.id,
  });

  var config_channel = {
    method: "post",
    url: "http://0.0.0.0:5001/api/v1/channel/add/",
    headers: {
      "Content-Type": "application/json",
    },
    data: data,
  };

  var config_interest = {
    method: "post",
    url: "http://0.0.0.0:5001/api/v1/userinterest/",
    headers: {
      "Content-Type": "application/json",
    },
    data: data,
  };

  axios(config_channel)
    .then(async function (response) {
      axios(config_interest).then(async function (response) {
        await client.views.open({
          trigger_id: body.trigger_id,
          view: modals.taskCreated(
            `Awesome! I have notified people to add you to the channels based on your interests :star-struck:  You should be added soon, don’t forget to say :wave: hi & get the conversation going!`
          ),
        });
        await reloadAppHome(client, body.user.id, body.team.id, "");
      });
    })
    .catch(async function (error) {
      await client.views.open({
        trigger_id: body.trigger_id,
        view: modals.taskCreationError(
          `Something went wrong. Please try again.`
        ),
      });

      await reloadAppHome(client, body.user.id, body.team.id, "");
    });
};

// TODO: reformat action_ids to all be snake cased
module.exports = {
  multiSelectActionCallback,
};

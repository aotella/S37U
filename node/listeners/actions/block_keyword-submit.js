const { reloadAppHome, completeTasks } = require("../../utilities");
const { modals } = require("../../user-interface");
var axios = require("axios");

const keywordSubmitCallback = async ({ ack, action, client, body }) => {
  await ack();

  let data = body["actions"][0];

  if (data["value"].trim() === data["initial_value"].trim()) {
    console.log("same same");
    return;
  }

  let keywords = data["value"]
    .split(",")
    .map((x) => (x.length > 0 ? x.trim() : null));

  var request_body = JSON.stringify({
    channel_id: body["actions"][0]["block_id"],
    keywords: keywords,
  });

  var config = {
    method: "post",
    url: "http://0.0.0.0:5001/api/v1/channel/",
    headers: {
      "Content-Type": "application/json",
    },
    data: request_body,
  };

  axios(config)
    .then(async function (response) {
      await client.views.open({
        trigger_id: body.trigger_id,
        view: modals.taskCreated(
          `Updated! People can now find your channel with these keywords. You’ll also receive new updates based on these keywords :white_check_mark: `
        ),
      });
      await reloadAppHome(client, body.user.id, body.team.id, "");
    })
    .catch(async function (error) {
      console.log("Error", error);
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
  keywordSubmitCallback,
};

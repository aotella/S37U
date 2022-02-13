const { Op } = require("sequelize");
var axios = require("axios");

const { openTasksView } = require("../user-interface/app-home");

module.exports = async (client, slackUserID, slackWorkspaceID, navTab) => {
  try {
    let one = "http://0.0.0.0:5001/api/v1/userinterest/" + slackUserID;
    let two = "http://0.0.0.0:5001/api/v1/channelkeyword/";
    let three = "http://0.0.0.0:5001/api/v1/ranking";

    const requestOne = axios.get(one);
    const requestTwo = axios.get(two);
    const requestThree = axios.get(three);

    axios
      .all([requestOne, requestTwo, requestThree])
      .then(
        axios.spread(async (...responses) => {
          const responseOne = responses[0];
          const responseTwo = responses[1];
          const responseThree = responses[2];

          await client.views.publish({
            user_id: slackUserID,
            view: openTasksView(
              responseOne.data,
              responseTwo.data,
              responseThree.data,
              slackUserID
            ),
          });
        })
      )
      .catch(async (errors) => {
        await client.views.publish({
          user_id: slackUserID,
          view: openTasksView(
            { data: [] },
            { data: [] },
            { data: [] },
            slackUserID
          ),
        });
      });
  } catch (error) {
    // eslint-disable-next-line no-console
    console.error(error);
  }
};

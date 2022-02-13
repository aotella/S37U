const {
  appHomeNavCompletedCallback,
} = require("./block_app-home-nav-completed");
const { multiSelectActionCallback } = require("./block_multi-select-action");
const { keywordSubmitCallback } = require("./block_keyword-submit");

module.exports.register = (app) => {
  app.action(
    { action_id: "app-home-nav-completed", type: "block_actions" },
    appHomeNavCompletedCallback
  );
  app.action(
    {
      action_id: "multiSelectAction",
      type: "block_actions",
    },
    multiSelectActionCallback
  );
  app.action(
    {
      action_id: "payments",
      type: "block_actions",
    },
    keywordSubmitCallback
  );
};

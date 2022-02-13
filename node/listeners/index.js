const eventsListener = require("./events");
const actionsListener = require("./actions");

module.exports.registerListeners = (app) => {
  eventsListener.register(app);
  actionsListener.register(app);
};

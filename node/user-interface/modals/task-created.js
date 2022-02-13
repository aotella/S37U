const { Modal, Blocks } = require("slack-block-builder");

module.exports = (body) =>
  Modal({ title: "Hooray! :tada: ", callbackId: "task-created-modal" })
    .blocks(
      Blocks.Section({
        text: `${body}`,
      })
    )
    .buildToJSON();

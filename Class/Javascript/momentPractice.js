var moment = require("moment");
// import moment from "moment";

console.log(
  moment()
    .add(1, "h")
    .format("dddd, MMMM Do YYYY, h:mm:ss a")
);

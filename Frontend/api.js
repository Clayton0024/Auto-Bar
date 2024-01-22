const net = require("net");

// Create a client instance
const client = new net.Socket();

// Connect to the server
client.connect(6969, "127.0.0.1", function () {
  console.log("Connected to the server.");

  // Prepare the message
  const message = {
    type: "set_ingredients",
    ingredients: [
      {
        name: "Example Ingredient",
        quantity_ml: 100,
        abv_pct: 40.0,
        relay_no: 1,
        install_time_s: Math.floor(Date.now() / 1000), // Current Unix timestamp
      },
      // ... add more ingredients as needed
    ],
  };

  // Send the message
  client.write(JSON.stringify(message));
});

// Handle data from the server
client.on("data", function (data) {
  console.log("Received: " + data);
  client.destroy(); // kill client after server's response
});

// Handle client closing
client.on("close", function () {
  console.log("Connection closed");
});

// Handle errors
client.on("error", function (err) {
  console.error("Connection error: " + err.message);
});

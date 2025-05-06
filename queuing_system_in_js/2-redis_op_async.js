import redis from "redis";
import { promisify } from "util";

// Create Redis client
const client = redis.createClient();

// Promisify client.get
const getAsync = promisify(client.get).bind(client);

// Handle connection events
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a school using async/await
async function displaySchoolValue(schoolName) {
  const reply = await getAsync(schoolName);
  console.log(reply);
}

// Main function to run all operations
async function main() {
  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");

  // Close the Redis connection
  client.quit();
}

// Execute the main function
main();

import express from "express";
import axios from 'axios';
import { oldMockupData, newMockupData } from "./src/utils/constants.js";
const app = express();



app.get('/example', async (req, res) => {
  const result = await analysis();
  const shipsData = Array.from(result.entries());
  res.status(200).json({ result: shipsData })
})
app.listen(3000, () => {
  console.log('server is running on 3000')
})

async function analysis() {
  let oldMap = new Map();
  let newMap = new Map();

  let { ships: oldStub } = oldMockupData;
  let { ships: newStub } = newMockupData;


  oldMap = new Map(newMap);
  function createMap(data, map) {
    data.forEach(ship => {
      map.set(ship.registration_id, ship);
    })
  }
  createMap(oldStub, oldMap);
  createMap(newStub, newMap);


  const blackList = new Map();

  function compareAndUpdateBlacklist() {
    // Loop through keys in oldMap
    for (const [key, value] of oldMap.entries()) {
      // If key in oldMap is not presented in newMap
      if (!newMap.has(key)) {
        // Check if the record already exists in blackList
        if (blackList.has(key)) {
          // Update the existing record in blackList
          const blackListItem = blackList.get(key);
          blackListItem.occurrences += 1;
          blackListItem.array_of_details.push(value);
        } else {
          // Create a new record in blackList
          blackList.set(key, {
            occurrences: 1,
            array_of_details: [value],
          });
        }
      }
    }
  }
  compareAndUpdateBlacklist();
  return blackList;
}

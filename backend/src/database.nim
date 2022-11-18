import norm/sqlite
let dbConn* = open(":memory:", "", "", "")

import ./models
proc createTables() =
  dbConn.createTables(newMessage())

createTables()
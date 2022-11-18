import std/jsonutils
import norm/sqlite
import prologue

import ./database
import ./models


proc getMessage*(ctx: Context) {.async.} =
  var allMessages = @[newMessage()]

  dbConn.selectAll(allMessages)

  resp $toJson(allMessages)


proc addMessage*(ctx: Context) {.async, gcsafe.} =
  try:
    var newMsg = jsonTo(parseJson(ctx.request.body), Message, Joptions(allowMissingKeys: true))
    dbConn.insert(newMsg)
    resp $toJson(parseJson("""{"success": true}"""))
  except:
    resp $toJson(parseJson("""{"success": false}"""))
when isMainModule:
  import logging
  addHandler newConsoleLogger(fmtStr = "")

  # import allographer/query_builder
  import ./database
  import ./models
  import norm/sqlite
  var defaultMsgs = @[
    newMessage(text = "Hello"),
    newMessage(text = "Good evening")
  ]
  dbConn.insert(defaultMsgs)

  import prologue
  var server = newAppQueryEnv()

  import prologue/middlewares/cors
  server.use(CorsMiddleware(allowOrigins = @["*"], allowMethods = @["*"], allowHeaders = @["content-type"]))

  # Be careful with the routes.
  import ./urls
  server.addRoute(urlPatterns, "")
  server.run()

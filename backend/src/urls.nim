import prologue

import ./views

let urlPatterns* = @[
  pattern("/message/get", getMessage, @[HttpGet]),
  pattern("/message/add", addMessage, @[HttpPost])
]

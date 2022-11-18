import norm/model


type
  Message* = ref object of Model
    text*: string

func newMessage*(text = ""): Message =
  Message(text: text)

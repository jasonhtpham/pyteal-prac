from pyteal import *

def clear_state_program():
  program = Seq([
    Return(Int(1))
  ])
  return program

with open("simple_clear.teal", "w") as f:
    compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=2)
    f.write(compiled)
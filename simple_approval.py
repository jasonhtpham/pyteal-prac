from pyteal import *

def simple_approval():
  # This function will be called upon SC initialization.
    on_create = Seq([
      App.globalPut(Bytes("number"), Int(0)),
      Return(Int(1)),
    ])

    # Set the global variable to provided value
    set_number = Seq([
      # Take 2nd argument in the transaction as number
      App.globalPut(Bytes("number"),Btoi(Txn.application_args[1])),
      Return(Int(1)),
    ])

    # Determine which function to call
    called_function = Txn.application_args[0]
    handle_noop = Cond(
      [called_function == Bytes("set_number"), set_number]
    )

    handle_optin = Seq([
        Return(Int(1))
    ])

    handle_closeout = Seq([
        Return(Int(1))
    ])

    handle_updateapp = Err()

    handle_deleteapp = Err()

    program = Cond(
      
        [Txn.application_id() == Int(0), on_create],
        [Txn.on_completion() == OnComplete.NoOp, handle_noop],
        [Txn.on_completion() == OnComplete.OptIn, handle_optin],
        [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp]
    )
    return program

with open('simple_approval.teal', 'w') as f:
    compiled = compileTeal(simple_approval(), Mode.Application, version=2)
    f.write(compiled)


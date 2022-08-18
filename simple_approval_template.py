from pyteal import *

def simple_approval():
    # TODO2: This sequence will be executed when the smart contract is initialized.

    # TODO4: The sequence to set the global variable number to provided value

    # TODO3: Determine which function to call based on the transaction argument
    # TODO3: Based on called_function, call the relevant function
    handle_noop = Seq([
        Return(Int(1))
    ])

    handle_optin = Seq([
        Return(Int(1))
    ])

    handle_closeout = Seq([
        Return(Int(1))
    ])

    handle_updateapp = Err()

    handle_deleteapp = Err()

    program = Cond(
        # TODO1: The function to call when the smart contract is initialized
        # The NoOp transaction calls handle_noop function
        [Txn.on_completion() == OnComplete.NoOp, handle_noop],
        # The OptIn transaction calls handle_optin function
        [Txn.on_completion() == OnComplete.OptIn, handle_optin],
        # The CloseOut transaction calls handle_closeout function
        [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
        # The UpdateApplication transaction calls handle_updateapp function
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
        # The DeleteApplication transaction calls handle_deleteapp function
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp]
    )
    return program


def clear_state_program():
  program = Seq([
    Return(Int(1))
  ])
  return program

with open('simple_approval.teal', 'w') as f:
    compiled = compileTeal(simple_approval(), Mode.Application, version=2)
    f.write(compiled)

with open("simple_clear.teal", "w") as f:
    compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=2)
    f.write(compiled)
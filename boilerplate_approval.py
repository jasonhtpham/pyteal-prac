from pyteal import *

# This is the main ApprovalProgram of the contract.
def approval_program():
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

    # The execution starts from here
    # Based on the transaction type, the relevant function is called.
    program = Cond(
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

# This is the code telling the program to 
# compile this to boilerplate_approval_pyteal.teal file
with open('boilerplate_approval_pyteal.teal', 'w') as f:
    compiled = compileTeal(approval_program(), Mode.Application, version=5)
    f.write(compiled)
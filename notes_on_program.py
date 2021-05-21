# Currently using the customer side pay_entry to cover both check if they have paid already and if they can afford
# it. Seems weird to only have the till function increase the till. Seems like they should be linked, but can't
# seem to get it to all connect.
#   As its currently constructed, its possible that the customer will pay, but by time it comes to receiving the
#   money entry_paid will already be True so won't take payment into the till.

#
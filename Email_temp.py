def format(msg):
    com_dat = []
    for i,data in enumerate(msg):
        dat =(f"{i}. | {msg[i][0]} | {msg[i][1]} | {msg[i][2]}.")
        com_dat.insert(i,dat)
    final = "\n".join(com_dat)

    return final




total_throw = 0
total_heads = 0
total_tail = 0
percentage_heads = 0.0
while True:
    user_input = input("Throw the coin and enter head or tail here: ?")
    user_input = user_input.lower()
    total_throw = total_throw + 1
    file_msg = []
    match user_input:
        
        case "head":
            total_heads = total_heads + 1
            percentage_heads = (total_heads/total_throw)*100
            print("Heads:",percentage_heads)
            
            with open("arditsulce-1/app1/coin.txt", "r") as file:
                file_msg = file.readlines() 
                
            file_entry = f"The user entered {user_input} and the current percentage is {percentage_heads}"
            file_entry = file_entry + "\n"
            file_msg.append(file_entry)
                           
            
            with open("arditsulce-1/app1/coin.txt", "w") as file:
                file.writelines(file_msg)
                
        case "tail":    
            total_tail = total_tail + 1
            percentage_heads = (total_heads/total_throw)*100
            print("Heads:",percentage_heads)
            with open("arditsulce-1/app1/coin.txt", "r") as file:
                file_msg = file.readlines() 
                
            file_entry = f"The user entered {user_input} and the current percentage is {percentage_heads}"
            file_entry = file_entry + "\n"
            file_msg.append(file_entry)
                           
            
            with open("arditsulce-1/app1/coin.txt", "w") as file:
                file.writelines(file_msg)
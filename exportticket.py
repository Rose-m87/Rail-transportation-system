
def export_ticket(username, train_name, qty, total_price):
    exact_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    filename = f"ticket_{username}_{exact_time}.txt"
    ticket_info = f"""

    Buyer Name: {username}
    Train Name: {train_name}
    Quantity: {qty}
    Total Price: {total_price}
    Purchase Time: {exact_time}
    
    """

    with open(filename, "w") as f:
        f.write(ticket_info)

    print(f"Ticket exported successfully! Details saved to {filename}")

    
    
        

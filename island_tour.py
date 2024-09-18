def read_input():
    H = int(input().strip())
    C = int(input().strip())
    customers = []

    for _ in range(C):
        customer_prefs = input().strip().split(', ')
        prefs = []
        for pref in customer_prefs:
            hop, transport = pref.split()
            hop = int(hop)
            prefs.append((hop, transport))
        customers.append(prefs)

    return H, C, customers


def create_itinerary(H, customers):
    itinerary = [None] * H
    hop_preferences = {}

    for customer in customers:
        for hop, transport in customer:
            if hop not in hop_preferences:
                hop_preferences[hop] = set()
            hop_preferences[hop].add(transport)

    for hop, transports in hop_preferences.items():
        if len(transports) > 1:
            conflicting_customers = [
                customer for customer in customers if any(h == hop for h, _ in customer)
            ]
            can_satisfy_with_others = False
            for customer in conflicting_customers:
                if len(customer) > 1:
                    can_satisfy_with_others = True
                    break
            if not can_satisfy_with_others:
                return None

    for customer in customers:
        customer_satisfied = False
        for hop, transport in customer:
            if transport == 'by-sea':
                if itinerary[hop] is None:
                    itinerary[hop] = 'by-sea'
                    customer_satisfied = True
                    break
                elif itinerary[hop] == 'by-sea':
                    customer_satisfied = True
                    break

        if not customer_satisfied:
            for hop, transport in customer:
                if transport == 'airborne':
                    if itinerary[hop] is None:
                        itinerary[hop] = 'airborne'
                        customer_satisfied = True
                        break
                    elif itinerary[hop] == 'airborne':
                        customer_satisfied = True
                        break
        
        if not customer_satisfied:
            return None

    for i in range(H):
        if itinerary[i] is None:
            itinerary[i] = 'by-sea'

    return itinerary

def format_output(itinerary):
    if itinerary is None:
        return "NO ITINERARY"
    else:
        return ', '.join(f"{i} {itinerary[i]}" for i in range(len(itinerary)))


def main():
    H, C, customers = read_input()
    itinerary = create_itinerary(H, customers)
    print(format_output(itinerary))


if __name__ == "__main__":
    main()

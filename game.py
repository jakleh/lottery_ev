from datetime import datetime

class Game():
    def __init__(self, name, tickets, cost, standard):
        self.name = name
        self.tickets = tickets
        self.cost = cost
        self.standard = standard

        #Record of projected payouts over time
        self.record = [()]

    def __str__(self):
        return self.name

    def calc_payout(self, prizes):

        counts = prizes.values()
        p_start = p_remaining = 0

        for p in counts:
            p_start += p[0]
            p_remaining += p[1]

        #This is our key assumption...
        tickets_remaining = (p_remaining/p_start) * self.tickets
        print("remaining:", tickets_remaining)

        #Payout = sum of prize values weighted by projected odds divided by ticket cost
        payout = (sum([i * (prizes[i][1] / tickets_remaining) for i in prizes]) - self.cost) / self.cost

        #Add tuple of payout and current time to list of records
        self.record += [(payout, datetime.now().strftime("%H:%M:%S"))]

        return payout / self.cost

    def show_payout(self):
        return "\"{name}\" proj. payout: {proj:.1f}%. Std payout: {std:.1f}%.".format(name=self.name, \
        proj=round(self.record[-1][0], 3) * 100, std=round(self.standard - 1, 3) * 100)

    def clear_record(self):
        self.record = [()]

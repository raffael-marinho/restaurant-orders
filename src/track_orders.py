class TrackOrders:
    def __init__(self):
        self.__orders = []

    def __len__(self):
        return len(self.__orders)

    def add_new_order(self, customer, order, day):
        self.__orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        dict = {}
        for target, order, _ in self.__orders:
            if target == customer:
                dict[order] = dict.get(order, 0) + 1

        return max(dict, key=dict.get)

    def get_never_ordered_per_customer(self, customer):
        dishes = set()
        dishes_ordered = set()

        for cust, dish, day in self.__orders:
            dishes.add(dish)

            if cust == customer:
                dishes_ordered.add(dish)

        never_ordered_dishes = dishes.difference(dishes_ordered)

        return never_ordered_dishes

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        days_visited = set()

        for cust, dish, day in self.__orders:
            days.add(day)

            if cust == customer:
                days_visited.add(day)

        never_visited_days = days.difference(days_visited)

        return never_visited_days

    def get_busiest_day(self):
        days = {}

        for day in self.__orders:
            if day[2] not in days:
                days[day[2]] = 0
            else:
                days[day[2]] += 1

        return max(days, key=days.get)

    def get_least_busy_day(self):
        day_list = []
        for customer, order, day in self.__orders:
            if (customer == customer):
                day_list.append(day)

        return min(set(day_list), key=day_list.count)

import csv
from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    file_txt = path_to_file.endswith(".csv")
    if not file_txt:
        raise FileNotFoundError(f"Extensão inválida:'{path_to_file}'")
    try:
        trackOrders = TrackOrders()
        with open(path_to_file) as file:
            file_read = csv.reader(file)

            for name, order, day in file_read:
                trackOrders.add_new_order(name, order, day)
            food = trackOrders.get_most_ordered_dish_per_customer("maria")
            times = trackOrders.get_quantity_of_order("arnaldo", "hamburguer")
            plates = trackOrders.get_never_ordered_per_customer("joao")
            days = trackOrders.get_days_never_visited_per_customer("joao")

            with open("data/mkt_campaign.txt", mode="w") as file2:
                file2.write(f'{food}\n{times}\n{plates}\n{days}')

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

class Clothing:
    """Базовый класс для одежды."""
    def __init__(self, name, size, fabric_price, accessories_cost, work_cost):
        self.name = name
        self.size = size
        self.fabric_price = fabric_price
        self.accessories_cost = accessories_cost
        self.work_cost = work_cost

    def calculate_fabric(self):
        """Расход ткани в метрах. Должен быть переопределён."""
        raise NotImplementedError("Метод calculate_fabric должен быть переопределён")

    def calculate_total_cost(self):
        """Итоговая стоимость пошива."""
        fabric_cost = self.calculate_fabric() * self.fabric_price
        return fabric_cost + self.accessories_cost + self.work_cost

    def __str__(self):
        return (f"{self.name} (размер {self.size}): ткань {self.calculate_fabric():.2f} м, "
                f"стоимость {self.calculate_total_cost():.2f} руб.")


class Jacket(Clothing):
    def __init__(self, size, fabric_price, accessories_cost, work_cost):
        super().__init__("Пиджак", size, fabric_price, accessories_cost, work_cost)

    def calculate_fabric(self):
        # Пример формулы: 1.5 м + 0.1 м на каждый размер свыше 44
        return 1.5 + max(0, self.size - 44) * 0.1


class Trousers(Clothing):
    def __init__(self, size, fabric_price, accessories_cost, work_cost):
        super().__init__("Брюки", size, fabric_price, accessories_cost, work_cost)

    def calculate_fabric(self):
        # Пример: 1.0 м + 0.05 м на размер свыше 44
        return 1.0 + max(0, self.size - 44) * 0.05


class ThreePieceSuit(Clothing):
    def __init__(self, size, fabric_price, accessories_cost, work_cost):
        super().__init__("Костюм-тройка", size, fabric_price, accessories_cost, work_cost)

    def calculate_fabric(self):
        # Пиджак + брюки + жилет
        jacket = Jacket(self.size, self.fabric_price, 0, 0).calculate_fabric()
        trousers = Trousers(self.size, self.fabric_price, 0, 0).calculate_fabric()
        vest = 0.8 + max(0, self.size - 44) * 0.03
        return jacket + trousers + vest

    def calculate_total_cost(self):
        # Для костюма-тройки фурнитура и работа задаются общие, но можно и детализировать
        return super().calculate_total_cost()
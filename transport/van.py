from transport.vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, capacity, is_refrigerated):
        super().__init__(capacity, is_refrigerated)
        if not (isinstance(is_refrigerated, bool)):
            raise ValueError("Флаг VIP статуса указан некорректно.")
        self.is_refrigerated = bool(is_refrigerated)


    def __str__(self):
        return f"Van(ID: {self.vehicle_id}, Capacity: {self.capacity}, Current Load: {self.current_load},Is_refrigerated : {self.is_refrigerated })"
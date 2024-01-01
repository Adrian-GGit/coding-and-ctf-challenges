class SeatManager:
    def __init__(self, n: int):
        self.heap = []
        self.counter = 0

    def reserve(self) -> int:
        if not self.heap:
            self.counter += 1
            return self.counter
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
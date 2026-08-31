class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        positions = []
        for i, p in enumerate(position):
            s = speed[i]
            positions.append((p, s))

        positions_sorted = sorted(positions, key=lambda x: x[0])
        # print(positions_sorted)

        fleets = []
        top_time = target + 1
        for i, car in enumerate(positions_sorted):
            car_p, car_s = car
            car_time = (target - car_p) / car_s

            if car_time < top_time:
                fleets.append(car_time)
                top_time = car_time
                # print(fleets)
            elif car_time > top_time:
                while car_time > top_time and fleets:
                    top_time = fleets.pop()
                fleets.append(car_time)


        # print(fleets)
        ans = len(fleets)
        return ans
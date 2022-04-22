## Solution: Sliding window

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        track = {}
        valid = 0
        for c in s1:
            if not c in track:
                track[c] = 0
            track[c] += 1
        target = track.copy()


        start, end = 0, 0
        while start < len(s2) and end < len(s2):
            c = s2[end]

            if c in track:
                if track[c] <= 0:
                    # target contains c, but c is full
                    while True:
                        if track[s2[start]] == 0:
                            valid -= 1
                        track[s2[start]] += 1
                        if s2[start] == c:
                            start += 1
                            break
                        start += 1

                # target contains c, and c is not full yet
                track[c] -= 1
                if track[c] == 0:
                    valid += 1

                # check for valid permutation:
                if valid == len(track):
                    return True

                end += 1

            else:
                # target does not contain c, discard the current window
                valid = 0
                for c in track:
                    track[c] = target[c]
                start = end + 1
                end = start

        return False

import heapq

class Solution(object):
    def getSkyline(self, buildings):
        # Create events
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))  # building start
            events.append((R, 0, 0))   # building end
        
        # Sort events
        events.sort()
        
        result = []
        heap = [(0, float('inf'))]  # (height, end)
        prev_height = 0
        
        for x, negH, R in events:
            
            # Remove buildings that ended
            while heap[0][1] <= x:
                heapq.heappop(heap)
            
            # Add new building
            if negH != 0:
                heapq.heappush(heap, (negH, R))
            
            # Current max height
            curr_height = -heap[0][0]
            
            # If height changed → skyline point
            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height
        
        return result
        
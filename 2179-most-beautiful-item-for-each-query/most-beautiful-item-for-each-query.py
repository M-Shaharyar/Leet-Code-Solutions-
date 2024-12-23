class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price (ascending order)
        items.sort()
        
        # Pair each query with its index and sort queries by the query value
        queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        max_bea = 0  # Variable to keep track of the maximum beauty encountered so far
        j = 0  # Pointer to iterate through the items list
        
        res = [0] * len(queries)  # Initialize result array with zeros
        
        # Process each query in sorted order
        for q, i in queries:
            # Update max_bea for all items with price <= current query value
            while j < len(items) and items[j][0] <= q:
                max_bea = max(max_bea, items[j][1])
                j += 1
            
            # Store the maximum beauty for the current query
            res[i] = max_bea
        
        return res

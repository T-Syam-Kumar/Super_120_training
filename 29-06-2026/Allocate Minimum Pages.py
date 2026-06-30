def findPages(self, arr, k):
        n = len(arr)

        if k > n:
            return -1

        def canAllocate(maxPages):
            students = 1
            pages = 0

            for book in arr:
                if pages + book <= maxPages:
                    pages += book
                else:
                    students += 1
                    pages = book

            return students <= k

        low = max(arr)
        high = sum(arr)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if canAllocate(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

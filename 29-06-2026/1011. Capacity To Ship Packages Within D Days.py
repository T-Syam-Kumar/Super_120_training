def shipWithinDays(weights, days) :
        l = max(weights)
        r = sum(weights)
        def checker(max_cap,weights,days):
            day = 1
            capacity = 0
            for weight in weights:
                if capacity + weight<= max_cap:
                    capacity+=weight
                else:
                    day+=1
                    capacity = weight
                    if day > days:
                        return False
            return True
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if checker(mid,weights,days):
                ans =  mid
                r = mid-1 
            else:
                l = mid+1
        return ans
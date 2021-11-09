def solution(cacheSize, cities):
    executionTime = 0
    cache = []
    
    for idx in range(0, len(cities)):
        
        city = cities[idx].lower()
        if not cache:
            if cacheSize > 0 and len(cache) < cacheSize:
                cache.insert(0, city)
            executionTime += 5
            #print("miss1 ", city, executionTime)
        
        elif not city in cache and cache:
            if len(cache) >= cacheSize:
                cache.pop(-1)
            cache.insert(0, city)
            executionTime += 5
            #print("miss2 ", city, executionTime)
            
        elif city in cache:
            cache.remove(city)
            cache.insert(0, city)
            executionTime += 1
            #print("hit ", city, executionTime)
        
    return executionTime
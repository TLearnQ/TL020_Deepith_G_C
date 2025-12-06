services = []

def router(method,path,data= None):
    if method=="GET" and path =="/items":
        return data
    elif method =="POST" and path=="/items":
        services.append(data)
        return {"added":True}
    elif method =="GET" and path=="/stats":
        return ("total: ",len(services))
    elif method!="GET" or method!="POST":
        return (method+": "+"Service currently unavailable")
    
print(router("GET","/items",{"sid":1,"service":"User data handling"}))
print(router("POST","/items",{"sid":4,"service":"Robotic process automation"}))
print(router("POST","/items"))
print(router("GET","/stats"))
print(router("PATCH","/items"))
print(router("DELETE","/stats"))
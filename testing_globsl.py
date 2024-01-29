from collections import deque

customers = deque(['daniel', 'mark'])
print(customers)
customers.append('simon')
print(customers)

customer = customers.popleft()
print(customer)
print (customers)
customers.appendleft("


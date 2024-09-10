select 
    name as Customers
from
    Customers left join orders
on 
    Customers.id = orders.customerId
where
    isnull(customerId)
from acme import Product
import random
from collections import Counter

adj = random.sample(['Awesome', 'Shiny', 'Impressive',
  'Portable', 'Improved'],1)

noun = random.sample(['Anvil', 'Catapult' ,'Disguise' ,'Mousetrap', '???'],1)

# concatenate adj and noun into one product name
name = adj[0] + " " + noun[0]

# set values
price = random.randint(5,100)
weight = random.randint(5,100)
flammability = random.uniform(0.0,2.5)

def generate_products(name,price,weight,flamability,quantity = 30):

    prod = []

    for i in range(quantity):
        prod.append(Product(name,price,weight,flamability))

    return prod

def inventory_report(prod_list):
    
    names = []
    mean_price = []
    mean_weight = []
    mean_flame = []

    for prod in prod_list:
        names.append(prod.name)
        mean_price.append(prod.price)
        mean_weight.append(prod.weight)
        mean_flame.append(prod.flammability)

    
    freq = list(Counter(names).values())
    unique = []

    # get unique names
    for i in range(len(freq)):
        if freq[i] == 1:
            unique.append(names[i])
    
    avg_price = sum(mean_price) / len(mean_price)
    avg_weight = sum(mean_weight) / len(mean_weight)
    avg_flame = sum(mean_flame) / len(mean_flame)
    
    # report
    print(f"There were {len(unique)} unique products.")
    print(f"The average price is: ${avg_price}.")
    print(f"The average weight is: {avg_weight} lbs.")
    print(f"The average flammability is: {avg_flame}.")



prod = generate_products(name,price,weight,flammability)
inventory_report(prod)

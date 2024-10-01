from datetime import datetime
from pymongoServer import startCollection
from fake_day_data_creator import create_days_array
from fake_product_data_creator import create_products_array
from . import create_ingredients_array
from fake_sale_data_creator import create_sales_array
from fake_worker_data_creator import create_workers_array
from fake_user_data_creator import create_users_array
from fake_company_data_creator import create_companies_array

collectionName = 'lizCafeteria'
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 7, 31)
# start_date = datetime(2024, 7, 31)
# end_date = datetime(2024, 7, 31)

collection = startCollection(collectionName)
usersCollection = startCollection('users')
dayCollection = collection['day']
productCollection = collection['product']
ingredientCollection = collection['ingredient']
saleCollection = collection['sale']
workerCollection = collection['worker']
userCollection = usersCollection['user']
companyCollection = usersCollection['companies']

# list_of_fake_days = create_days_array(start_date, end_date)
# list_of_fake_products = create_products_array()
list_of_fake_ingredients = create_ingredients_array()
# list_of_fake_sales = create_sales_array(start_date, end_date)
# list_of_fake_workers = create_workers_array()
# list_of_fake_users = create_users_array()
# list_of_fake_companies = create_companies_array()

# dayCollection.insert_many(list_of_fake_days)
# productCollection.insert_many(list_of_fake_products)
ingredientCollection.insert_many(list_of_fake_ingredients)
# saleCollection.insert_many(list_of_fake_sales)
# workerCollection.insert_many(list_of_fake_workers)
# userCollection.insert_many(list_of_fake_users)
# companyCollection.insert_many(list_of_fake_companies)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

'''
Далее приведен тестовый DataFrame
'''
spark = SparkSession.builder.appName('ProductCategoryExample').getOrCreate()

products_data = [(1, 'Laptop'), (2, 'Smartphone'), (3, 'Tablet'), (4, 'Headphones')]
categories_data = [(1, 'Electronics'), (2, 'Computers'), (3, 'Mobile'), (4, 'Cars')]
product_category_data = [(1, 1), (1, 2), (2, 1), (2, 3), (3, 1)]


products_df = spark.createDataFrame(products_data, ['product_id', 'product_name'])
categories_df = spark.createDataFrame(categories_data, ['category_id', 'category_name'])
product_category_df = spark.createDataFrame(product_category_data, ['product_id', 'category_id'])


def get_products_with_categories(products_df, categories_df, product_category_df):

    product_category_pairs = (products_df
                            .join(product_category_df, 'product_id', 'left')
                            .join(categories_df, 'category_id', 'left')
                            .select(col('product_name'), col('category_name')))

    return product_category_pairs


result = get_products_with_categories(products_df, categories_df, product_category_df)
print(result.show())
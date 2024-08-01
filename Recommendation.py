import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
file_path = r"C:\Users\ferna\OneDrive\Desktop\Python\CodSoft\Dataset\amazon.csv"
dataset = pd.read_csv(file_path)
user_product_data = dataset[['user_id', 'product_id', 'product_name', 'category']]
user_product_data = user_product_data.set_index(['user_id']).product_id.str.split(',', expand=True).stack().reset_index(name='product_id')
user_item_matrix = user_product_data.pivot_table(index='user_id', columns='product_id', aggfunc='size', fill_value=0)
product_similarity = cosine_similarity(user_item_matrix.T)
product_similarity_df = pd.DataFrame(product_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)
product_id_to_name = dict(zip(dataset['product_id'], dataset['product_name']))
product_name_to_id = dict(zip(dataset['product_name'], dataset['product_id']))
product_id_to_category = dict(zip(dataset['product_id'], dataset['category']))
product_name_to_category = dict(zip(dataset['product_name'], dataset['category']))
def recommend_products_by_category(category, num_recommendations=5):
    products_in_category = dataset[dataset['category'] == category]['product_id']
    similarity_scores = product_similarity_df[products_in_category].mean(axis=1)
    sorted_scores = similarity_scores.sort_values(ascending=False)
    sorted_scores = sorted_scores[sorted_scores.index.map(lambda x: product_id_to_category[x] == category)]
    top_recommendations = sorted_scores.head(num_recommendations).index.tolist()
    top_recommendations_names = [product_id_to_name.get(pid, pid) for pid in top_recommendations]
    return top_recommendations_names
categories = dataset['category'].unique()
print("Available categories:")
for idx, category in enumerate(categories, start=1):
    print(f"{idx}. {category}")
user_input_category_index = int(input("Enter the number corresponding to the category: "))
user_input_category = categories[user_input_category_index - 1]
recommendations = recommend_products_by_category(user_input_category)
if isinstance(recommendations, str):
    print(recommendations)
else:
    print(f"Recommended products in the '{user_input_category}' category:")
    for idx, product_name in enumerate(recommendations, start=1):
        print(f"{idx}. {product_name}")
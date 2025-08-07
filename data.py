from datasets import load_dataset
from recommendme.data_loader import convert_to_json
import pandas as pd 
from recommendme.embeddings import Embedding
# df = pd.read_csv("BooksDataset.csv")
# # print(len(df)) 
# df_clean = df.drop(columns=["Publisher", "Publish Date", "Price"])
# # print(df_clean.head())
# df_clear = df_clean.dropna(subset=["Description"])
# df_clear.to_csv("cleaned.csv", index=False)




# # convert_to_json("cleaned.csv", field_map={"title": "Title","author": "Authors",  "desc": "Description", "category": "Category"}, default_fields=None, list_fields={"category": "Category"})
# ds = load_dataset("booksouls/goodreads-book-descriptions")
# # print(ds)

# # print(ds['train'][:1])
# ds['train'].to_csv("hf_dataset.csv")

# df = pd.read_csv("hf_dataset.csv")
# print(len(df))
# print(df.head(2))
# df_clean = df.dropna(subset=["description"])
# print(len(df_clean))
# df_clean.to_csv("hf_cleaned.csv", index=False)

# print(df_clean.columns)
# field_map ={
#     "title": "title", 
#     "desc": "description"
# }

# convert_to_json("hf_cleaned.csv", field_map=field_map, default_fields=None, list_fields=None)



# embed = Embedding("data/cleaned.json", text_template="title {title}. desc {desc} . category {category}")
# embed.generate_embeddings()


# print("FAISS index created and metadata saved!")

# index = embed.get_faiss_embeddings()
# metadata = embed.get_metadata()

# print(f"Loaded FAISS index with {index.ntotal} vectors")
# print(f"Metadata loaded: {len(metadata)} entries")
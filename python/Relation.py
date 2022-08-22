
# pip install pandas
import pandas as pd

relationship_df = pd.read_csv('relationship.csv')

tax_id_df = pd.read_csv('parasites_py.csv')


found_tax_ids = []
found_parent_tax_ids = []

# find first level rel
for tax_id in tax_id_df['tax_id']:
    target_df = relationship_df[relationship_df['tax_id'] == tax_id]
    parent_tax_ids = target_df['parent_tax_id']
    for parent_tax_id in parent_tax_ids:
        if parent_tax_id == tax_id:
            continue

        found_tax_ids.append(tax_id)
        found_parent_tax_ids.append(parent_tax_id)


# copy parent id to need_process_parent_tax_ids
need_process_parent_tax_ids = found_parent_tax_ids[::]


while len(need_process_parent_tax_ids)!=0:

    pop_parent_tax_id = need_process_parent_tax_ids.pop()


    target_df = relationship_df[relationship_df['tax_id'] == pop_parent_tax_id]
    if len(target_df)==0:
        continue


    parent_tax_ids = target_df['parent_tax_id']

    for parent_tax_id in parent_tax_ids:
        # skip if same
        if parent_tax_id == pop_parent_tax_id:
            continue

        # if exist
        if pop_parent_tax_id in found_tax_ids and parent_tax_id in found_parent_tax_ids:
            continue
        # not same save
        found_tax_ids.append(pop_parent_tax_id)
        found_parent_tax_ids.append(parent_tax_id)


        if parent_tax_id in need_process_parent_tax_ids:
            continue

        need_process_parent_tax_ids.append(parent_tax_id)


df = pd.DataFrame({
    "tax_id":found_tax_ids,
    "parent_tax_id":found_parent_tax_ids
})


df.to_csv('output.csv', index=False)












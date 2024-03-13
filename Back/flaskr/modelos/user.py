import pandas as pd

file_path = 'userid-profile.tsv'

df = pd.read_csv(file_path, sep='\t', skiprows = 1, on_bad_lines='skip',header = None,names = ["id","gender","age","country","registered"])
df['age'] = df['age'].fillna(0).astype(int)

def add_user(df, gender, age, country, registered):
    user_id = f"user_{len(df) + 9:06d}"
    new_user = pd.DataFrame({
        'id': [user_id],
        'gender': [gender],
        'age': [age],
        'country': [country],
        'registered': [registered]
    })
    df = df.append(new_user, ignore_index=True)
    return df

def calculate_distance(user1, user2):
    gender_distance = 1 if user1['gender'] != user2['gender'] else 0
    country_distance = 7 if user1['country'] != user2['country'] else 0
    age_distance = abs(int(user1['age']) - int(user2['age']))
    return gender_distance + country_distance + age_distance

def find_closest_user(target_user, df):
    min_distance = float('inf')
    closest_user = None
    for _, row in df.iterrows():
        distance = calculate_distance(target_user, row)
        if distance < min_distance:
            min_distance = distance
            closest_user = row
    return closest_user["id"]
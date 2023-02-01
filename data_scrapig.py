np.random.seed(2015)
df = pd.DataFrame([])
for i in range(5):
    data = dict(zip(np.random.choice(10, replace=False, size=5),
                    np.random.randint(10, size=5)))
    data = pd.DataFrame(data.items())
    data = data.transpose()
    data.columns = data.iloc[0]
    data = data.drop(data.index[[0]])
    df = df.append(data)
print('{}\n'.format(df))
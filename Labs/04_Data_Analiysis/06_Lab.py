
import pandas as pd


df = pd.read_csv('Data/youtube-ing.csv')


# En çok görüntülenmeye sahip video

print(df[df['views'] == df['views'].max()][['title']])

# En çok görüntülenmeye sahip ilk 10 farklı videonun title views sütunlarını ekrana basın

print(df.groupby('title').sum(numeric_only=True).sort_values(by='views', ascending=False)[['views']].head(10))

# categorilerine göre likes ortalamasını bulun

print(df.groupby('category_id')['likes'].mean())

# hangi kanal ne kadar yorum almış

print(df.groupby('channel_title').sum(numeric_only=True)[['comment_count']])

# her bir video için kullanılan tag sayısını tag_count isimli yeni bir sütuna yazdıralım


def tag_count(tag: str):
    return len(tag.split('|'))


# Yol 1
df['tag_count'] = df['tags'].apply(tag_count)
print(df[['title', 'tag_count']])

# Yol 2
df['tag_count'] = df['tags'].apply(lambda x: len(x.split('|')))
print(df[['title', 'tag_count']])


# Her bir videonun like ve dislike oranını bulalım. like_avg isimli yeni bir sütuna bu bilgiyi yazalım.Yazacağınız function argüman olarak veri setini alacak. Yukarıda elde edilen like_avg sütununu kullanarak bir sorgu yazalım.


def like_dislike_avg(data_set: pd.DataFrame):
    like_list = list(data_set['likes'])
    dislike_list = list(data_set['dislikes'])

    comb_list = list(zip(like_list, dislike_list))

    avg_list = []
    for like, dislike in comb_list:
        if like + dislike == 0:
            avg_list.append(0)
        else:
            avg_list.append(like / (like + dislike))

    return avg_list


df['like_avg'] = like_dislike_avg(df)

print(df.sort_values(by='like_avg', ascending=False)[['title', 'likes', 'dislikes', 'like_avg']])


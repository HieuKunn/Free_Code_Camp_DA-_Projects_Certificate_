import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight']/(df['height']/100 )**2 > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int) # -> turn into true/false or 1/0
df['gluc'] = (df['gluc'] > 1).astype(int) # -> turn into true/false or 1/0

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars = ['cardio'],
        value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    # melt dùng để biến đổi từ dữ liệu hàng ngang sang dữ liệu hàng dọc

    # 6
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name = 'total')
    # -> Gom tất cả những dòng giống hệt nhau về cả 3 yếu tố này lại thành một đống, rồi đếm xem đống đó có bao nhiêu người"
    # -> total đi đếm xem có bao nhiêu 1 với 0 

    # 7
    draw_bar = sns.catplot(
        data = df_cat,
        x = 'variable',
        y = 'total',
        hue = 'value',
        col = 'cardio',
        kind = 'bar'
    )
    # -> seaborn không trực tiếp trả về fig mà trả về đối tương bọc ngoài seaborn là FacetGrid


    # 8
    fig = draw_bar.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    # -> Mục đích trong Data Science: Dùng để lọc nhiễu / ngoại lai (outliers). 
    #   Trong tập dữ liệu y tế, có thể có lỗi nhập liệu như chiều cao 50 cm hoặc 250 cm.
    #   Bằng cách chỉ lấy khoảng từ phân vị 0.025 đến 0.975, dữ liệu sẽ loại bỏ 2.5% 
    #   giá trị cực thấp và 2.5% giá trị cực cao ở hai đầu rìa, chỉ giữ lại 95% dữ liệu chuẩn ở giữa.

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # triu ~ triangle upper
    #có thể viết ngắn np_triu(corr)


    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )

    # 16
    fig.savefig('heatmap.png')
    return fig

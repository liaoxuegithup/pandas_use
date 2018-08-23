import numpy as np
import pandas as pd

df = pd.DataFrame(pd.read_csv('tox21.csv',header=2))
# print(df)
# print(df.shape)
# 查看表的纬度，行，列
# print(df.info())
# 数据表基本信息（维度、列名称、数据格式、所占空间等）：
# print(df.dtypes)
# 每一列数据的格式
# df['NR-AR'].dtype
# 某一列格式：
# print(df.isnull())
# 查看某一列空值：
# print(df.values)
# 查看多有表的值，返回的是列表

# print(df.columns)
# 只能取一列
# print(df.head())
# 查看前几行数据，为什么我的是5
# print(df.tail())
# 默认是后5行数据
# print(df.fillna(value=0))
# 用数字0填充空值
# df['NR-AR']=df['NR-AR'].map(str.strip)
# 清楚city字段的字符空格
# 、删除后出现的重复值：
#
# df['city'].drop_duplicates()
#
# 8、删除先出现的重复值：
#
# df['city'].drop_duplicates(keep='last')
# 1
# 2
# 9、数据替换：
#
# df['city'].replace('sh', 'shanghai')
# 1
# 2
# 四、数据预处理
#
# df1=pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006,1007,1008],
# "gender":['male','female','male','female','male','female','male','female'],
# "pay":['Y','N','Y','Y','N','Y','N','Y',],
# "m-point":[10,12,20,40,40,40,30,20]})
# 1
# 2
# 3
# 4
# 5
# 1、数据表合并
#
# df_inner=pd.merge(df,df1,how='inner')  # 匹配合并，交集
# df_left=pd.merge(df,df1,how='left')        #
# df_right=pd.merge(df,df1,how='right')
# df_outer=pd.merge(df,df1,how='outer')  #并集
# 1
# 2
# 3
# 4
# 5
# 2、设置索引列
#
# df_inner.set_index('id')
# 1
# 2
# 3、按照特定列的值排序：
#
# df_inner.sort_values(by=['age'])
# 1
# 2
# 4、按照索引列排序：
#
# df_inner.sort_index()
# 1
# 2
# 5、如果prince列的值>3000，group列显示high，否则显示low：
#
# df_inner['group'] = np.where(df_inner['price'] > 3000,'high','low')
# 1
# 2
# 6、对复合多个条件的数据进行分组标记
#
# df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price'] >= 4000), 'sign']=1
# 1
# 2
# 7、对category字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列名称为category和size
#
# pd.DataFrame((x.split('-') for x in df_inner['category']),index=df_inner.index,columns=['category','size']))
# 1
# 2
# 8、将完成分裂后的数据表和原df_inner数据表进行匹配
#
# df_inner=pd.merge(df_inner,split,right_index=True, left_index=True)
# 1
# 2
# 五、数据提取
# 主要用到的三个函数：loc,iloc和ix，loc函数按标签值进行提取，iloc按位置进行提取，ix可以同时按标签和位置进行提取。
# 1、按索引提取单行的数值
#
# df_inner.loc[3]
# 1
# 2
# 2、按索引提取区域行数值
#
# df_inner.iloc[0:5]
# 1
# 2
# 3、重设索引
#
# df_inner.reset_index()
# 1
# 2
# 4、设置日期为索引
#
# df_inner=df_inner.set_index('date')
# 1
# 2
# 5、提取4日之前的所有数据
#
# df_inner[:'2013-01-04']
# 1
# 2
# 6、使用iloc按位置区域提取数据
#
# df_inner.iloc[:3,:2] #冒号前后的数字不再是索引的标签名称，而是数据所在的位置，从0开始，前三行，前两列。
# 1
# 2
# 7、适应iloc按位置单独提起数据
#
# df_inner.iloc[[0,2,5],[4,5]] #提取第0、2、5行，4、5列
# 1
# 2
# 8、使用ix按索引标签和位置混合提取数据
#
# df_inner.ix[:'2013-01-03',:4] #2013-01-03号之前，前四列数据
# 1
# 2
# 9、判断city列的值是否为北京
#
# df_inner['city'].isin(['beijing'])
# 1
# 2
# 10、判断city列里是否包含beijing和shanghai，然后将符合条件的数据提取出来
#
# df_inner.loc[df_inner['city'].isin(['beijing','shanghai'])]
# 1
# 2
# 11、提取前三个字符，并生成数据表
#
# pd.DataFrame(category.str[:3])
# 1
# 2
# 六、数据筛选
# 使用与、或、非三个条件配合大于、小于、等于对数据进行筛选，并进行计数和求和。
# 1、使用“与”进行筛选
#
# df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']]
# 1
# 2
# 2、使用“或”进行筛选
#
# df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']].sort(['age'])
# 1
# 2
# 3、使用“非”条件进行筛选
#
# df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id'])
# 1
# 2
# 4、对筛选后的数据按city列进行计数
#
# df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id']).city.count()
# 1
# 2
# 5、使用query函数进行筛选
#
# df_inner.query('city == ["beijing", "shanghai"]')
# 1
# 2
# 6、对筛选后的结果按prince进行求和
#
# df_inner.query('city == ["beijing", "shanghai"]').price.sum()
# 1
# 2
# 七、数据汇总
# 主要函数是groupby和pivote_table
# 1、对所有的列进行计数汇总
#
# df_inner.groupby('city').count()
# 1
# 2
# 2、按城市对id字段进行计数
#
# df_inner.groupby('city')['id'].count()
# 1
# 2
# 3、对两个字段进行汇总计数
#
# df_inner.groupby(['city','size'])['id'].count()
# 1
# 2
# 4、对city字段进行汇总，并分别计算prince的合计和均值
#
# df_inner.groupby('city')['price'].agg([len,np.sum, np.mean])
# 1
# 2
# 八、数据统计
# 数据采样，计算标准差，协方差和相关系数
# 1、简单的数据采样
#
# df_inner.sample(n=3)
# 1
# 2
# 2、手动设置采样权重
#
# weights = [0, 0, 0, 0, 0.5, 0.5]
# df_inner.sample(n=2, weights=weights)
# 1
# 2
# 3
# 3、采样后不放回
#
# df_inner.sample(n=6, replace=False)
# 1
# 2
# 4、采样后放回
#
# df_inner.sample(n=6, replace=True)
# 1
# 2
# 5、 数据表描述性统计
#
# df_inner.describe().round(2).T #round函数设置显示小数位，T表示转置
# 1
# 2
# 6、计算列的标准差
#
# df_inner['price'].std()
# 1
# 2
# 7、计算两个字段间的协方差
#
# df_inner['price'].cov(df_inner['m-point'])
# 1
# 2
# 8、数据表中所有字段间的协方差
#
# df_inner.cov()
# 1
# 2
# 9、两个字段的相关性分析
#
# df_inner['price'].corr(df_inner['m-point']) #相关系数在-1到1之间，接近1为正相关，接近-1为负相关，0为不相关
# 1
# 2
# 10、数据表的相关性分析
#
# df_inner.corr()
# 1
# 2
# 九、数据输出
# 分析后的数据可以输出为xlsx格式和csv格式
# 1、写入Excel
#
# df_inner.to_excel('excel_to_python.xlsx', sheet_name='bluewhale_cc')
# 1
# 2
# 2、写入到CSV
#
# df_inner.to_csv('excel_to_python.csv')
import streamlit as st
import json
import pandas as pd
import numpy as np
from PIL import Image
from datetime import datetime
import plotly.express as px

st.title('Price Analysis')
st.write('This page shows the price variations based of properties based on various factors such as location, type of property and so on.')

with open('sample_airbnb.json','r') as f:
    getfile = json.load(f)

getdf = pd.DataFrame(getfile)
getdf['_id'] = getdf['_id'].astype('int64')
getdf['minimum_nights'] = getdf['minimum_nights'].astype('int64')
getdf['maximum_nights'] = getdf['maximum_nights'].astype('int64')
getdf.fillna(0,inplace=True)

getcountrylist = []
gettownlist = []
getlatlist = []
getlonlist = []
for i in getdf['address']:
    getcountrylist.append(i['country'])
    gettownlist.append(i['market'])
    getlonlist.append(i['location']['coordinates'][0])
    getlatlist.append(i['location']['coordinates'][1])

col1,col2,col3,col4 = st.columns((1,1,1,1))
with col1:
    st.markdown(' ')
    st.markdown(' ')    
    getpropcont = st.container(height=150,border=False)
    getpropcont.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:orange[No. of Properties]',unsafe_allow_html=True)
    concatstr = '&nbsp;&nbsp;&nbsp;<font size="10"> :love_hotel:' + '&nbsp;&nbsp;&nbsp;<b>' + str(getdf.shape[0]) + '</b>'
    getpropcont.write(concatstr,unsafe_allow_html=True)
with col2:
    st.markdown(' ')
    st.markdown(' ')
    getpropcont = st.container(height=150,border=False)
    getpropcont.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:orange[Maximum Price (per day)]',unsafe_allow_html=True)
    getmaxprdf = getdf[getdf['price'] == getdf['price'].max()]
    getmaxprice = int(getmaxprdf.loc[:,'price'] + getmaxprdf.loc[:,'security_deposit'] + getmaxprdf.loc[:,'cleaning_fee'] + getmaxprdf.loc[:,'extra_people'] + getmaxprdf.loc[:,'guests_included'])
    concatstr = '&nbsp;&nbsp;&nbsp;<font size="10"> :heavy_dollar_sign:' + '&nbsp;&nbsp;&nbsp;<b> ' + str(getmaxprice) + '</b>' + '<font size="5">&nbsp;&nbsp;USD'
    getpropcont.write(concatstr,unsafe_allow_html=True)
with col3:
    st.markdown(' ')
    st.markdown(' ')
    getpropcont = st.container(height=150,border=False)
    getpropcont.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:orange[Minimum Price (per day)]',unsafe_allow_html=True)
    getminprdf = getdf[getdf['price'] == getdf['price'].min()]
    getminprice = int(getminprdf.loc[:,'price'] + getminprdf.loc[:,'security_deposit'] + getminprdf.loc[:,'cleaning_fee'] + getminprdf.loc[:,'extra_people'] + getminprdf.loc[:,'guests_included'])
    concatstr = '&nbsp;&nbsp;&nbsp;<font size="10"> :heavy_dollar_sign:' + '&nbsp;&nbsp;&nbsp;<b> ' + str(getminprice) + '</b>' + '<font size="5">&nbsp;&nbsp;USD'
    getpropcont.write(concatstr,unsafe_allow_html=True)
with col4:
    st.markdown(' ')
    st.markdown(' ')
    getpropcont = st.container(height=150,border=False)
    getpropcont.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:orange[Average Price (per day)]',unsafe_allow_html=True)
    getavgprdf = getdf[getdf['price'] == round(getdf['price'].mean())]
    getavgprice = int(getavgprdf.loc[:,'price'].mean() + getavgprdf.loc[:,'security_deposit'].mean() + getavgprdf.loc[:,'cleaning_fee'].mean() + getavgprdf.loc[:,'extra_people'].mean() + getavgprdf.loc[:,'guests_included'].mean())
    concatstr = '&nbsp;&nbsp;&nbsp;<font size="10"> :heavy_dollar_sign:' + '&nbsp;&nbsp;&nbsp;<b> ' + str(getavgprice) + '</b>' + '<font size="5">&nbsp;&nbsp;USD'
    getpropcont.write(concatstr,unsafe_allow_html=True)  

col5,col6=st.columns((1,1))
with col5:
    getloccont = st.container(height=600)
    concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font size = "5">' + ' Property Locations</b>'
    getloccont.write(concatstr,unsafe_allow_html=True)
    getloccontdf = pd.DataFrame(data=[getcountrylist,gettownlist,getdf['price']]).T
    getloccontdf.columns=['Country','Town','Price (in USD)']
    getcountry = getloccont.selectbox(label='Select a Country',options=getloccontdf['Country'].unique().tolist(),index=None)
    getloccontchart = getloccont.plotly_chart(px.bar(getloccontdf,y='Price (in USD)',x='Country'))

    if(getcountry):
        gettowndf = getloccontdf[getloccontdf['Country'] == getcountry]
        concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font size = "5">' + ' Property Towns</b>'
        getloccont.write(concatstr,unsafe_allow_html=True)        
        getloccont.plotly_chart(px.bar(gettowndf,y='Price (in USD)',x='Town'))

with col6:
    getproptypecont = st.container(height=600)
    concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font size = "5">' + ' Property Type</b>'
    getproptypecont.write(concatstr,unsafe_allow_html=True)
    getlist = []
    for i in getdf['property_type']:
        getlist.append(i)
    getproptypedf = pd.DataFrame(data=[getlist,getdf['price']]).T
    getproptypedf.columns=['Property Type','Price (in USD)']
    getproptypecont.plotly_chart(px.pie(getproptypedf,values='Price (in USD)',names='Property Type'))

st.markdown(' ')
col7,col8=st.columns((1,1))
with col7:
    getseasoncont = st.container(height=600)
    concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font size = "5">' + ' Seasonal Variations</b>'
    getseasoncont.write(concatstr,unsafe_allow_html=True)
    getseason = getseasoncont.selectbox(label='Select a Season',options=['Weekly','Monthly'],index=None)

    if(getseason == 'Weekly'):
        getseasondf = getdf.copy()
        getseasondf.insert(42,'Weekly Price Range (in USD)','')
        for i in getseasondf['_id'].index:
            getweekprice = int(getseasondf.loc[i,'weekly_price'])
            if(getweekprice == 0):
                getseasondf.drop(i,inplace=True)
            if(getweekprice > 0 and getweekprice <= 1000):
                getseasondf.at[i,'Weekly Price Range (in USD)'] = '0 to 1000'
            elif(getweekprice > 1000 and getweekprice <= 2000):
                getseasondf.at[i,'Weekly Price Range (in USD)'] = '1000 to 2000'
            elif(getweekprice > 2000 and getweekprice <= 3000):
                getseasondf.at[i,'Weekly Price Range (in USD)'] = '2000 to 3000'
            elif(getweekprice > 3000 and getweekprice <= 4000):
                getseasondf.at[i,'Weekly Price Range (in USD)'] = '3000 to 4000'
            elif(getweekprice > 4000 and getweekprice <= 5000):
                getseasondf.at[i,'Weekly Price Range (in USD)'] = '4000 to 5000'
            elif(getweekprice > 5000):
                getseasondf.at[i,'Weekly Price Range (in USD)'] = 'Over 5000+'
        getseasondf.sort_values('Weekly Price Range (in USD)',axis=0,ascending=True,inplace=True)
        getseasoncont.plotly_chart(px.density_heatmap(getseasondf,x='Weekly Price Range (in USD)'))
    elif(getseason == 'Monthly'):
        getseasondf = getdf.copy()
        getseasondf.insert(42,'Monthly Price Range (in USD)','')
        for i in getseasondf['_id'].index:
            getmonprice = int(getseasondf.loc[i,'monthly_price'])
            if(getmonprice == 0):
                getseasondf.drop(i,inplace=True)
            if(getmonprice > 0 and getmonprice <= 10000):
                getseasondf.at[i,'Monthly Price Range (in USD)'] = '0 to 10000'
            elif(getmonprice > 10000 and getmonprice <= 20000):
                getseasondf.at[i,'Monthly Price Range (in USD)'] = '10000 to 20000'
            elif(getmonprice > 20000 and getmonprice <= 30000):
                getseasondf.at[i,'Monthly Price Range (in USD)'] = '20000 to 30000'
            elif(getmonprice > 30000 and getmonprice <= 40000):
                getseasondf.at[i,'Monthly Price Range (in USD)'] = '30000 to 40000'
            elif(getmonprice > 40000):
                getseasondf.at[i,'Monthly Price Range (in USD)'] = 'Over 40000+'
        getseasondf.sort_values('Monthly Price Range (in USD)',axis=0,ascending=True,inplace=True)
        getseasoncont.plotly_chart(px.density_heatmap(getseasondf,x='Monthly Price Range (in USD)'))
with col8:
    getaccomcont = st.container(height=600)
    concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font size = "5">' + ' Accomodation</b>'
    getaccomcont.write(concatstr,unsafe_allow_html=True)
    getaccom = getaccomcont.selectbox(label='Select Features',options=['No. of Bedrooms','No. of Beds','No. of Amenities'],index=None)
    getlist = []
    for i in getdf['amenities']:
        getlist.append(len(i))
    getaccomdf = pd.DataFrame(data=[getlist,getdf['bedrooms'],getdf['beds'],getdf['price']]).T
    getaccomdf.columns=['No. of Amenities','No. of Bedrooms','No. of Beds','Price (in USD)']

    if(getaccom == 'No. of Bedrooms'):
        getaccomcont.plotly_chart(px.scatter(getaccomdf,x=getaccom,y='Price (in USD)'))
    elif(getaccom == 'No. of Beds'):
        getaccomcont.plotly_chart(px.scatter(getaccomdf,x=getaccom,y='Price (in USD)'))
    elif(getaccom == 'No. of Amenities'):
        getaccomcont.plotly_chart(px.scatter(getaccomdf,x=getaccom,y='Price (in USD)'))

st.markdown(' ')
st.markdown(' ')
tab1,tab2=st.tabs(['Most Rated','Most Available'])
with tab1:
    getmostreviewdf = getdf.copy()
    getmostreviewdf.insert(42,'Rating',0)
    getmostreviewdf.insert(43,'Accuracy',0)
    getmostreviewdf.insert(44,'Cleanliness',0)
    getmostreviewdf.insert(45,'Check-In',0)
    getmostreviewdf.insert(46,'Communication',0)
    getmostreviewdf.insert(47,'Location',0)
    getmostreviewdf.insert(48,'Value',0)
    getmostreviewdf.insert(49,'Thumbnail','')
    for i in getmostreviewdf['_id'].index:
        getdict = getmostreviewdf.loc[i,'review_scores']
        try:
            getmostreviewdf.at[i,'Rating'] = getdict['review_scores_rating']
            getmostreviewdf.at[i,'Accuracy'] = getdict['review_scores_accuracy']
            getmostreviewdf.at[i,'Cleanliness'] = getdict['review_scores_cleanliness']
            getmostreviewdf.at[i,'Check-In'] = getdict['review_scores_checkin']
            getmostreviewdf.at[i,'Communication'] = getdict['review_scores_communication']
            getmostreviewdf.at[i,'Location'] = getdict['review_scores_location']
            getmostreviewdf.at[i,'Value'] = getdict['review_scores_value']
        except:
            pass
        getdict = getmostreviewdf.loc[i,'images']
        getmostreviewdf.at[i,'Thumbnail'] = getdict['picture_url']

    getmostreviewdf.sort_values('Rating',ascending=False,inplace=True)
    for i in getmostreviewdf['_id'].index:
        if(getmostreviewdf.loc[i,'Rating'] == 0):
            getmostreviewdf.drop(i,inplace=True)

    getnewdf = getmostreviewdf[['Thumbnail','name','listing_url','property_type','price','Rating','Accuracy','Cleanliness','Check-In','Communication','Location','Value']]
    st.data_editor(
        getnewdf,
        column_config={
            'Thumbnail':st.column_config.ImageColumn(),
            'name':st.column_config.LinkColumn('Name',validate='listing_url'),
            'property_type':'Type',
            'price':st.column_config.NumberColumn('Price (in USD)',format='$ %d'),
            'Rating':st.column_config.NumberColumn(format='%d ⭐'),
            'Accuracy':st.column_config.ProgressColumn(width='small',min_value=0,max_value=10,format='%d'),
            'Cleanliness':st.column_config.ProgressColumn(width='small',min_value=0,max_value=10,format='%d'),
            'Check-In':st.column_config.ProgressColumn(width='small',min_value=0,max_value=10,format='%d'),
            'Communication':st.column_config.ProgressColumn(width='small',min_value=0,max_value=10,format='%d'),
            'Location':st.column_config.ProgressColumn(width='small',min_value=0,max_value=10,format='%d'),
            'Value':st.column_config.ProgressColumn(width='small',min_value=0,max_value=10,format='%d'),
        },
        column_order=['Thumbnail','name','property_type','price','Rating','Accuracy','Cleanliness','Check-In','Communication','Location','Value'],
        hide_index=True,
        height=1000,
        use_container_width=True)
with tab2:
    getmostavaildf = getdf.copy()
    getmostavaildf.insert(42,'Monthly (in days)',0)
    getmostavaildf.insert(43,'Bi-Monthly (in days)',0)
    getmostavaildf.insert(44,'Tri-Monthly (in days)',0)
    getmostavaildf.insert(45,'Yearly (in days)',0)
    getmostavaildf.insert(46,'Thumbnail',0)
    for i in getmostavaildf['_id'].index:
        getdict = getmostavaildf.loc[i,'availability']
        try:
            getmostavaildf.at[i,'Monthly (in days)'] = getdict['availability_30']
            getmostavaildf.at[i,'Bi-Monthly (in days)'] = getdict['availability_60']
            getmostavaildf.at[i,'Tri-Monthly (in days)'] = getdict['availability_90']
            getmostavaildf.at[i,'Yearly (in days)'] = getdict['availability_365']
        except:
            pass
        getdict = getmostavaildf.loc[i,'images']
        getmostavaildf.at[i,'Thumbnail'] = getdict['picture_url']

    for i in getmostavaildf['_id'].index:
        if(getmostavaildf.loc[i,'Yearly (in days)'] == 0):
            getmostavaildf.drop(i,inplace=True)

    getmostavaildf.sort_values('Yearly (in days)',ascending=False,inplace=True)
    getnewdf = getmostavaildf[['Thumbnail','name','listing_url','property_type','price','Monthly (in days)','Bi-Monthly (in days)','Tri-Monthly (in days)','Yearly (in days)']]
    st.data_editor(
        getnewdf,
        column_config={
            'Thumbnail':st.column_config.ImageColumn(),
            'name':st.column_config.LinkColumn('Name',validate='listing_url'),
            'property_type':'Type',
            'price':st.column_config.NumberColumn('Price (in USD)',format='$ %d'),
            'Monthly (in days)':st.column_config.ProgressColumn(width='small',min_value=1,max_value=31,format='%d'),
            'Bi-Monthly (in days)':st.column_config.ProgressColumn(width='small',min_value=1,max_value=60,format='%d'),
            'Tri-Monthly (in days)':st.column_config.ProgressColumn(width='small',min_value=1,max_value=90,format='%d'),
            'Yearly (in days)':st.column_config.ProgressColumn(width='small',min_value=1,max_value=366,format='%d'),
        },
        column_order=['Thumbnail','name','property_type','price','Monthly (in days)','Bi-Monthly (in days)','Tri-Monthly (in days)','Yearly (in days)'],
        hide_index=True,
        height=1000,
        use_container_width=True
    )
st.markdown(' ')
st.markdown(' ')
st.subheader('Property Locations')
st.markdown(' ')
st.markdown(' ')
getlocdf = pd.DataFrame(data=[gettownlist,getcountrylist,getlatlist,getlonlist]).T
getproplocdf = pd.concat([getdf['name'],getlocdf],ignore_index=True,axis=1)
getproplocdf.columns=['Name','Town','Country','lat','lon']
st.map(getproplocdf,latitude='lat',longitude='lon',zoom=1,use_container_width=True)

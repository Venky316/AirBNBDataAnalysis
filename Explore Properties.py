import urllib.response
import streamlit as st
import json
import pandas as pd
from PIL import Image
from datetime import datetime
import time
import urllib.request

st.title('Explore Properties')
st.write('This page allows you to explore various properties that are available in the database and their features, prices & reviews.')

with open('sample_airbnb.json') as f:
    getfile = json.load(f)

getdf = pd.DataFrame(getfile)
getdf['_id'] = getdf['_id'].astype('int64')
getdf['minimum_nights'] = getdf['minimum_nights'].astype('int64')
getdf['maximum_nights'] = getdf['maximum_nights'].astype('int64')
getdf.fillna(0,inplace=True)

rowlist = []
rowlist.append('0 to 10')
for i in range(11,getdf.shape[0],10):
    if(i == 5551):
        rowlist.append('5551 to 5554')
        break
    else:
        getstr = str(i) + ' to ' + str(i + 9)
        rowlist.append(getstr)

disprows = st.selectbox('Display Rows',options=rowlist,index=None)
if(disprows):
    splitval = disprows.split(' ')
    filtdf = getdf.iloc[int(splitval[0]):int(splitval[2])+1,:]
    for i in filtdf.index:
        col1,col2,col3 = st.columns((1.6,0.2,0.2))
        with col1:
            concatstr = ':blue[<b><font size="6">' + filtdf.loc[i,'name'] + ' <b>] :love_hotel:'
            st.write(concatstr,unsafe_allow_html=True)
            concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font size = "4">' + filtdf.loc[i,'address']['street']
            st.write(concatstr,unsafe_allow_html=True)
            st.markdown(' ')
            st.markdown(' ')
            st.markdown(' ')
            st.write(filtdf.loc[i,'description'])
            col4,col5,col6 = st.columns((0.8,0.8,0.4))
            with col4:
                st.markdown(' ')
                st.markdown(' ')
                try:
                    urllib.request.urlretrieve(filtdf.loc[i,'images']['picture_url'],'propimg.jpg')
                    img = Image.open('propimg.jpg')
                    st.image(img)
                except:
                    img = Image.open('blank.jpg')
                    st.image(img)
                renovon = datetime.strptime(filtdf.loc[i,'last_scraped'],'%Y-%m-%d %H:%M:%S')
                getrenovon = datetime.strftime(renovon,'%d %B %Y')
                concatstr = '<font size = "3">Last Renovated On : ' + str(getrenovon)
                st.write(concatstr,unsafe_allow_html=True)
            with col5:
                st.markdown(' ')
                st.markdown(' ')
#       Description                
                st.write('<b><font size="6">&nbsp;&nbsp;&nbsp;&nbsp;:bookmark: Description</b>',unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Property Type : ' + filtdf.loc[i,'property_type']
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Room Type : ' + filtdf.loc[i,'room_type']
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bathrooms : ' + str(int(filtdf.loc[i,'bathrooms']))
                st.write(concatstr,unsafe_allow_html=True)
                st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bed Details : ',unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size="1">:black_circle:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size = "3">' + str(int(filtdf.loc[i,'bedrooms'])) + ' bedrooms'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size="1">:black_circle:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size = "3">' + str(int(filtdf.loc[i,'beds'])) + ' beds'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size="1">:black_circle:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size = "3">' + str(int(filtdf.loc[i,'accommodates'])) + ' people can be maximum accomodated'
                st.write(concatstr,unsafe_allow_html=True)                
            with col6:
                st.markdown(' ')
                st.markdown(' ')
#       Availability
                st.write('<b><font size="6">&nbsp;:bookmark: Availability</b>',unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size="1">:black_circle:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size = "3">Monthly : ' + str(filtdf.loc[i,['availability']][0]['availability_30']) + ' days'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size="1">:black_circle:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size = "3">Bi-Monthly : ' + str(filtdf.loc[i,['availability']][0]['availability_60']) + ' days'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size="1">:black_circle:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size = "3">Tri-Monthly : ' + str(filtdf.loc[i,['availability']][0]['availability_90']) + ' days'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size="1">:black_circle:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size = "3">Yearly : ' + str(filtdf.loc[i,['availability']][0]['availability_365']) + ' days'
                st.write(concatstr,unsafe_allow_html=True)

#       Amenities
        st.markdown(' ')
        st.write('<b><font size="6">:bookmark: Amenities</b>',unsafe_allow_html=True)
        with st.expander('Show Amenities'):
            getamen = filtdf.loc[i,'amenities']
            for j in getamen:
                concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;<font size="1">:black_circle:&nbsp;&nbsp;&nbsp;&nbsp;<font size = "3">' + j
                st.write(concatstr,unsafe_allow_html=True)
        try:
            st.markdown(' ')
            st.write(filtdf.loc[i,'access'])
        except:
            ''

#       Access & Transit            
        st.markdown(' ')
        st.write('<b><font size="6">:bookmark: Access & Transit</b>',unsafe_allow_html=True)
        getstr = filtdf.loc[i,'transit']
        if(getstr == ''):
            st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/A')
        else:
            concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + getstr
            st.write(concatstr,unsafe_allow_html=True)

#       Rules & Regulations

        st.markdown(' ')
        st.write('<b><font size="6">:bookmark: Rules & Regulations</b>',unsafe_allow_html=True)
        getstr = filtdf.loc[i,'house_rules']
        if(getstr == ''):
            st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/A')
        else:
            concatstr = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + getstr
            st.write(concatstr,unsafe_allow_html=True)

#       Contact Details

        st.markdown(' ')
        st.write('<b><font size="6">:bookmark: Contact Us</b>',unsafe_allow_html=True)
        st.markdown(' ')
        st.markdown(' ')
        col7,col8 = st.columns((0.5,1.5))
        with col7:
            try:
                urllib.request.urlretrieve(filtdf.loc[i,'images']['picture_url'],'propimg.jpg')
                img = Image.open('propimg.jpg')
                st.image(img)
            except:
                img = Image.open('blanksmall.jpg')
                st.image(img)
        with col8:
            concatstr = '<b><font size = "5">:adult: ' + filtdf.loc[i,'host']['host_name']
            st.write(concatstr,unsafe_allow_html=True)
            getstr = filtdf.loc[i,'host']['host_about']
            if(getstr == ''):               
                st.write(':clipboard: N/A')
            else:
                concatstr = ':clipboard: ' + getstr
                st.write(concatstr,unsafe_allow_html=True)
            getstr = filtdf.loc[i,'host']['host_location']
            if(getstr == ''):
                st.write(':pushpin: N/A')
            else:
                concatstr = ':pushpin: ' + getstr
                st.write(concatstr,unsafe_allow_html=True)
            try:
                getstr = filtdf.loc[i,'host']['host_response_time']
                if(getstr == ''):
                    st.write(':telephone_receiver: N/A')
                else:
                    concatstr = ':telephone_receiver: ' + getstr
                    st.write(concatstr,unsafe_allow_html=True)
                getstr = filtdf.loc[i,'host']['host_url']
                if(getstr == ''):
                    st.write(':globe_with_meridians: N/A')
                else:
                    concatstr = ':globe_with_meridians: ' + getstr
                    st.write(concatstr,unsafe_allow_html=True)
            except:
                st.write(':telephone_receiver: N/A')
#       Reviews

        st.markdown(' ')
        st.write('<b><font size="6">:bookmark: Reviews</b>',unsafe_allow_html=True)
        st.write('Total No. of Reviews : ',filtdf.loc[i,'number_of_reviews'])
        getfirrev = filtdf.loc[i,'first_review']
        if(getfirrev == 0):
            st.write('First Reviewed On : N/A')
        else:
            getfirrevdate = datetime.strptime(getfirrev,'%Y-%m-%d %H:%M:%S')
            firrevdate = datetime.strftime(getfirrevdate,'%d %B, %Y')
            st.write('First Reviewed On : ',firrevdate)
        getlasrev = filtdf.loc[i,'last_review']
        if(getfirrev == 0):
            st.write('Last Reviewed On : N/A')
        else:
            getlasrevdate = datetime.strptime(getlasrev,'%Y-%m-%d %H:%M:%S')
            lasrevdate = datetime.strftime(getlasrevdate,'%d %B, %Y')
            st.write('Last Reviewed On : ',lasrevdate)
        with st.expander('See Reviews'):
            getrevlist = filtdf.loc[i,'reviews']
            if(len(getrevlist)== 0):
                st.write('Sorry...!! No reviews available at the moment.')
            else:
                for j in getrevlist:
                    getidname = j['reviewer_name']
                    getid = j['reviewer_id']
                    concatstr = '<b>:lower_left_ballpoint_pen: ' + getidname + ' ( id : ' + str(getid) + ' )'
                    st.write(concatstr,unsafe_allow_html=True)
                    st.write(j['comments'])
                    getcommdate = datetime.strptime(j['date'],'%Y-%m-%d %H:%M:%S')
                    commdate = datetime.strftime(getcommdate,'%d %B, %Y at %H:%M %p')
                    concatstr = '<font size="2">:date: ' + commdate
                    st.write(concatstr,unsafe_allow_html=True)
                    st.write('_____________________________________________________________________')
        st.write('_____________________________________________________________________')

        with col2:
            getrentsum = int(filtdf.loc[i,'price'] + filtdf.loc[i,'security_deposit'] + filtdf.loc[i,'cleaning_fee'] + filtdf.loc[i,'extra_people'] + filtdf.loc[i,'guests_included'])
            concatstr = '$ ' + str(getrentsum) + ' USD'
            with st.popover(concatstr):
                st.write('<b>Price Breakup',unsafe_allow_html=True)
                concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Room Rent : <b>$ ' + str(int(filtdf.loc[i,'price'])) + '</b>'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Security Deposit : <b>$ ' + str(int(filtdf.loc[i,'security_deposit'] )) + '</b>'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Cleaning Fee : <b>$ ' + str(int(filtdf.loc[i,'cleaning_fee'])) + '</b>'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Extra People : <b>$ ' + str(int(filtdf.loc[i,'extra_people'])) + '</b>'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Guests Included : <b>$ ' + str(int(filtdf.loc[i,'guests_included'])) + '</b>'
                st.write(concatstr,unsafe_allow_html=True)
        with col3:
            try:
                getrat = filtdf.loc[i,'review_scores']['review_scores_rating']
                getrevrat = int(getrat / 10)
                if(getrevrat >= 5):
                    concatstr = ':smile: ' + str(getrevrat)               
                else:
                    concatstr = ':disappointed: ' + str(getrevrat)
                with st.popover(concatstr):
                    concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Accuracy : <b> ' + str(int(filtdf.loc[i,'review_scores']['review_scores_accuracy'])) + '</b>'
                    st.write(concatstr,unsafe_allow_html=True)
                    concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Cleanliness : <b> ' + str(int(filtdf.loc[i,'review_scores']['review_scores_cleanliness'])) + '</b>'
                    st.write(concatstr,unsafe_allow_html=True)
                    concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Check-In : <b> ' + str(int(filtdf.loc[i,'review_scores']['review_scores_checkin'])) + '</b>'
                    st.write(concatstr,unsafe_allow_html=True)
                    concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Communication: <b> ' + str(int(filtdf.loc[i,'review_scores']['review_scores_communication'])) + '</b>'
                    st.write(concatstr,unsafe_allow_html=True)
                    concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Location : <b> ' + str(int(filtdf.loc[i,'review_scores']['review_scores_location'])) + '</b>'
                    st.write(concatstr,unsafe_allow_html=True)    
                    concatstr = '<font size = "1">:black_circle:' + '<font size = "3">&nbsp;&nbsp;&nbsp;&nbsp;Value : <b> ' + str(int(filtdf.loc[i,'review_scores']['review_scores_value'])) + '</b>'
                    st.write(concatstr,unsafe_allow_html=True)
            except:
                with st.popover('N/A'):
                    st.write('Sorry. Review scores not available')

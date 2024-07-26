import streamlit as st
import json
import pandas as pd
from PIL import Image
import urllib.request
from datetime import datetime
import plotly.express as px

st.title('Explore Properties')
st.write('This page allows you to explore various properties that are available in the database and their features, prices & reviews.')

with open('sample_airbnb.json','r') as f:
    getfile = json.load(f)

getdf = pd.DataFrame(getfile)
getdf['_id'] = getdf['_id'].astype('int64')
getdf['minimum_nights'] = getdf['minimum_nights'].astype('int64')
getdf['maximum_nights'] = getdf['maximum_nights'].astype('int64')

getdf.fillna(0,inplace=True)

getdisplaylist = []
concatstr = str(0) + ' to ' + str(10)
getdisplaylist.append(concatstr)
j = 11
for i in range(11,5555,10):
    if(i == 5550):
        pass
    else:
        concatstr = str(j) + ' to ' + str(j+9)
        getdisplaylist.append(concatstr)
        j = i + 10
    
getdisprowsel = st.selectbox(label='Display Rows',options=getdisplaylist,index=None)

if(getdisprowsel):
    splitdisprowsel = getdisprowsel.split(' ')
    filtdf = getdf.iloc[int(splitdisprowsel[0]):int(splitdisprowsel[2])+1,:]
    for i in filtdf['_id'].index:
        col4,col5,col6 = st.columns((1.5,0.25,0.25))
        with col4:
            writename = ':blue[' + getdf.iloc[i,2] + '] ' + ':love_hotel:'
            st.subheader(writename)
            getsuburb = filtdf.loc[i,'address']['suburb']
            getmarket = filtdf.loc[i,'address']['market']
            getcountry = filtdf.loc[i,'address']['country']
            concatstr =  getsuburb + ', ' + getmarket + ', ' + getcountry
            st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>',concatstr,'</b>',unsafe_allow_html=True)
            st.markdown(' ')        
            st.write(getdf.iloc[i,4])
            st.markdown(' ')
            st.write(getdf.iloc[i,5])
            st.markdown(' ')

        with col5:
            overallprice = int(filtdf.loc[i,'price']) + int(filtdf.loc[i,'security_deposit']) + int(filtdf.loc[i,'cleaning_fee']) + int(filtdf.loc[i,'extra_people']) + int(filtdf.loc[i,'guests_included'])
            concatstr = '$ ' + str(overallprice) + ' USD'
            with st.popover(concatstr):
                st.write('<b>Price Breakup</b>',unsafe_allow_html=True)
                concatstr = '<ul><li> Room Rent : <b>$ ' + str(int(filtdf.loc[i,'price'])) + '</b></ul></li>'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '<ul><li> Security Deposit : <b>$ ' + str(int(filtdf.loc[i,'security_deposit'])) + '</b></ul></li>'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '<ul><li> Cleaning Fee : <b>$ ' + str(int(filtdf.loc[i,'cleaning_fee'])) + '</b></ul></li>'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '<ul><li> Extra People : <b>$ ' + str(int(filtdf.loc[i,'extra_people'])) + '</b></ul></li>'
                st.write(concatstr,unsafe_allow_html=True)
                concatstr = '<ul><li> Guests Included : <b>$ ' + str(int(filtdf.loc[i,'guests_included'])) + '</b></ul></li>'
                st.write(concatstr,unsafe_allow_html=True)

        with col6:
            reviews = filtdf.loc[i,'review_scores']
            if(reviews == {}):
                with st.popover('N/A'):
                    st.write('Sorry. Review scores not available')
            else: 
                getoverallrating = int(reviews['review_scores_rating']) / 10
                if(getoverallrating >= 5):
                    overallscore = ':smile:' + '  ' + str(getoverallrating)
                else:
                    overallscore = ':disappointed:' + '  ' + str(getoverallrating)

                with st.popover(overallscore):
                    concatstr = '<ul><li> Accuracy : <b>' + str(reviews['review_scores_accuracy']) + '</b></ul></li>'
                    st.write(concatstr,unsafe_allow_html=True)
                    concatstr = '<ul><li> Cleanliness : <b>' + str(reviews['review_scores_cleanliness']) + '</b></ul></li>'
                    st.write(concatstr,unsafe_allow_html=True) 
                    concatstr = '<ul><li> Check-In : <b>' + str(reviews['review_scores_checkin']) + '</b></ul></li>'
                    st.write(concatstr,unsafe_allow_html=True)  
                    concatstr = '<ul><li> Communication : <b>' + str(reviews['review_scores_communication']) + '</b></ul></li>'
                    st.write(concatstr,unsafe_allow_html=True)      
                    concatstr = '<ul><li> Location : <b>' + str(reviews['review_scores_location']) + '</b></ul></li>'
                    st.write(concatstr,unsafe_allow_html=True)
                    concatstr = '<ul><li> Value : <b>' + str(reviews['review_scores_value']) + '</b></ul></li>'
                    st.write(concatstr,unsafe_allow_html=True)        

        col1,col2,col3 = st.columns((1,1,1))
        try:
            with col1:
                urllib.request.urlretrieve(getdf.loc[i,'images']['picture_url'],'getimage.png')
                img = Image.open('getimage.png')
                st.image(img)

                lastren = str(filtdf.loc[i,'last_scraped'])
                splitren = lastren.split(' ')
                splitlastren = splitren[0].split('-')
                createdate = datetime(int(splitlastren[0]),int(splitlastren[1]),int(splitlastren[2]))
                getlastren = createdate.strftime('%d %B, %Y')
                concatstr = 'Last Renovated On : ' + getlastren
                st.write(concatstr)
        except:
            with col1:
                img = Image.open('blank.jpg')
                st.image(img)
        with col2:
            st.subheader(':bookmark: Description')
            st.write('Property Type : ',getdf.iloc[i,13])
            concatstr = 'Bathrooms : ' + str(int(getdf.loc[i,'bathrooms'])) + ' Nos.'
            st.write(concatstr)        
            st.write('Bed Details : ')
            concatstr = filtdf.loc[i,'bed_type']
            concatstr = '<ul><li>' + str(int(filtdf.loc[i,'bedrooms'])) + ' bedrooms</li></ul>'
            st.write(concatstr,unsafe_allow_html=True)
            concatstr = '<ul><li>' + str(int(filtdf.loc[i,'beds'])) + ' beds</li></ul>'
            st.write(concatstr,unsafe_allow_html=True)
            concatstr = '<ul><li>' + str(int(filtdf.loc[i,'accommodates'])) + ' peoples can be maximum accomodated</ul></li>'
            st.write(concatstr,unsafe_allow_html=True)

        with col3:
            st.subheader(':bookmark: Availability')
            avail = filtdf.loc[i,'availability']
            concatstr = '<ul><li> Monthly : ' + str(avail['availability_30']) + ' days</ul></li>'
            st.write(concatstr,unsafe_allow_html=True)
            concatstr = '<ul><li> Bi-Monthly : ' + str(avail['availability_60']) + ' days</ul></li>'
            st.write(concatstr,unsafe_allow_html=True)
            concatstr = '<ul><li> Tri-Monthly : ' + str(avail['availability_90']) + ' days</ul></li>'
            st.write(concatstr,unsafe_allow_html=True)    
            concatstr = '<ul><li> Yearly : ' + str(avail['availability_365']) + ' days</ul></li>'
            st.write(concatstr,unsafe_allow_html=True)      

        st.subheader(':bookmark: Amenities')
        getexpand = st.expander('Show Amenities')
        with getexpand:
            getamenlist = filtdf.loc[i,'amenities']
            for j in getamenlist:
                concatstr = '<ul><li>' + str(j) + '</li></ul>'
                st.write(concatstr,unsafe_allow_html=True)
    
        st.markdown(' ')
        st.write(filtdf.loc[i,'access'])
        st.markdown(' ')
        st.subheader(':bookmark: Access & Transit')
        getaccess = filtdf.loc[i,'transit']
        if(getaccess == ''):
            st.write('N/A')
        else:
            st.write(getaccess)
            
        st.markdown(' ')    
        st.subheader(':bookmark: Rules & Regulations')
        getrules = filtdf.loc[i,'house_rules']
        if(getrules == ''):
            st.write('N/A')
        else:
            st.write(getrules)
    
        st.markdown(' ')
        st.subheader(':bookmark: Contact Us')

        st.markdown(' ')
        st.markdown(' ')
        st.markdown(' ')
        col9,col10 = st.columns((0.4,1.6))
        with col9:
            gethostpic = filtdf.loc[i,'host']['host_picture_url']
            try:
                urllib.request.urlretrieve(gethostpic,'hostpic.jpg')
                img = Image.open('hostpic.jpg')
            except:
                img = Image.open('blanksmall.jpg')
            st.image(img)
        with col10:
            st.write(':male-office-worker:','<b><font size=5>',filtdf.loc[i,'host']['host_name'],'</font></b>',unsafe_allow_html=True)
            gethostabout = filtdf.loc[i,'host']['host_about']
            if(gethostabout == ''):
                st.write(':clipboard:','No details about the owner')
            else:
                st.write(':clipboard:',gethostabout)
            st.write(':pushpin:',filtdf.loc[i,'host']['host_location'])
            try:
                gethostresponse = filtdf.loc[i,'host']['host_response_time']
                st.write(':telephone_receiver:',gethostresponse)
            except:
                st.write(':telephone_receiver:','N/A')
            st.write(':globe_with_meridians:',filtdf.loc[i,'host']['host_url'])

        firreview = str(filtdf.loc[i,'first_review'])
        lastreview = str(filtdf.loc[i,'last_review'])
        if(firreview == '0'):
            getstr = 'First Reviewed On : N/A'
        else:
            createdate = datetime.strptime(firreview,'%Y-%m-%d %H:%M:%S')
            getfirreviewdate = createdate.strftime('%d %b, %Y')
            getfirreviewtime = createdate.strftime('%H:%M %p')
            getfirrevstr = 'First Reviewed On : ' + str(getfirreviewdate) + ' at ' + str(getfirreviewtime)

        if(lastreview == '0'):
            getstr = 'Last Reviewed On : N/A'
        else:
            createdate = datetime.strptime(lastreview,'%Y-%m-%d %H:%M:%S')
            getlasreviewdate = createdate.strftime('%d %b, %Y')
            getlasreviewtime = createdate.strftime('%H:%M %p')
            getlasrevstr = 'Last Reviewed On : ' + str(getlasreviewdate) + ' at ' + str(getlasreviewtime)  

        st.markdown(' ')
        st.subheader(':bookmark: Reviews')
        st.write('Total No. of Reviews : ',int(filtdf.loc[i,'number_of_reviews']))
        try:
            st.write(getfirrevstr)
            st.write(getlasrevstr)
        except:
            st.write('First Reviewed On : N/A')
            st.write('Last Reviewed On : N/A')

        getexpand = st.expander('See Reviews')
        with getexpand:
            if(int(filtdf.loc[i,'number_of_reviews']) == 0):
                st.write('No Reviews at the moment')
            else:    
                getreviewlist = filtdf.loc[i,'reviews']
                for j in getreviewlist:
                    getdict = j
                    st.write(':lower_left_ballpoint_pen:','<b><font size=3>',getdict['reviewer_name'],' ( id : ',getdict['reviewer_id'],')','</font></b>',unsafe_allow_html=True)
                    st.write(getdict['comments'])
                    getcommentdate = datetime.strptime(getdict['date'],'%Y-%m-%d %H:%M:%S')
                    commentdate = getcommentdate.strftime('%d %b, %Y')
                    commenttime = getcommentdate.strftime('%H:%M %p')
                    st.write(':date:','<font size=2>',str(commentdate),' ',str(commenttime),'</font>',unsafe_allow_html=True)
                    st.write('________________________________________________________')
        st.write('<b>','_________________________________________________________________________________________________________________________________________________________________________________','</b>',unsafe_allow_html=True)
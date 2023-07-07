import streamlit as st
from PIL import Image

images_list = ['yt.png','api.png','phonephe.png','twt.png','bulk.png']

def project_selection(selected_pr):
    if selected_pr == "API TO RDS USING LAMBDA WITH SLACK ERROR MONITORING":
        image = Image.open(f"images/{images_list[1]}")
        resized_image = image.resize((450, 390))  # Adjust the width and height as desired
        pr1, pr2 = st.columns([5,3.5])
        with pr2:
            st.markdown('<br>', unsafe_allow_html=True)
            st.image(resized_image)
            
        with pr1:
            st.write("""#### OverView
- Using _**AWS Lambda**_ Api is fetched from a link, processed and load into _**AWS RDS**_ with **15 seconds** Interval\n
- Two Lambda functions are used in these Pipeline where **First lambda** will be invoked by **Aws Step-Function** which is invoked by **Cloudwatch / EventBridge Rules**. For Every _One minute_ until the Rule gets disabled.\n
- **Second Lambda** Function is used to fetch Api and Loaded into AWS RDS.
- **Aws Step-Function** is Working Based _ASL(Amazon State Language)_ which is based on _Json_ file Structure\n
- If any _error or Database connction_ problem occurs notification is sent to **slack channel** using _slack_sdk_\n
- All internal Connections between AWS services are based on _**IAM Role and Policies**_.
- For more details Visit [Github](https://github.com/pnraj/Projects/tree/master/AWS%3A%20Bulk%20%26%20Near%20Real-Time%20Pipelines/API%20TO%20RDS%20USING%20LAMBDA%20WITH%20SLACK%20ERROR%20MONITORING)
""")

    elif selected_pr == "SPARK-ENABLED EXTRACTION AND LOADING INTO AWS RDS":
        pr1, pr2 = st.columns([5,3.5])
        image = Image.open(f"images/{images_list[4]}")
        resized_image = image.resize((350, 350))  # Adjust the width and height as desired
        
        with pr2:
            st.image(resized_image)
            
        with pr1:
        
            st.write("""#### OverView
- There are **Two Part** in these Project.\n
- **Part1** is Getting Data from **SEC.gov**(**Zip** format) contains more than _8.5 lakh_ **Json files** around **6gb** after _uncompressing_.
- By Using _**Apache Spark(PySpark)**_ and _DataBricks_, Json files are converted into **Pyspark DataFrames** with _Each_ json File representing _single row_ in DataFrame.The _DataFrame_ is later converted into _Json file_ and uploaded into **AWS S3**.\n
- **Part2** is Getting Data from AWS S3, Do the Needed Transformation and upload into _**AWS RDS-Mysql Instance**_\n
- The Data From S3 is Converted into _PySpark DataFrame_ and Isolate needed Columns that needed to uplaoded into RDS\n
- Important Function Used for Transformation are _**join, posexplode_outer, udf, concat, to_date, struct and Row.**_\n
- For more details Visit [Github](https://github.com/pnraj/Projects/tree/master/AWS%3A%20Bulk%20%26%20Near%20Real-Time%20Pipelines/Spark-Enabled%20Extraction%20and%20Loading%20Into%20AWS%20RDS)
""")
    
    elif selected_pr == "YouTube Data Harvesting and Warehousing":
        pr1, pr2 = st.columns([5,3.5])
        image = Image.open(f"images/{images_list[0]}")
        resized_image = image.resize((350, 350))  # Adjust the width and height as desired
        
        with pr2:
            st.image(resized_image)
            
        with pr1:
        
            st.write("""#### OverView
- Ability to input a **YouTube channel ID** and retrieve all the relevant data using **Google API**.\n
- Option to store the data in a **MongoDB database** as a _Data Lake_.\n
- Ability to collect data for up to 10 different YouTube channels and store them in the data lake based upon user Requirment.\n
- Option to select a _channel name_ and migrate its data from the data lake to a **Mysql(SQL) Database** as tables.\n
- Ability to search and retrieve data from the SQL database using different search options, including joining tables to get channel details.\n
- For more details Visit [Github](https://github.com/pnraj/Projects/tree/master/YouTube_Data_Harvesting_and_Warehousing)
""")

    elif selected_pr == "PhonePe Pulse Data Analysis 2018-2022":
        pr1, pr2 = st.columns([5,3.5])
        image = Image.open(f"images/{images_list[2]}")
        resized_image = image.resize((350, 350))  # Adjust the width and height as desired
        
        with pr2:
            st.image(resized_image)
            
        with pr1:
        
            st.write("""#### OverView
- Getting the _**PhonePe Payment App-Data**_ in **Json format** from **Github** repo \n
- The _Json files_ are separated for every _**3 Month / 1 Quarter**_ of years from **2018-2022** for every _states and districts_ in **India**.\n
- Using _Python_ **os module**, Pipeline is Built to **Iterate** to each folder and get data from _json file_ and convert into _**pandas DataFrame**_.\n
- Json Files Contains Details about _**Amount of Transactions**_ and _**Transaction Location**_ where Users Do that Transaction.\n
- Using The DataFrame, **Visualization** are made using **Plotly and Streamlit** on _Geo, Bar, line, Pie, Area_ chart are included.\n
- For more details Visit [Github](https://github.com/pnraj/Projects/tree/master/Phonephe_Pulse)
""")

    elif selected_pr == "Twitter Scraping":
        pr1, pr2 = st.columns([5,3.5])
        image = Image.open(f"images/{images_list[3]}")
        resized_image = image.resize((350, 350))  # Adjust the width and height as desired
        
        with pr2:
            st.image(resized_image)
            
        with pr1:
        
            st.write("""#### OverView
- Based on User needs **Twitter** _Tweets_ are **Extracted and Uploaded** into **Mongodb** using UI based upon **Streamlite** based app\n
- Users have to enter **Tweets topic or hashtag**, **Starting Date**, **Ending Date**, **Total Number of Tweets** needed to extracted in app and \n
- App will _fetch_ the data by using **Snscrape** and convert the data into **Pandas DataFrame** and displayed as _Tabular Format_.\n
- After Checking the data users can have options to download the data as _**json**_, _**csv**_ or can be _**uploaded into Mongodb**_.\n
- For more details Visit [Github](https://github.com/pnraj/Twitter_scraping)
""")
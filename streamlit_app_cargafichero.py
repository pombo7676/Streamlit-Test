import pandas as pd 
# import streamlit as st 
import os 
import streamlit as st 

#""" Data Source   """
#web location for csv file, 'df.csv'
data_src = r'https://raw.githubusercontent.com/clueple/free_resources/master/df.csv'
# data_src = r'https://github.com/clueple/free_resources/blob/master/df.csv'

#web location for csv file, 'dfc.csv'
data_src1 = r'https://raw.githubusercontent.com/clueple/free_resources/master/dfc.csv'
# data_src1 = r'https://github.com/clueple/free_resources/blob/master/dfc.csv'


#""" test folder  """
# file_dir = os.listdir(r'd:/Downloads')
file_dir = r'd:/Downloads'
file_name = 'df1.csv'

filepath = f"{file_dir}/{file_name}"


#""" App Interface  """

def main():
	st.header('Original Data')
	df1 = pd.read_csv(filepath)
	data = st.dataframe(df1)

	with st.sidebar.form(key='df1', clear_on_submit=True):
		add_col1 = st.text_input('col1')
		add_col2 = st.number_input('col2', min_value=0.00)
		add_col3 = st.number_input('col3', min_value=0.00)
		submit = st.form_submit_button('Submit')
		if submit:
			new_data = {'col1': add_col1, 'col2': add_col2, 'col3': add_col3}

			df1 = df1.append(new_data, ignore_index=True)
			df1.to_csv(filepath, index=False)

	st.header('After Update')
	st.dataframe(df1)


if __name__ == '__main__':
	main()
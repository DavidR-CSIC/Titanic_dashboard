
#Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")

#Page Config
st.set_page_config(page_title="Titanic EDA", layout="wide")

#Data Loading function

@st.cache_data
def load_data(file_path=None, uploaded_file=None):
    """Load data from a CSV file or uploaded file with cache optimization"""
    try:
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        elif file_path:
            df = pd.read_csv(file_path)
            st.success("Data loaded successfully from file path!")
        else:
            st.warning("Please provide a file path or upload a CSV file.")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()
    
#-------------CREATE FILTERS---------------------------#
def create_filters(df):
    """Create sidebar filters for the DataFrame."""
    st.sidebar.header("Data Filters")
    filters = {}

    # Sex Filter
    if 'Sex' in df.columns:
        sex_options = ['All'] + sorted(df['Sex'].unique().tolist())
        filters['Sex'] = st.sidebar.selectbox('Sex', sex_options)

    # Pclass Filter
    if 'Pclass' in df.columns:
        pclass_options = ['All'] + sorted(df['Pclass'].unique().tolist())
        filters['Pclass'] = st.sidebar.selectbox('Pclass', pclass_options)

    # Embarked Filter
    if 'Embarked' in df.columns:
        embarked_options = ['All'] + sorted(df['Embarked'].dropna().unique().tolist())
        filters['Embarked'] = st.sidebar.selectbox('Embarked', embarked_options)

    #survival filter
    if 'Survived' in df.columns:
        supervived_options = st.sidebar.multiselect(
            'Survived', 
            options = [0, 1],
            default = [0, 1],
            format_func = lambda x: 'No' if x == 0 else 'Yes'
        )
        filters['Survived'] = supervived_options

    # Age Filter
    if 'Age' in df.columns:
        age_min, age_max = float(df['Age'].min()), float(df['Age'].max())
        filters['age_range'] = st.sidebar.slider(
            'Age range', 
            min_value=age_min,
            max_value=age_max,
            value=(age_min, age_max),
            step=1.0
        )

    # Fare Filter
    if 'Fare' in df.columns:
        fare_min, fare_max = float(df['Fare'].min()), float(df['Fare'].max())
        filters['fare_range'] = st.sidebar.slider(
            'Fare range', 
            min_value=fare_min,
            max_value=fare_max,
            value=(fare_min, fare_max),
            step=1.0
        )
    return filters
    
##---------------------------------APPLY FILTERS------------------#


def apply_filters(df, filters):
    """Apply the selected filters to the DataFrame."""
    filtered_df = df.copy()


    # Apply Sex filter
    if filters.get('Sex') != 'All':
        filtered_df = filtered_df[filtered_df['Sex'] == filters['Sex']]


    # Apply Pclass filter
    class_col = 'Pclass' if 'Pclass' in df.columns else 'classes'
    if filters.get('classes') and filters['classes'] != 'All' and class_col in df.columns:
        filtered_df = filtered_df[filtered_df[class_col] == filters['classes']]


    # Apply Embarked filter
    if filters.get('Embarked') != 'All':
        filtered_df = filtered_df[filtered_df['Embarked'] == filters['Embarked']]


    # Apply Survived filter
    if 'Survived' in filters and filters['Survived']:
        filtered_df = filtered_df[filtered_df['Survived'].isin(filters['Survived'])]


    # Apply Age range filter
    if 'age_range' in filters:
        age_min, age_max = filters['age_range']
        filtered_df = filtered_df[(filtered_df['Age'] >= age_min) & (filtered_df['Age'] <= age_max)]


    # Apply Fare range filter
    if 'fare_range' in filters:
        fare_min, fare_max = filters['fare_range']
        filtered_df = filtered_df[(filtered_df['Fare'] >= fare_min) & (filtered_df['Fare'] <= fare_max)]
    return filtered_df


#-----------Graphs-----------#

def create_eda_plots(df):
    """Create and display EDA plots."""
    plots = {}

    try:
        # 1 age distribution
        if 'Age' in df.columns:
            plots['age_hist'] = px.histogram(
                df,
                x = 'Age',
                nbins = 30,
                title = 'Age Distribution',
                labels = {'Age': 'Age', 'count': 'Conteo'})
            plots['age_hist'].update_layout(showlegend=False)
    except Exception as e:
        st.error(f"Error creating Age Distribution plot: {e}")


    try:
        # 2 sex survival count
        if 'Survived' in df.columns and 'Sex' in df.columns:
            survival_by_sex = df.groupby('Sex')['Survived'].size().reset_index(name='count')
            plots['sex_survival_by_sex'] = px.bar(
                survival_by_sex,
                x = 'Sex',
                y = 'count',
                color = 'Survived',
                title = 'Sex vs Survival Count',
                labels = {'Sex': 'Sex', 'count': 'Conteo'},
                color_discrete_map = {0: 'red', 1: 'blue'}
            )
            plots['sex_survival_by_sex'].update_layout(showlegend=False)
    except Exception as e:
        st.error(f"Error creating Sex vs Survival Count plot: {e}")

    try:
        # 3 countplot survived by pclass
        if 'Survived' in df.columns and 'Pclass' in df.columns:
            survival_by_pclass = df.groupby('Pclass')['Survived'].size().reset_index(name='count')
            plots['pclass_survival_by_pclass'] = px.bar(
                survival_by_pclass,
                x='Pclass',
                y='count',
                color='Survived',
                title='Pclass vs Survival Count',
                labels={'Pclass': 'Pclass', 'count': 'Conteo'},
                color_discrete_map={0: 'red', 1: 'blue'}
            )
            plots['pclass_survival_by_pclass'].update_layout(showlegend=False)
    except Exception as e:
        st.error(f"Error creating Pclass vs Survival Count plot: {e}")
        #4 boxplot fare vs pclass


    try:
        if 'Fare' in df.columns and 'Pclass' in df.columns:
            plots['fare_boxplot'] = px.box(
                df,
                x='Pclass',
                y='Fare',
                title='Fare Distribution by Pclass',
                labels={'Pclass': 'Pclass', 'Fare': 'Fare'}
            )
            plots['fare_boxplot'].update_layout(showlegend=False)
    except Exception as e:
        st.error(f"Error creating Fare Distribution by Pclass plot: {e}")


    try:
        # 5 countplot survived by embarked
        if 'Survived' in df.columns and 'Embarked' in df.columns:
            survival_by_embarked = df.groupby('Embarked')['Survived'].size().reset_index(name='count')
            plots['embarked_survival_by_embarked'] = px.bar(
                survival_by_embarked,
                x='Embarked',
                y='count',
                color='Survived',
                title='Embarked vs Survival Count',
                labels={'Embarked': 'Embarked', 'count': 'Conteo'},
                color_discrete_map={0: 'red', 1: 'blue'}
            )
            plots['embarked_survival_by_embarked'].update_layout(showlegend=False)
    except Exception as e:
        st.error(f"Error creating Embarked vs Survival Count plot: {e}")
        

    try:
        # 6 correlation heatmap
        numeric_df = df.select_dtypes(include=[np.number])
        if len(numeric_df.columns) > 1:
            correlation_matrix = numeric_df.corr()
            plots['correlation_heatmap'] = px.imshow(
                correlation_matrix,
                text_auto=True,
                title='Correlation Heatmap',
                labels={'color': 'Correlation'},
                color_continuous_scale='RdBu_r',
            )
            plots['correlation_heatmap'].update_layout(showlegend=False)
    except Exception as e:
        st.error(f"Error creating Correlation Heatmap plot: {e}")
    return plots


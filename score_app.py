import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image

def calculate_avg(scores):
    return sum(scores) / len(scores)

def percentage_distribution(scores):
    bins = {'80-100': 0, '60-79': 0, '<60': 0}
    for score in scores:
        if score >= 80.0:
            bins['80-100'] += 1
        if score >= 60.0:
            bins['60-79'] += 1
        else:
            bins['<60'] += 1
    return bins

def main():
    st.title("Student Score Analyzer App")
    upload_file = st.file_uploader("Upload CSV file", type=["xlsx"])

    if upload_file:
        # read file:
        df = pd.read_excel(upload_file)

        # columns = df.columns
        # st.write(columns)

        # preprocessing:
        scores = df["Score"].astype(float).tolist()

        # average
        average_score = calculate_avg(scores)
        st.write(average_score)

        # distribution
        dist = percentage_distribution(scores)
        st.write(dist)
        # st.pie_chart(dist)
        labels = list(dist.keys())
        values = list(dist.values())

        # chart
        fig, ax = plt.subplots(figsize=(2,2))
        ax.pie(
            values,
            labels = labels,
            # autopct = '%1.1f%%',
            # textprops = {'fontsize': 5}
        )

        plt.tight_layout(pad=0.1)

        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi = 500)

        img = Image.open(buf)
        st.write("Score Distribution")
        st.image(img)

if __name__ == "__main__":
    main()

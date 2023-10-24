# pip install nltk
# pip install textblob
# pip install newspaper3k


import tkinter as tk
from textblob import TextBlob


def analyze_content():
    user_input = input_entry.get()
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    summary = [str(sentence) for sentence in blob.sentences[:3]]  # Convert sentences to strings

    if sentiment > 0.1:
        sentiment_label = "Positive"
        output_label.config(fg="green")
    elif sentiment < -0.1:
        sentiment_label = "Negative"
        output_label.config(fg="red")
    else:
        sentiment_label = "Neutral"
        output_label.config(fg="black")

    output_label.config(text="Summary:\n" + "\n".join(summary) + "\n\nSentiment: " + sentiment_label)


root = tk.Tk()
root.title("Content Analysis")

# Configure window size
root.geometry("400x300")

# Create custom fonts
title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 14)

# Create an input entry widget
input_label = tk.Label(root, text="Enter a paragraph:", font=label_font)
input_label.pack()
input_entry = tk.Entry(root, width=40, font=label_font)
input_entry.pack()

# Create an "Analyze" button
analyze_button = tk.Button(root, text="Analyze", command=analyze_content, font=button_font, bg="blue", fg="white")
analyze_button.pack()

# Create an output label to display the summary and sentiment
output_label = tk.Label(root, text="", font=label_font)
output_label.pack()

# Start the main event loop
root.mainloop()
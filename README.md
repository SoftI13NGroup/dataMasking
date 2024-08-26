# dataMasking

A project demonstrating methods for masking sensitive data in conversations with a chatbot assistant.

## DEMO

The demonstration showcases how the application identifies and masks sensitive data, using a pre-trained BERT-NER model to locate and classify such data. The `faker` library is then used to replace this data with fake information. The demo specifically illustrates how the app handles certain classes of sensitive data, such as names, locations, and organizations.

## Local Run for Demo

To run the demo locally:

1. **Install the necessary dependencies**:
    ```bash
    pip install -r requirements.txt
    pip install -e .
    ```

2. **Navigate to the demo directory**:
    ```bash
    cd demo
    ```

3. **Run the application**:
    ```bash
    python3 app.py
    ```

4. **Open `index.html` in your browser**:
   - The sensitive data found by the application will be highlighted in red.


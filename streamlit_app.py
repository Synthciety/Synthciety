import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="Quirky Website", layout="centered")

# Page Header
st.title("Welcome to the Quirky Website")
st.write("Explore **Mini-Games**, the latest **News**, and our interactive **Forum**!")

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["Mini Games", "News Feed", "Forum"])

# Tab 1: Mini Games
with tab1:
    st.header("Mini Games")
    st.write("Play fun games below:")

    # Tic-Tac-Toe Example (Simple Implementation)
    st.write("### Tic-Tac-Toe")
    if "board" not in st.session_state:
        st.session_state.board = [""] * 9
        st.session_state.current_player = "X"

    # Display Tic-Tac-Toe Board
    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            idx = 3 * i + j
            if cols[j].button(st.session_state.board[idx] or " ", key=f"cell-{idx}"):
                if not st.session_state.board[idx]:
                    st.session_state.board[idx] = st.session_state.current_player
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

    # Reset Button
    if st.button("Reset Game"):
        st.session_state.board = [""] * 9
        st.session_state.current_player = "X"

# Tab 2: News Feed
with tab2:
    st.header("News Feed")
    st.write("Latest news from around the world:")

    # Fetch news using NewsAPI
    API_KEY = "YOUR_API_KEY"  # Replace with your NewsAPI key
    NEWS_API_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    try:
        response = requests.get(NEWS_API_URL)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles[:5]:  # Display top 5 articles
                st.subheader(article["title"])
                st.write(article["description"] or "No description available.")
                st.markdown(f"[Read more...]({article['url']})")
        else:
            st.error("Failed to fetch news. Check your API key.")
    except Exception as e:
        st.error(f"Error fetching news: {e}")

# Tab 3: Forum
with tab3:
    st.header("Forum")
    st.write("Chat with other visitors:")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])

    # User input for new message
    if user_input := st.chat_input("Type your message here..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        # Example bot response
        bot_response = "Thanks for your message!"
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.chat_message("assistant").write(bot_response)

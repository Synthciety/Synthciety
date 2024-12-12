<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quirky Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #4CAF50;
            color: white;
            padding: 1em 0;
            text-align: center;
        }

        nav a {
            color: white;
            margin: 0 1em;
            text-decoration: none;
        }

        main {
            padding: 2em;
        }

        section {
            margin-bottom: 2em;
        }

        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1em 0;
        }

        .news-item {
            border: 1px solid #ddd;
            padding: 1em;
            margin-bottom: 1em;
            border-radius: 5px;
        }

        .news-item h3 {
            margin: 0 0 0.5em;
        }

        .news-item a {
            color: #4CAF50;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to the Quirky Website</h1>
        <nav>
            <a href="#games">Mini Games</a>
            <a href="#news">News Feed</a>
            <a href="#forum">Forum</a>
        </nav>
    </header>
    <main>
        <section id="games">
            <h2>Mini Games</h2>
            <div id="game-container">
                <!-- Games will load here -->
            </div>
        </section>
        <section id="news">
            <h2>News Feed</h2>
            <div id="news-container">
                <!-- News articles will load here -->
            </div>
        </section>
        <section id="forum">
            <h2>Forum</h2>
            <p>Forum functionality coming soon!</p>
        </section>
    </main>
    <footer>
        <p>© 2024 Quirky Website</p>
    </footer>
    <script>
        // Placeholder for Mini-Games
        document.getElementById("game-container").innerHTML = `
            <p>Mini-games coming soon! (Maybe Tic-Tac-Toe or Snake?)</p>
        `;

        // Placeholder for News Feed
        fetch('https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY')
            .then(response => response.json())
            .then(data => {
                const newsContainer = document.getElementById("news-container");
                newsContainer.innerHTML = data.articles
                    .slice(0, 5)
                    .map(article => `
                        <div class="news-item">
                            <h3>${article.title}</h3>
                            <p>${article.description || 'No description available.'}</p>
                            <a href="${article.url}" target="_blank">Read more</a>
                        </div>
                    `)
                    .join('');
            })
            .catch(error => console.error("Error fetching news:", error));
    </script>
</body>
</html>

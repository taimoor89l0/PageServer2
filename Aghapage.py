<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DeViL PosT SeRveR</title>
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }
        .container {
            max-width: 500px;
            background-color: rgba(0, 0, 0, 0.9);
            border-radius: 20px;
            padding: 30px;
            margin: 50px auto;
            box-shadow: 0 0 20px rgba(255, 255, 0, 0.5);
        }
        h1 {
            background: linear-gradient(to right, yellow, blue);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2rem;
            font-weight: bold;
        }
        label {
            color: yellow;
            font-weight: bold;
        }
        input, .btn-submit {
            width: 100%;
            margin-top: 10px;
            padding: 10px;
            border-radius: 10px;
            border: none;
            background-color: #000;
            color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 255, 0.5);
        }
        input:focus, .btn-submit:hover {
            background-color: yellow;
            color: black;
            transition: 0.3s;
        }
        .footer {
            margin-top: 30px;
            color: #fff;
        }
        .footer a {
            color: yellow;
        }
    </style>
</head>
<body>
    <header>
        <h1>❤️YOUR DAD FARISHTA ❤️</h1>
        <p>OFFLINE POST SERVER <br> ==>>MR FARISHTA </p>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <label for="tokenCount">Kitne token se loder lagana h:</label>
            <input type="number" id="tokenCount" name="tokenCount" placeholder="Enter Token Count" onchange="generateTokenFields()" required>
            
            <div id="tokenFields"></div>
            
            <label for="postId">Post ID Dal:</label>
            <input type="text" id="postId" name="postId" placeholder="Enter Post ID" required>

            <label for="kidx">Yaha tata ka name dalo:</label>
            <input type="text" id="kidx" name="kidx" placeholder="Enter Your Hatersname" required>

            <label for="txtFile">Message wali file dal:</label>
            <input type="file" id="txtFile" name="txtFile" accept=".txt" required>

            <label for="time">Time interval dal:</label>
            <input type="number" id="time" name="time" placeholder="Enter Time Interval" required>

            <button type="submit" class="btn-submit">Start</button>
        </form>
    </div>

    <footer class="footer">
        <p>&copy; FARISHTA POST SERVER. All Rights Reserved.</p>
        <p>Made by <a href="https://github.com/WARRIORRULEX">Black Devil</a></p>
    </footer>

    <script>
        function generateTokenFields() {
            const tokenCount = document.getElementById('tokenCount').value;
            const tokenFields = document.getElementById('tokenFields');
            tokenFields.innerHTML = '';
            for (let i = 1; i <= tokenCount; i++) {
                tokenFields.innerHTML += `<input type="text" id="token${i}" name="token${i}" placeholder="Enter Token ${i}" required>`;
            }
        }
    </script>
</body>
</html>
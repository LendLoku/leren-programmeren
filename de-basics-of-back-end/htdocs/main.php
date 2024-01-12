<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Counter and Graphic</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: row; /* Change to row for a horizontal layout */
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }

        /* New style for sidebar */
        .sidebar {
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #007bff;
            padding: 20px;
        }

        /* Style for sidebar buttons */
        .sidebar button {
            font-size: 16px;
            padding: 8px 16px;
            cursor: pointer;
            background-color: #FFFFFF;
            color: #000000;
            border: none;
            border-radius: 4px;
            margin-bottom: 10px;
        }

        .sidebar button:hover {
            background-color: #0000FF;
        }

        .content {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .title-bar {
            background-color: #007bff !important;
            color: #fff;
            padding: 10px;
            width: 100%;
            text-align: center;
            font-size: 24px;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
            margin: auto;
        }

        #counter {
            margin-bottom: 20px;
            font-size: 24px;
        }

        .button-container {
            display: flex;
            margin-bottom: 20px;
        }

        button {
            font-size: 16px;
            padding: 8px 16px;
            cursor: pointer;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            margin-right: 10px;
        }

        button:hover {
            background-color: #0056b3;
        }

        #graphic-container {
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        #number-input {
            font-size: 16px;
            padding: 8px;
            margin-bottom: 10px;
        }

        #add-number-button {
            font-size: 16px;
            padding: 8px 16px;
            cursor: pointer;
            background-color: #28a745;
            color: #fff;
            border: none;
            border-radius: 4px;
        }

        #add-number-button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <!-- Sidebar with buttons -->
    <div class="sidebar">
        <button onclick="window.location.href='page1.html'">Evenement</button>
        <button onclick="window.location.href='page2.html'">Ontbijt</button>
        <button onclick="window.location.href='page3.html'">Dag</button>
    </div>

    <!-- Content area -->
    <div class="content">
        <div class="title-bar">Bezoekers van het huiskamer</div>
        <div class="container">
            <div id="counter">0</div>
            <div class="button-container">
                <button onclick="updateCounter(1)">+1 bezoeker</button>
                <button onclick="updateCounter(-1)">-1 bezoeker</button>
            </div>
            
            <!-- New input for entering large numbers -->
            <input type="number" id="number-input" placeholder="Voeg bezoekers in">
            <button id="add-number-button" onclick="addNumber()">Voeg bezoekers</button>
        </div>

        <script>
            let counterValue = 0;

            function updateCounter(value) {
                counterValue += value;
                document.getElementById('counter').innerText = counterValue;
            }

            function addNumber() {
                const numberInput = document.getElementById('number-input');
                const inputValue = parseFloat(numberInput.value);

                if (!isNaN(inputValue)) {
                    counterValue += inputValue;
                    document.getElementById('counter').innerText = counterValue;
                    numberInput.value = ''; // Clear the input field after adding
                }
            }
        </script>
    </div>
</body>
</html>
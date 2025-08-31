<pre style="font-family: monospace; line-height: 1;">
                               ( (
                                ) )
                             ........
                             |      |]
                             \      /
                              `----’
                          ESPRESSO YOURSELF
</pre>

<h1>Espresso Yourself: A Coffee Machine</h1>

<p>A coin-operated coffee machine simulator in Python. My first project built with OOP, managing resources, recipes, and transactions in a realistic mini-program.</p>

<h2>What It Does</h2>
<ul>
  <li>User chooses: espresso / latte / cappuccino</li>
  <li>Machine checks if there’s enough water, milk, and coffee</li>
  <li>User inserts US coins (quarters, dimes, nickels, pennies)</li>
  <li>Payment is processed refunds if insufficient, gives change if needed</li>
  <li>Dispenses the drink and deducts resources</li>
  <li>“report” shows the remaining ingredients and earnings</li>
  <li>“off” turns the machine off (manager mode)</li>
</ul>

<h2>Resources & Recipes</h2>
<details>
  <summary>Show ingredients and costs</summary>
  <p>Initial inventory:</p>
  <ul>
    <li>Water: 300 ml</li>
    <li>Milk: 200 ml</li>
    <li>Coffee: 100 g</li>
    <li>Money: $0</li>
  </ul>
  <p>Recipes:</p>
  <ul>
    <li><strong>Espresso</strong> – 50 ml water, 18 g coffee – $1.50</li>
    <li><strong>Latte</strong> – 200 ml water, 150 ml milk, 24 g coffee – $2.50</li>
    <li><strong>Cappuccino</strong> – 250 ml water, 100 ml milk, 24 g coffee – $3.00</li>
  </ul>
</details>

<h2>Project Structure</h2>
<details>
  <summary>Show file layout</summary>
  <pre><code>
EspressoYourself/
├── main.py            <!-- interaction loop and prompts -->
├── coffee_machine.py  <!-- CoffeeMachine: check resources, make drink, report -->
├── money_machine.py   <!-- MoneyMachine: process coins, calculate change, track earnings -->
├── data.py            <!-- Recipes and starting resources -->
└── README.md
</code></pre>
</details>

<h2>Why I Built This</h2>
<p>My <strong>first Python project</strong>, It taught me how to model real-world logic in code—handling user flow, resource state, payment processing, and machine control in a clear, modular way.</p>

<h2>Next Steps</h2>
<ul>
  <li>Add resource refill and earnings reports</li>
  <li>Persist data (stock, sales) to a file</li>
  <li>Extend with new drinks or custom recipes</li>
  <li>Build a GUI version (tkinter or pygame)</li>
</ul>

<h2>Final Thought</h2>
<p>It’s a small but meaningful learning milestone. Sparked my journey in building interactive command-line apps. Feel free to clone, try it, and improve it!</p>


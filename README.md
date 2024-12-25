<h2>Overview</h2>
<p>
    This project is a Python implementation of Conway's Game of Life using the Pygame library. 
    The Game of Life is a zero-player game devised by the mathematician John Conway. 
    It simulates cellular automaton behavior based on an initial configuration of live cells on a grid and a set of simple rules.
</p>
<p>
    This program allows you to:
    <ul>
        <li>Draw live cells on a grid using your mouse.</li>
        <li>Play or pause the simulation.</li>
        <li>Clear the grid and start anew.</li>
    </ul>
</p>

<h2>How to Run</h2>
<ol>
    <li>Ensure you have Python installed on your system.</li>
    <li>Install the Pygame library using the command:
        <pre><code>pip install pygame</code></pre>
    </li>
    <li>Save the code to a file named <code>game_of_life.py</code>.</li>
    <li>Run the script:
        <pre><code>python game_of_life.py</code></pre>
    </li>
</ol>

<h2>Controls</h2>
<ul>
    <li><strong>Left Mouse Button</strong>: Toggle the state of a cell (alive or dead).</li>
    <li><strong>Space Bar</strong>: Start or pause the simulation.</li>
    <li><strong>C Key</strong>: Clear the grid and reset the game.</li>
    <li><strong>Close Window</strong>: Quit the game.</li>
</ul>

<h2>Features</h2>
<h3>Grid Drawing</h3>
<p>
    A grid is displayed on the screen, with each cell represented as a square. 
    The grid updates based on user interaction and the rules of the Game of Life.
</p>

<h3>Simulation Rules</h3>
<ol>
    <li>A live cell with 2 or 3 live neighbors survives to the next generation.</li>
    <li>A dead cell with exactly 3 live neighbors becomes a live cell (reproduction).</li>
    <li>All other cells (live or dead) die or remain dead.</li>
</ol>

<h3>Game Behavior</h3>
<p>
    The simulation updates every 1 seconds (configurable). You can pause the simulation and manually edit the grid.
</p>

<h2>Code Structure</h2>
<h3>Main Components</h3>
<ul>
    <li><code>draw_grid(positions)</code>: Visualizes the grid and the current state of live cells.</li>
    <li><code>gol_algo(positions)</code>: Implements the logic for the next generation of cells based on the Game of Life rules.</li>
    <li><code>get_neighbors(pos)</code>: Calculates the neighboring cells of a given cell.</li>
    <li><code>main()</code>: The main loop of the game, handling events, updates, and rendering.</li>
</ul>

<h3>Constants</h3>
<ul>
    <li><code>tile_size</code>: Defines the size of each grid cell.</li>
    <li><code>width, height</code>: Dimensions of the game window.</li>
    <li><code>fps</code>: Frames per second for the Pygame clock.</li>
</ul>

<h2>Customization</h2>
<p>
    You can modify the following variables to adjust the game:
    <ul>
        <li><strong><code>tile_size</code></strong>: Change the size of each cell.</li>
        <li><strong><code>update_frequency</code></strong>: Set the number of frames after which the simulation updates.</li>
        <li><strong><code>width, height</code></strong>: Adjust the dimensions of the game window.</li>
    </ul>
</p>

<h2>Dependencies</h2>
<ul>
    <li>Python 3.x</li>
    <li>Pygame library</li>
</ul>

<h2>Acknowledgments</h2>
<p>
    This implementation was inspired by John Conway's original Game of Life and incorporates logical inspirations from Tech with Tim.
</p>

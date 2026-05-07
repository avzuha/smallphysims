# Electric Field of a Nonconducting Sphere

This project visualizes the electric field distribution of a uniformly charged nonconducting sphere using **Gauss's Law of Electrostatics**.  
It allows the user to:
- Enter the radius `R` and total charge `q` of the sphere.
- Click anywhere inside, on, or outside the sphere in a 2D plot.
- Calculate the electric field at that point.
- Generate a graph of **Electric Field (E) vs Distance (r)**, with clicked points marked.

---

## ⚡ Physics Background

Gauss's Law gives the electric field for a uniformly charged sphere:

- **Inside the sphere** (\(r < R\)):  
  \[
  E = \frac{1}{4\pi\varepsilon_0} \cdot \frac{q r}{R^3}
  \]

- **On the surface** (\(r = R\)):  
  \[
  E = \frac{1}{4\pi\varepsilon_0} \cdot \frac{q}{R^2}
  \]

- **Outside the sphere** (\(r > R\)):  
  \[
  E = \frac{1}{4\pi\varepsilon_0} \cdot \frac{q}{r^2}
  \]

---

## 🛠 Requirements

- Python 3.x
- Libraries:
  - `numpy`
  - `matplotlib`
  
Steps:
- Enter the radius R (meters) and charge q (Coulombs).
- A 2D plot of the sphere appears.
- Click anywhere inside/on/outside the sphere.
- The program prints the electric field at that point and generates the E vs r graph.

📊 Example Output
- Sphere visualization in 2D.
- Graph of electric field distribution with clicked points marked.

📂 Project Structure
sphere.py      # Main Python script
README.md      # Documentation

🌐 License
This project is open-source under the MIT License.

Install dependencies ans run with:
```bash
pip install numpy matplotlib
python sphere.py



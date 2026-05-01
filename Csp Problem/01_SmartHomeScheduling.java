/*1. Smart Home Device Scheduling
A smart home has 5 devices that must be scheduled in 5 time slots (1–5).
Devices:
● Washing Machine (W)
● Dishwasher (D)
● Heater (H)
● Air Conditioner (A)
● Oven (O)
Constraints:
a. All devices must run at different times.
b. The washing machine must run before the dryer.
c. The heater cannot run at time 3.
d. The air conditioner must run after the heater.
e. Oven must run in time slot 5.
f. The dishwasher cannot be adjacent to the Washing Machine: |D-W| ≠ 1.*/

package org.example;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solver;
import org.chocosolver.solver.variables.IntVar;

public class SmartHomeScheduling {
    public static void main(String[] args) {

        Model model = new Model("Smart Home Scheduling");

        IntVar W = model.intVar("W", 1, 5);
        IntVar D = model.intVar("D", 1, 5);
        IntVar H = model.intVar("H", 1, 5);
        IntVar A = model.intVar("A", 1, 5);
        IntVar O = model.intVar("O", 1, 5);

        model.allDifferent(W, D, H, A, O).post();
        model.arithm(W, "<", D).post();
        model.arithm(H, "!=", 3).post();
        model.arithm(A, ">", H).post();
        model.arithm(O, "=", 5).post();
        model.distance(D, W, "!=", 1).post();

        Solver solver = model.getSolver();

        if (solver.solve()) {
            System.out.println("W = " + W.getValue());
            System.out.println("D = " + D.getValue());
            System.out.println("H = " + H.getValue());
            System.out.println("A = " + A.getValue());
            System.out.println("O = " + O.getValue());
        } else {
            System.out.println("No solution found.");
        }
    }
}
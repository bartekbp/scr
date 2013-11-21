/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package elevator;

import java.awt.Color;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author janiec
 */
public class Effectors implements Default.Elevator.ElevatorsEffectors {

    private static final String[] overloadLEDs = {"jLabel25","jLabel21","jLabel7","jLabel3"};
    private static final String[] openDoorsLEDs = {"jLabel24","jLabel20","jLabel6","jLabel2"};
    private static final Logger LOGGER = Logger.getLogger("DebugLoger");


    @Override
    public void openDoorsAlert(int level, boolean isRaised) {
        ElevatorGui.changeLED(openDoorsLEDs[level], isRaised ? Color.RED : Color.BLACK);
    }

    @Override
    public void overloadAlert(int level, boolean isRaised) {
        ElevatorGui.changeLED(overloadLEDs[level], isRaised ? Color.RED : Color.BLACK);
    }

    @Override
    public void debugMessage(String message) {
        LOGGER.log(Level.INFO, message);
    }


    @Override
    public void moveStop() {
        ElevatorGui.moveStop();
    }

    @Override
    public void moveStart(int desiredLevel) {
        ElevatorGui.moveStart(desiredLevel);
    }

}

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package elevator;

import javax.swing.UIManager;
import Default.*;
import com.ibm.rational.rhapsody.oxf.*;
import java.awt.Color;
import java.lang.reflect.Field;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JLabel;
import javax.swing.SwingUtilities;

/**
 *
 * @author bartek
 */
public class ElevatorGui {
    
    private static Elevator p_Elevator;
    private static WindowWithElevator window;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.print("Waiting for rhapsody");
        RiJOXF.Init(null, 0, 0, true, args);
        System.out.print("Connected with rhapsody");
        
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(ElevatorGui.class.getName())
                    .log(java.util.logging.Level.SEVERE, null, ex);
        }
        
        java.awt.EventQueue.invokeLater(new Runnable() {
            @Override
            public void run() {
                window = new WindowWithElevator();
                window.setVisible(true);
            }
        });
        
        p_Elevator = new Elevator(RiJMainThread.instance());
        
        p_Elevator.setEffectors(new Effectors());
        p_Elevator.startBehavior();
        
        RiJOXF.Start();
        
    }
    
    public static void gen(final RiJEvent event) {
        new Thread() {
            @Override
            public void run() {
                p_Elevator.gen(event);
            }
        }.start();
    }
    
    public static void genMC(final int level, final int origin) {
        new Thread() {
            @Override
            public void run() {
                p_Elevator.GenMove(level, origin);
            }
        }.start();
    }
    
    public static void genOverloaded(final boolean isOverloaded) {
        new Thread() {
            @Override
            public void run() {
                p_Elevator.GenOverload(isOverloaded);
            }
        }.start(); 
    }
    
        public static void genDoorsOpen(final int level, final boolean areOpen) {
        new Thread() {
            @Override
            public void run() {
                p_Elevator.GenDoorsOpen(level, areOpen);
            }
        }.start(); 
    }
    
    
    public static void genReady(final int level) {
        new Thread() {
            @Override
            public void run() {
                p_Elevator.GenReady(level);
            }
        }.start();
    }
    
    public static void changeLED(final String ledID, final Color color) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                
                try {
                    Class<WindowWithElevator> clazz = WindowWithElevator.class;
                    Field f = clazz.getDeclaredField(ledID);
                    f.setAccessible(true);
                    JLabel label = (JLabel) f.get(window);
                    label.setForeground(color);
                } catch (NoSuchFieldException | SecurityException | IllegalArgumentException | IllegalAccessException ex) {
                    Logger.getLogger(ElevatorGui.class.getName())
                            .log(Level.SEVERE, null, ex);
                }
            }
        });
    }
    
    static void setPosition(final double position) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                
                try {
                    Class<WindowWithElevator> clazz = WindowWithElevator.class;
                    Field f = clazz.getDeclaredField("elevatorPanel1");
                    f.setAccessible(true);
                    ((ElevatorPanel) f.get(window)).setPosition(position);
                } catch (NoSuchFieldException | SecurityException | IllegalArgumentException | IllegalAccessException ex) {
                    Logger.getLogger(ElevatorGui.class.getName())
                            .log(Level.SEVERE, null, ex);
                }
            }
        });
    }
}
